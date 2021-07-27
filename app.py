from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, sqlalchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dba@localhost:5433/sampledb'
db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email



@app.route("/student/<int:page_num>")
def student(page_num):
    student = Student.query.paginate(per_page=5, page=page_num, error_out=True)
    return render_template("index.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)