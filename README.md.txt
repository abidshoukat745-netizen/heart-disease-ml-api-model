# ❤️ Heart Disease Prediction API (Dockerized)

A production-ready **Heart Disease Prediction API** built with FastAPI and Docker. This project allows users to send patient health data and receive predictions about the likelihood of heart disease using a trained machine learning model.

---

## 🚀 Features

* ⚡ FastAPI-based high-performance REST API
* 🧠 Machine Learning model for heart disease prediction
* 📦 Fully Dockerized for easy deployment
* 🔄 JSON-based request/response handling
* 🧪 Interactive API docs with Swagger UI
* 🛠 Easy integration with frontend or other services

---

## 🏗 Project Structure

```
heart-disease-api/
│
├── main.py                # Main FastAPI application
├── model.pkl            # Trained ML model
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .gitignore
└── README.md
```

---

## 🧠 Model Information

The model is trained on a heart disease dataset using machine learning techniques.
It predicts whether a patient is likely to have heart disease based on input features such as:

* Age
* Sex
* Chest pain type
* Blood pressure
* Cholesterol levels
* Maximum heart rate
* And more...

---

## 🐳 Docker Setup

### 1. Build Docker Image

```bash
docker build -t heart-disease-api .
```

### 2. Run Container

```bash
docker run -d -p 8000:8000 heart-disease-api
```

The API will be available at:

👉 http://localhost:8000

---

## 📡 API Endpoints

### 🔍 Root Endpoint

```http
GET /

---

### ❤️ Predict Heart Disease

```http
POST /predict
```

#### Request Body (JSON):

```json
{
  "age": 45,
  "sex": 1,
  "cp": 3,
  "trestbps": 120,
  "chol": 233,
  "thalach": 150,
  "exang": 0
}
```

#### Response:

```json
{
  "prediction": 1
}
```

* `1` → Heart Disease Detected
* `0` → No Heart Disease

---

## 📚 API Documentation

Once the server is running, access:

* Swagger UI: http://localhost:8000/docs
* ReDoc: http://localhost:8000/redoc

---

## ⚙️ Installation (Without Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-api.git
cd heart-disease-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn app:app --reload
```

---

## ☁️ Deployment Options

You can deploy this API on:

* Docker Hub
* AWS EC2 / ECS
* Google Cloud Run
* Azure Container Apps

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Abid Ali**
GitHub: https://github.com/abidshoukat745-netizen

---

## ⭐ Support

If you like this project, please ⭐ the repository!

---
