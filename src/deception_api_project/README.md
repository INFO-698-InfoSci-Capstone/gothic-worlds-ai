# 🧠 Deception Score API

This project exposes a trained deception detection model via a Flask API. You can send a sentence and get a predicted deception score in response.

---

## 📦 Project Structure
```
deception_api_project/
│
├── app/                           # Main application package
│   ├── __init__.py               # Initializes Flask app and loads model
│   ├── routes.py                 # Flask routes (e.g., /predict, /)
│   └── model/
│       └── loader.py             # Model/vectorizer loading utility
│
├── models/                       # Serialized ML models
│   ├── iw_deception_score_model.pkl
│   └── iw_deception_score_vectorizer.pkl
│
├── logs/                         # Runtime log files
│   └── flask_server.log
│
├── .env                          # Environment variables (host, port, etc.)
├── run.py                        # Application entry point
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```
---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd deception_api_project
```

## Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Environment Configuration
```
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=False
```

## Running the Application
Start the Flask app in the background and write logs to a file:
```
nohup python run.py > logs/flask_server.log 2>&1 &
```
 - `nohup` allows it to keep running even if the terminal is closed.
 - Output is redirected and appended to `logs/flask_server.log`.
 
## Checking Logs (in a separate terminal)
```
tail -f logs/flask_server.log
```
This will show a live stream of the logs as the server runs.
---

## Testing the API
1. Check status (GET request)
```
curl http://localhost:5000/
```

2. Get a deception score (POST request)
```
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I swear I never touched that cookie jar!"}'
```

---
## 🛑 Stopping the Server
Option 1: Gracefully stop using the PID
```
lsof -i:5000
```

Find the process ID (PID), then:
```
kill <PID>
```

Option 2: Kill by script name
```
pkill -f run.py
```

---
## 🧪 Sample Output
```
{
  "deception_score": 0.87
}
```
