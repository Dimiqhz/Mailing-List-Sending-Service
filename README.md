# Mailing-List-Sending-Service

This project is a mailing-list sending service built using Python 2.7, Django 1.9.9, following the MVC architectural pattern. It provides functionality to manage subscribers, create email campaigns, track email activity, and handle subscriptions and unsubscriptions.

(The project was performed as a test task)
---

## 📌 Features

- **Mailing Management:** Create, schedule, and manage email campaigns.
- **Subscriber Management:** Maintain subscriber lists efficiently.
- **Logging & Tracking:** Track email opens by subscribers.
- **Subscription Handling:** Easy subscription and unsubscription functionality.
- **Django Admin:** Administrative interface for advanced operations.

---

## 🛠️ Technology Stack

- Python 2.7
- Django 1.9.9
- Ajax & jQuery
- Celery (for asynchronous tasks)
- Redis (broker for Celery tasks)
- Bootstrap & Bootstrap DateTimePicker
- SQLite (default database; PostgreSQL/MySQL optional)
- Bleach (for XSS protection)

---

## 🌐 Project URL Routes

| URL                                    | Description                        |
|----------------------------------------|------------------------------------|
| `/mailing/create/`                     | Create a new mailing campaign      |
| `/mailing/list/`                       | View all mailing campaigns         |
| `/mailing/logs/`                       | View logs of opened emails         |
| `/subscribers/`                        | List and manage subscribers        |
| `/subscribers/subscribe/`              | Subscription page                  |
| `/subscribers/unsubscribe/<email>/`    | Unsubscription page                |
| `/admin/`                              | Django admin interface             |

---

## 🚀 Installation Guide

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Dimiqhz/Mailing-List-Sending-Service.git
cd Mailing-List-Sending-Service
```

### 2️⃣ Set up the virtual environment and install dependencies
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 3️⃣ Start Redis server (required for Celery)
Make sure Redis is installed and running:

```bash
redis-server
```

### 4️⃣ Configure Django settings (Optional)
Adjust settings (`settings.py`) for database configurations and SMTP if necessary.

### 5️⃣ Run database migrations

```bash
python manage.py migrate
```
### 6️⃣ Start Celery worker

```bash
celery -A Mailing-List-Sending-Service worker --loglevel=info
```
### 7️⃣ Run the Django development server
```bash
python manage.py runserver
Access your app at http://127.0.0.1:8000/
```

## 🔒 Security & Validation
Django built-in validation is complemented by the Bleach library for enhanced XSS protection.
SMTP setup is recommended for production-level email sending.

## 📌 Notes
SQLite is used by default for simplicity. Consider migrating to PostgreSQL or MySQL in production.
Basic Bootstrap styling included; customize the UI for production environments.
