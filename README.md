# URL Shortener

A self-hosted web application that converts long URLs into short, easy-to-share links.

### Tech Stack
- Backend: Python + Flask
- Frontend: HTML + CSS
- Database: SQLite (SQLAlchemy)

### How to Run
> Prerequisites
- Python 3.7+ installed

1. ### Clone or Download the Project

```bash
git clone https://github.com/Kevvy404/URL-Shortener.git
cd URL-Shortener
```

2. ### Set Up a Virtual Environment 
```bash
# Create the virtual environment
python -m venv venv

# Activate it
source venv/bin/activate      # Linux/Mac
.\venv\Scripts\activate       # Windows (PowerShell)
```

3. ### Install Dependencies
```bash
pip install flask flask-sqlalchemy werkzeug==2.3.7 flask-migrate
```
4. ### 
```bash
cd URL   #Change directory
```

5. ### Initialise the Database
```bash
python -c "from app import db, app; app.app_context().push(); db.create_all()"
```

6. ### Run the Application
```bash
python app.py
```
> Expected Output
``` 
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000 
 ```

6. ### Access the Web Application
- Open your browser and visit: http://localhost:5000

7. ### Stopping the Application
- Press Ctrl + C in your terminal to stop the Flask Server
