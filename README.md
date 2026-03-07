# 🚀 Smart Attendance Portal with Supabase

A modern **AI-ready Smart Attendance Management System** built using **Streamlit, Supabase, and Python** to manage classroom attendance efficiently with a clean admin interface and cloud database.

This project demonstrates how modern backend services like **Supabase (PostgreSQL + API)** can be integrated with **Python applications** to build scalable education tools.

---

# 📌 Project Overview

Traditional attendance systems are often manual, inefficient, and difficult to manage.
This project provides a **digital attendance portal** where administrators can:

* Manage classrooms
* Track student attendance
* Store data securely in the cloud
* Access records instantly

The system uses **Supabase as the backend database** and **Streamlit for the interactive frontend dashboard**.

---

# ✨ Key Features

✅ Cloud-based attendance storage
✅ Admin dashboard for classroom management
✅ Real-time database interaction using Supabase
✅ Simple and clean Streamlit UI
✅ Easy classroom creation and configuration
✅ Secure environment variables for API keys
✅ Modular Python project structure

---

# 🏗️ Project Architecture

```
User (Admin)
      │
      ▼
Streamlit Web App
      │
      ▼
Supabase API
(PostgreSQL Database)
      │
      ▼
Attendance Records Storage
```

The application communicates with Supabase using its **Python client**, allowing seamless interaction with the PostgreSQL database.

---

# 🛠️ Tech Stack

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| **Python**       | Backend logic                         |
| **Streamlit**    | Interactive web interface             |
| **Supabase**     | Backend-as-a-service (Database + API) |
| **PostgreSQL**   | Data storage                          |
| **Git & GitHub** | Version control                       |
| **uv / venv**    | Python environment management         |

---

# 📂 Project Structure

```
Smart-Attendance-Portal-with-Supabase
│
├── Attendence
│   ├── admin.py
│   ├── attendance.py
│   └── database.py
│
├── frontend
│   └── app.py
│
├── .streamlit
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```
git clone https://github.com/sauravyadav7721/Smart-Attendance-Portal-with-Supabase.git
```

```
cd Smart-Attendance-Portal-with-Supabase
```

---

### 2️⃣ Create Virtual Environment

Using **uv / venv**

```
python -m venv smattenv
```

Activate environment

Windows:

```
smattenv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Supabase

Create a file:

```
.streamlit/secrets.toml
```

Add your Supabase credentials:

```
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_api_key"
```

⚠️ This file should **never be pushed to GitHub**.

---

### 5️⃣ Run the Application

```
streamlit run frontend/app.py
```

The app will start at:

```
http://localhost:8501
```

---

# 🗄️ Database Setup (Supabase)

Create tables in Supabase dashboard.

Example structure:

### Classroom Table

| Column     | Type |
| ---------- | ---- |
| class_name | text |
| subject    | text |
| faculty    | text |

### Attendance Table

| Column     | Type      |
| ---------- | --------- |
| student_id | text      |
| class_name | text      |
| status     | boolean   |
| timestamp  | timestamp |

---

# 📸 Project Demo

The portal allows administrators to:

* Create classroom settings
* Record student attendance
* Manage attendance records from a centralized dashboard

---

# 🎯 Learning Outcomes

This project helped demonstrate:

* Building **real-world data applications**
* Integrating **Python with Supabase**
* Designing **cloud-connected systems**
* Implementing **secure API credential management**
* Creating **interactive dashboards using Streamlit**

---

# 🌟 Future Improvements

* Face recognition attendance using **OpenCV**
* Student login portal
* Automated attendance analytics
* Email attendance reports
* Mobile responsive UI

---

# 👨‍💻 Author

**Saurav Yadav**

Data Science Student at Nalanda University
Passionate about **AI, Data Science, and Real-world Applications**

🔗 GitHub
https://github.com/sauravyadav7721

---

# 🙏 Acknowledgement

This project implementation was inspired by the learning resources and project explanation provided by **Krish Naik**, which helped in understanding the architecture and workflow of a smart attendance management system.

---

# ⭐ Support

If you found this project helpful, please consider **starring the repository** ⭐
It helps the project reach more developers and learners.

