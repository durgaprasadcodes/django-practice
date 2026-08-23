# 🚀 Django Portfolio Website

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Developer](https://img.shields.io/badge/Developer-Durga%20Prasad%20Kota-purple.svg)](https://github.com/durgaprasadcodes)

A modern, high-performance developer portfolio built with **Django**, **HTML5**, and custom **Dark Glassmorphism CSS**. Designed specifically to highlight projects, technical skillsets, stats, and contact workflows for **Durga Prasad Kota** (Python Full Stack Developer & AI/ML Engineer).

---

## ✨ Features

- 🎨 **Ultra-Premium Dark Glassmorphism UI**: Beautiful dark theme crafted using CSS glassmorphic cards, backdrop blur filters, glowing borders, and keyframe animations.
- ⚡ **Dynamic Django Views & Data**: Template context passing for personal bio data, statistics counters, social links, and skill matrices.
- 📱 **Fully Responsive Layout**: Mobile-first grid and flexbox system seamlessly adapting across desktop, tablet, and mobile displays.
- 🛠️ **Interactive Skill Cards**: Custom skill matrix featuring icon matching for Python, FastAPI, Django, React, Databases, ML, and DevOps tools.
- 📬 **Contact Workflow**: Sleek contact form equipped with CSRF protection and interactive focus states.
- 🎯 **Active Tab Highlighting**: Dynamic navbar tracking active routes using Django's resolver match.

---

## 🛠️ Technology Stack

- **Backend Framework**: Python 3.x, Django 5.x
- **Frontend Architecture**: HTML5, Vanilla CSS3 (Custom Glassmorphism Design System)
- **Typography & Icons**: Google Fonts (*Plus Jakarta Sans*), FontAwesome 6
- **Version Control**: Git & GitHub

---

## 📁 Project Structure

```text
portfolio/
├── manage.py
├── db.sqlite3
├── README.md
├── portfolio/              # Django core settings & configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── routes/                 # Portfolio app views, models, and routes
│   ├── views.py            # Context data for home, about, skills, contact
│   ├── urls.py             # URL routing rules
│   └── models.py
├── static/                 # Static assets (CSS & Images)
│   ├── css/
│   │   ├── navbar.css
│   │   ├── home.css
│   │   ├── about.css
│   │   ├── skills.css
│   │   ├── contact.css
│   │   └── footer.css
│   └── img/
│       └── cat.jpeg
└── templates/              # HTML Templates
    ├── navbar.html
    ├── footer.html
    ├── home.html
    ├── about.html
    ├── skills.html
    └── contact.html
```

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project running on your local machine.

### Prerequisites

Ensure you have Python 3.10+ and `pip` installed:

```bash
python --version
```

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/durgaprasadcodes/portfolio-with-django.git
   cd portfolio-with-django/portfolio
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🌐 Routes Overview

| Route | View | Description |
| :--- | :--- | :--- |
| `/` | `home` | Hero section, social buttons, statistics grid, and profile avatar |
| `/about/` | `about` | Education, specialization cards, career goals, and highlight banner |
| `/skills/` | `skills` | Interactive technical skills grid with icon badges |
| `/contact/` | `contact` | Get in touch form with CSRF security |

---

## 👤 Author

**Durga Prasad Kota**
- **GitHub**: [@durgaprasadcodes](https://github.com/durgaprasadcodes)
- **LinkedIn**: [Durga Prasad Kota](https://linkedin.com/in/your-linkedin)
- **LeetCode**: [@Durga_Prasad_Kota](https://leetcode.com/Durga_Prasad_Kota)
- **Portfolio**: [durgaprasadcodes.vercel.app](https://durgaprasadcodes.vercel.app)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
