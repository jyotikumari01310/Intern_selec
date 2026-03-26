# 🚀 Internship Project – Scalable REST API with Authentication

## 📌 Overview

This project is a full-stack application built as part of a backend developer internship assignment. It demonstrates the design and implementation of a secure, scalable REST API with authentication, role-based access control, and a basic frontend interface.

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* MySQL
* SQLAlchemy
* JWT Authentication

### Frontend

* React.js
* Axios

---

## 🔐 Features

### ✅ Authentication

* User Registration
* User Login
* Password hashing using bcrypt
* JWT-based authentication

### 👤 Role-Based Access

* User and Admin roles
* Admin-only operations (e.g., delete tasks)

### 📦 Task Management (CRUD)

* Create Task
* Get All Tasks
* Delete Task (Admin only)

### 📘 API Documentation

* Swagger UI available at:

```
http://127.0.0.1:8000/docs
```

---

## 🗄️ Database

* MySQL database used
* Tables:

  * Users
  * Tasks

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/internship-project.git
cd internship-project
```

---

### 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

👉 Update database config in:

```
app/config/database.py
```

Replace:

```
YOUR_PASSWORD
```

with your MySQL password.

---

### 3️⃣ Run Backend

```bash
python -m uvicorn main:app --reload
```

👉 Backend runs at:

```
http://127.0.0.1:8000
```

---

### 4️⃣ Frontend Setup

```bash
cd ../frontend
npm install
npm start
```

👉 Frontend runs at:

```
http://localhost:3000
```

---

## 🔐 Authentication Flow

1. Register user
2. Login to receive JWT token
3. Use token in requests:

```
Authorization: Bearer <token>
```

---

## 🧪 API Testing

Use Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Scalability Considerations

* Modular project structure
* Can be extended to microservices
* JWT-based stateless authentication
* Can integrate Redis for caching
* Can deploy using Docker

---

## 📂 Project Structure

```
internship-project/
│
├── backend/
│   ├── app/
│   ├── main.py
│
├── frontend/
│   ├── src/
│
├── README.md
```

---

## 🎯 Future Improvements

* Update & Edit Task functionality
* Better UI/UX design
* Pagination for tasks
* Docker deployment
* Logging system

---

## 📬 Submission

GitHub Repository:
👉 https://github.com/jyotikumari01310/intern_selec

---

## 🙌 Author

Jyoti
