# TaskNest - Company Employee Portal

## 🎉 Live Now: [TaskNest on Render](https://tasknest-company-portal.onrender.com)

![Signup Page](https://raw.githubusercontent.com/bharaths002/company-portal/main/path/to/signup_thumbnail.png)

---

## 🌟 Tagline:

**"Boom! A brand new project launch - TaskNest, where employee management meets sleek design!"**

---

## 📊 Overview

TaskNest is a responsive, full-stack **employee management portal** built with Django. It allows users to register, log in, and manage their portal activity in a seamless UI that works flawlessly across desktop and mobile devices. Ideal for HR teams or small company intranet dashboards.

---

## 🌐 Live Demo

> ✨ Deployed on **Render**

* [https://tasknest-company-portal.onrender.com](https://tasknest-company-portal.onrender.com)

---

## ⚖️ Tech Stack

### 🎨 Frontend

* **HTML5** - Semantic markup for structure
* **CSS3** - Custom styles for all pages, responsive design with media queries
* **Vanilla JavaScript** - Form validation, minor interactivity
* **Responsive UI** - Designed to adapt to both PC and mobile screens
* **Dashboard Theme** - Static homepage with user-friendly sections

### 🚀 Backend

* **Django 3.2.25** - Robust Python web framework
* **Django Authentication** - Built-in user registration and login system
* **Views/URL Routing** - Clean URL structure with meaningful navigation paths
* **Django Signals** *(optional)* - Tracks user login activity (extendable)

### 📁 Templates & Static

* Templates stored in `templates/`
* Static files from `static/` and `portal/static/` using `WhiteNoise` for production serving

### 󰔐 Database

* **SQLite** (default)

  * Suitable for local and quick deployment
  * Configured using `dj-database-url`
* Can be extended to PostgreSQL/MySQL

---

## 📝 Features

* 📅 **Signup/Login System** (Custom styling + Django Auth)
* 🏢 **Responsive Dashboard** with user info and navigation
* 🎓 **Form validation** on front-end (JS)
* 📲 **Mobile-first Design**
* ✨ **Production-ready** with:

  * `collectstatic`
  * Whitenoise
  * Debug=False for security
  * Render Deployment Support

---

## ⚙️ Setup & Deployment

### ⚡ Local Setup

1. Clone repo:

```bash
git clone https://github.com/bharaths002/company-portal.git
cd company-portal
```

2. Create a virtual environment:


python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate


3. Install dependencies:


pip install -r requirements.txt


4. Run locally:


python manage.py runserver


### 🏠 Deployment (Render)

* `Build Command:`


pip install -r requirements.txt && python manage.py collectstatic --noinput


* `Start Command:`

```bash
gunicorn company.wsgi:application
```

* Set environment variables:

  * `DEBUG=False`
  * `ALLOWED_HOSTS=yourdomain.onrender.com`
  * `DJANGO_SECRET_KEY=your_secure_key`

---

## 📝 Future Enhancements

* [ ] Add employee CRUD operations
* [ ] Role-based access (admin/user)
* [ ] Notifications or task manager
* [ ] Dynamic dashboard with charts (Plotly/D3.js)

---

## 👨‍💼 What I Learned

* ✍️ Django MVC structure in real-time
* ✅ Deployment on Render with Gunicorn and Whitenoise
* 🌟 Styling static templates for responsiveness
* 📄 Connecting environment variables securely
* ✨ Handling static files and `collectstatic` issues

---

## 🚀 Author

**Bharath S**
Full Stack Developer | Python & Django Enthusiast
[LinkedIn](https://www.linkedin.com/in/yourprofile) | [GitHub](https://github.com/bharaths002)

---

> ❤️ Loved this project? Feel free to give it a star and share!
