import joblib
import os

# app/model/loader.py
from tensorflow.keras.models import load_model
from transformers import DistilBertTokenizer
import numpy as np
import tensorflow as tf



def load_model_and_vectorizer():
    model = joblib.load(os.path.join('models', 'iw_deception_score_model.pkl'))
    vectorizer = joblib.load(os.path.join('models', 'iw_deception_score_vectorizer.pkl'))
    return model, vectorizer


# --- R2 Metric ---
class R2Score(tf.keras.metrics.Metric):
    def __init__(self, name="r2_score", **kwargs):
        super().__init__(name=name, **kwargs)
        self.sse = self.add_weight(name="sse", initializer="zeros")
        self.sst = self.add_weight(name="sst", initializer="zeros")
        self.count = self.add_weight(name="count", initializer="zeros")
        self.mean_y = self.add_weight(name="mean_y", initializer="zeros")

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_true = tf.reshape(y_true, [-1])
        y_pred = tf.reshape(y_pred, [-1])

        # Update running mean
        batch_count = tf.cast(tf.shape(y_true)[0], tf.float32)
        total_count = self.count + batch_count
        new_mean = (self.mean_y * self.count + tf.reduce_sum(y_true)) / total_count

        # Compute batch SSE and SST
        batch_sse = tf.reduce_sum(tf.square(y_true - y_pred))
        batch_sst = tf.reduce_sum(tf.square(y_true - new_mean))

        # Update state
        self.sse.assign_add(batch_sse)
        self.sst.assign_add(batch_sst)
        self.count.assign(total_count)
        self.mean_y.assign(new_mean)

    def result(self):
        return 1.0 - (self.sse / (self.sst + tf.keras.backend.epsilon()))

    def reset_states(self):
        self.sse.assign(0.0)
        self.sst.assign(0.0)
        self.count.assign(0.0)
        self.mean_y.assign(0.0)

# Load model and tokenizer
model = load_model("models/model.keras", custom_objects={"R2Score": R2Score})
# model = load_model("./../../models/model.keras", custom_objects={"R2Score": R2Score})
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")


# Preprocess a single input
def preprocess_text(text, max_len=128):
    encoded = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_len,
        padding='max_length',
        truncation=True,
        return_attention_mask=False,  # Set to True if your model uses attention
        return_tensors='np'
    )
    return encoded["input_ids"]

# Predict deception score for a single text input
def predict_deception_score_from_model(text):
    input_ids = preprocess_text(text)
    prediction = model.predict(input_ids)
    return float(prediction[0])


# # text = "I never saw that email before today."
# text = "You must believe me when I say, the cries you heard last night were nothing more than the wind through the towers. There are no prisoners here… only guests who choose to stay, as you have."
# score = predict_deception_score_from_model(text)
# print(f"Deception Score: {score:.4f}")