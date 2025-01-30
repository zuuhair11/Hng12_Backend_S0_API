# HNG12 Stage 0 Backend Task

## 📌 Project Description
This is a simple public API built with **FastAPI** that returns basic information, including:
- My registered email address (used in HNG12 Slack).
- The current date and time in **ISO 8601 UTC format**.
- The **GitHub URL** of this project's codebase.

This API is built as part of the **HNG12 Backend Internship Stage 0 Task** and is deployed to a publicly accessible endpoint.

---

## 🚀 API Endpoint
### **GET /**
**Response Format (200 OK):**
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

---

## 🛠️ Setup Instructions
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2️⃣ Create a Virtual Environment (Optional, but Recommended)**
```sh
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install fastapi uvicorn
```

### **4️⃣ Run the API Locally**
```sh
uvicorn main:app --reload
```

### **5️⃣ Test the API**
Open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 🌍 Deployment
The API is live and accessible at:
🔗 **[your-deployed-url]**

**Deployment Platforms:**
- Render: [https://render.com](https://render.com)
- Railway: [https://railway.app](https://railway.app)

---


## 📝 Additional Information
- **Programming Language:** Python (FastAPI)
- **Response Format:** JSON
- **Handles CORS:** Yes
- **Hosting:** Publicly accessible

---
## Head up to HNG Talents pool to meet a lot of skilled developers.

- [Python Developers](https://hng.tech/hire/python-developers)
- [C# Developers](https://hng.tech/hire/csharp-developers)
- [Go Developers](https://hng.tech/hire/golang-developers)
- [PHP Developers](https://hng.tech/hire/php-developers)
- [Java Developers](https://hng.tech/hire/java-developers)
- [Node.js Developers](https://hng.tech/hire/nodejs-developers)

---

## 📬 Contact
For any questions or contributions, feel free to reach out:
- GitHub: [zuuhair11](https://github.com/zuuhair11)
- Email: zouhairsahtout66@gmail.com
