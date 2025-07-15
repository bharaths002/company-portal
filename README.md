# TaskNest - Company Employee Portal

## 🎉 Live Now: [TaskNest on Render](https://tasknest-company-portal.onrender.com)

![Signup Page](https://raw.githubusercontent.com/bharaths002/company-portal/main/path/to/signup_thumbnail.png)

---

## 🌟 Tagline:

**"Boom! A brand new project launch - TaskNest, where employee management meets sleek design!"**
[![Deploy on Render](https://img.shields.io/badge/Deployed%20on-Render-5f5fff?logo=render&logoColor=white&style=for-the-badge)](https://tasknest-company-portal.onrender.com)


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

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run locally:

```bash
python manage.py runserver
```

### 🏠 Deployment (Render)

* `Build Command:`

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

* `Start Command:`

```bash
gunicorn company.wsgi:application
```

* Set environment variables:

  * `DEBUG=False`
  * `ALLOWED_HOSTS=tasknest-company-portal.onrender.com
  * `DJANGO_SECRET_KEY=django-insecure-&6tj*a&e_2_-5sk)=w!68-98(lb3v-tfe@pv$7ugc)pz(+2k6f

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
[LinkedIn](https://www.linkedin.com/in/bharaths18?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3ByqxqTf9xRe2L4IoVjo85DQ%3D%3D) | [GitHub](https://github.com/bharaths002)

---

> ❤️ Loved this project? Feel free to give it a star and share!
