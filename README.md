# ShareMyStay — Flask Website

A full website for the ShareMyStay platform, built with Python + Flask.

## Pages
- `/` — Home page (hero, how it works, why us)
- `/stays` — Browse listings (with city filter)
- `/list-home` — Form to submit a property
- `/about` — About, roadmap, stats

## Setup (first time)

1. Make sure Python 3 is installed:
   ```
   python --version
   ```

2. Install Flask:
   ```
   pip install flask
   ```
   Or with the requirements file:
   ```
   pip install -r requirements.txt
   ```

3. Run the website:
   ```
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://localhost:5000
   ```

## Project Structure
```
sharemystay/
├── app.py               ← Main Python file (routes & data)
├── requirements.txt     ← Python packages needed
└── templates/
    ├── base.html        ← Shared layout (nav, footer, styles)
    ├── index.html       ← Home page
    ├── stays.html       ← Find a stay page
    ├── list_home.html   ← List your home form
    └── about.html       ← About page
```

## Next Steps (to make it production-ready)
- Add a database (SQLite with SQLAlchemy) to store real listings
- Add user login/signup (Flask-Login)
- Add image upload for listings
- Add a payment gateway for featured listings
- Deploy to a cloud server (Render, Railway, or AWS)
