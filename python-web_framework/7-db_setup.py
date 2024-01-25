"""application to configure database connection"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<db_username>:<db_password>@<db_host>/<db_name>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your USER Model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

# Create Database Tables
def create_tables():
    with app.app_context():
        db.create_all()

# Root Route
@app.route('/')
def root():
    return 'Hello, ALX Flask!'

if __name__ == '__main__':
    # Run Flask application with database configuration
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 7-db_setup.py <db_username> <db_password> <db_name>")
        sys.exit(1)

    db_username, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@localhost/{db_name}'
    create_tables()

    app.run(debug=True)

