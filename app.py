from flask import Flask, render_template, redirect, url_for, flash
from forms import ContactForm
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db, ContactSubmission

load_dotenv()  # Load variables from a local .env file if present

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-only-secret')  # Set SECRET_KEY in environment for production

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db and migrations
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    """Home page with introduction"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page with detailed bio"""
    return render_template('about.html')

@app.route('/skills')
def skills():
    """Skills and services showcase"""
    return render_template('skills.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form page"""
    form = ContactForm()
    
    if form.validate_on_submit():
        # Save submission to the database
        submission = ContactSubmission(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(submission)
        db.session.commit()

        flash(f'Thank you {submission.name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
