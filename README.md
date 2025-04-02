# Predictive Model API

## 📌 Overview
This FastAPI-based application exposes a simple predictive model via a REST API. The model takes a numeric input and returns a numeric prediction.

## 🚀 Features
- **GET /predict**: Accepts a numeric input as a query parameter and returns a prediction.
- **POST /predict**: Accepts a JSON payload with a numeric input and returns a prediction.
- **Lightweight & Fast**: Built with FastAPI for high performance.

## 🛠 Project Structure
```
predictive_api/
│── app/
│   │── __init__.py
│   │── main.py          # FastAPI app initialization
│   │── models.py        # Pydantic models
│   │── routes.py        # API routes
│   │── services.py      # Business logic
│   │── config.py        # Configuration settings
│── model/
│   │── simple_model.pkl # Pre-trained model
│── requirements.txt     # Dependencies
│── README.md            # Documentation
│── .gitignore           # Ignore unnecessary files
│── run.py               # Entry point to start the app
```

## 🔧 Setup & Installation
### **1️⃣ Clone the Repository**
```
git clone https://github.com/your-repo-name.git
cd predictive_api
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```
python run.py
```

The server will start at: `http://127.0.0.1:8000`

## 📡 API Endpoints
### **1️⃣ GET /predict**
- **Request:**
  ```
  curl "http://127.0.0.1:8000/predict?x=4.2"
  ```
- **Response:**
  ```
  {
    "prediction": 9.8
  }
  ```

### **2️⃣ POST /predict**
- **Request:**
  ```
  curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"x": 4.2}'
  ```
- **Response:**
  ```
  {
    "prediction": 9.8
  }
  ```

## 🌐 Deployment
To deploy, you can use any free-tier cloud hosting like:
- **Render**
- **Railway**
- **Fly.io**
- **Vercel (with FastAPI adapter)**