import urllib.parse
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


params = urllib.parse.quote_plus(os.environ["AzureSQLConnectionString"])

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mssql+pyodbc:///?odbc_connect={params}"

# basedir = os.path.abspath(os.path.dirname(__file__))

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
#     basedir, "database.db"
# )
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.firstname}>"


@app.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)
