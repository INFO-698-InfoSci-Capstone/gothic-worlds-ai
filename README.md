# Narrator AI  + Research Compendium

![Homepage](./src/frontend/public/images/Narrator_AI_Homepage.jpg)

Narrator AI is a gothic-themed chatbot where users can chat with literary characters like Dracula and Frankenstein. It supports AI models including OpenAI, DeepSeek, Claude, and local models via Ollama.

This repository also includes a reproducible research compendium containing project configurations, logs, and data directories for research-oriented exploration and Docker deployment.

---

## 🗂 File Organization

```
.
Gothic-Worlds-Ai/
├── analysis/                      # Research compendium
│   ├── logs/                      # Progress logs
│   ├── figures/                   # Manuscript figures
│   └── supplementaryMaterials/
│       ├── supplementaryFigures/ # Supplementary figures
│       └── supplementaryTables/  # Supplementary tables
├── src/                           # Main application source
│   ├── backend/                   # Express.js backend
│   ├── frontend/                  # Next.js frontend
│   ├── data/                      # Raw and derived datasets
│   ├── deception_api_project/     # Flask API for deception scoring
│   │   ├── app/
│   │   ├── models/
│   │   ├── logs/
│   │   ├── .env
│   │   ├── run.py
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── .env                       # Environment variables
│   ├── .gitignore                 # Ignore rules for this subdir
│   ├── start.bat                  # Windows launch script
│   └── start.sh                   # Mac/Linux launch script
├── CONDUCT.md                     # Contributor code of conduct
├── DESCRIPTION                    # Project description metadata
├── LICENSE                        # License information
└── README.md                      # Combined documentation
```
---

## 🛠 Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/INFO-698-InfoSci-Capstone/gothic-worlds-ai.git
cd gothic-worlds-ai
```

### 2. Configure Environment Variables

- In `/src/` dir `.env` file add your API keys and custom settings:
  ```
  BACKEND_HOST=http://localhost
  BACKEND_PORT=5001
  FRONTEND_HOST=http://localhost
  FRONTEND_PORT=3000 # frontend does not automatically use this; update port in package.json dev script
  JWT_SECRET=
  NODE_ENV=development
  OPENAI_API_KEY=
  CLAUDE_API_KEY=
  DEEPSEEK_API_KEY=
  OLLAMA_API_URL=http://localhost:11434
  MONGODB_URI=
  # ALLOWED_ORIGINS=http://localhost:3000
  DECEPTION_API_URL=http://149.165.171.120:5000/predict
  ```

### 3. Install Dependencies

```bash
cd src/backend && npm install
cd ../frontend && npm install
```

### 4. Run the App

#### Option A: Using Start Script (recommended)
```
cd src
```

- On **Mac/Linux**:
    - give execution permission to the script.
        ```bash
        chmod +x start.sh
        ```
        ```bash
        ./start.sh
        ```

- On **Windows**:
    -  ```bash
        start.bat
        ```

Through Shell/Batch will perform these Actions:

- Kill existing processes on ports given in `.env` (ex: 3000/5000)
- Start the backend (ex: `localhost:5000`)
- Start the frontend (ex: `localhost:3000`)

#### Option B: Run FrontEnd & BackEnd Services Separately (In case `start shell/bat` file doesn't work)

In separate terminals:

make sure you are in `/src/` folder

- **Backend**

  ```bash
  cd backend
  npm run dev
  ```
Backend should be running on `http://localhost:5000` if you specify same in `.env`

- **Frontend**

  ```bash
  cd frontend
  npm run dev
  ```
Frontend should be running on `http://localhost:3000` if you specify same in `.env`

---

## 🧠 Deception Score API (Subproject)
The Deception Score API is a Flask-based microservice that uses a trained machine learning model to analyze a sentence and return a deception score.

🔹 Features:

RESTful API with `/predict` endpoint \
Pretrained model using `scikit-learn` \
Logs all requests and predictions \
Runs as a background process with `nohup`

🔹 How to Use:
```
# change dir to deception score api dir
cd deception_api_project

# Run server in background
nohup python run.py > logs/flask_server.log 2>&1 &

# Check if it's running
curl http://localhost:5000/

# Predict deception score
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I swear I never touched that cookie jar!"}'
```

🔹 Output Example:
```
{ "deception_score": 0.87 }
```
For detailed setup and structure, see the `deception_api_project/README.md`.

---

## 🧠 Features

- Gothic-styled chat interface
- Choose characters like Dracula, Wednesday, etc.
- Support for OpenAI, Claude, DeepSeek, and local Ollama models
- Built-in demo mode (no API keys needed)
- JWT-based authentication
- Persistent conversation history
- Deception Score for Each Response 

---

## 🧪 Demo Mode

Without API keys, the app falls back to:

- Simulated chat responses
- Mock login
- Basic characters and flows

---

## 💻 Tech Stack

| Layer     | Tech                             |
| --------- | -------------------------------- |
| Frontend  | Next.js (React)                  |
| Backend   | Express.js (Node)                |
| Auth      | JWT (optional)                   |
| AI Models | OpenAI, Claude, Ollama, DeepSeek |

---

## 🧪 Local Model (Ollama)

Install [Ollama](https://ollama.ai) and pull any model which works for you:

```bash
ollama pull llama3.2:1b
```

---

## 🧾 Research Compendium Overview

This repository is structured for reproducible research:

  - `analysis/logs/` – Notes and progress logs

  - `analysis/data/` – Raw and derived datasets

  - `analysis/figures/` – Manuscript visuals

  - `analysis/supplementaryMaterials/` – Extra tables/figures

Future updates will include a Dockerfile and binder/ container to simplify deployment and reproducibility.

## 🔐 Demo Login

In demo mode, you can use any credentials — no real auth is enforced.

---

## 🦪 License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

Feel free to fork, use, or extend this project for your own gothic adventures or academic research!
