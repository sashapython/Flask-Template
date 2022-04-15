#Importing stuff
from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy

#Initializing app and db
app = Flask(__name__)
db = SQLAlchemy(app)

#Config
app.config["SECRET_KEY"] = "your_secret_key"

#Database location DONT CHANGE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

#Routes here:

#Change this route later
@app.route('/')
def home():
    return render_template('it_worked.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
