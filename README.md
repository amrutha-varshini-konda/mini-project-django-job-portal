# 🚀 JobConnect Portal

JobConnect is a full-stack web application designed to connect job seekers with employers. It features a robust **Django REST Framework** backend with JWT authentication and a sleek **Tailwind CSS** frontend.

---

## ✨ Features

* **User Authentication:** Secure user registration and login using JSON Web Tokens (JWT).
* **Job Listings & Management:** Authenticated users can post new job openings (title, description, location, salary).
* **Live Search:** Filter available jobs instantly by title or location.
* **Job Applications:** Apply directly to jobs with applicant details and resume links.
* **Application Tracker:** Dedicated "My Applications" tab to view all submitted applications.
* **Persistent State:** Uses `localStorage` on the frontend and SQLite on the backend to track application states and prevent duplicate submissions.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework, djangorestframework-simplejwt
* **Frontend:** HTML5, JavaScript (ES6+), Tailwind CSS
* **Database:** SQLite

---

## ⚙️ Getting Started Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/amrutha-varshini-konda/jobconnect.git](https://github.com/amrutha-varshini-konda/jobconnect.git)
cd jobconnect