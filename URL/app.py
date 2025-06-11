from flask import Flask, render_template, request, redirect
import string
import random
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(500), nullable=False)
    short = db.Column(db.String(10), unique=True, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original = request.form['url']
        short = generate_short_code()
        
        # Check if the URL already exists in the DB
        existing_url = URL.query.filter_by(original=original).first()
        if existing_url:
            short = existing_url.short
        else:
            new_url = URL(original=original, short=short)
            db.session.add(new_url)
            db.session.commit()
        
        short_url = request.host_url + short
        return render_template('home.html', short_url=short_url)
    
    return render_template('home.html')

@app.route('/<short>')
def redirect_to_url(short):
    url_entry = URL.query.filter_by(short=short).first_or_404()
    return redirect(url_entry.original)

if __name__ == '__main__':
    app.run(port=5001)
