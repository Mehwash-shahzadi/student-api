# 🎓 Student Management System API

A clean, modular RESTful API built with **FastAPI** and **SQLModel**, designed for managing students, courses, enrollments, grades, and attendance. Powered by **PostgreSQL**, configured using **.env**, and managed with **Poetry** for reliability and portability.

---

## 📌 Overview

This project provides an extensible backend for academic or institutional use cases, enabling:

- Student registration and management (Full CRUD)
- Course management (Create/Read)
- Student-course enrollment (Create/Read)
- Grade assignment (Create/Read)
- Attendance tracking (Create/Read)

---

## ⚙️ Tech Stack

| Layer           | Technology    |
| --------------- | ------------- |
| Framework       | FastAPI       |
| ORM             | SQLModel      |
| Database        | PostgreSQL    |
| Config          | python-dotenv |
| Dependency Mgmt | Poetry        |
| Client GUI      | TablePlus     |
| Editor          | VS Code       |

---

## 📁 Folder Structure

student_management/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── config/
│ │ └── db.py # Database setup
│ ├── models/ # SQLModel database models
│ ├── schemas/ # Pydantic request/response models
│ ├── routers/ # API route definitions
│ └── utils/ # Reusable utilities
│
├── .env # Environment variables
├── .gitignore # Git exclusions
├── pyproject.toml # Poetry project config
├── poetry.lock # Locked dependencies
├── requirements.txt # Optional pip support
└── README.md # Project documentation

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student_management.git
cd student_management
```

3. Install dependencies

poetry install

Alternative: pip

pip install -r requirements.txt

▶️ Run the Application

Using Poetry
poetry run uvicorn app.main:app --reload
