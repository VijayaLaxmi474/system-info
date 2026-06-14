from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    department = db.Column(db.String(100))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/employees")
def employees():
    all_employees = Employee.query.all()
    return render_template(
        "employees.html",
        employees=all_employees
    )

@app.route("/add", methods=["GET","POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]

        emp = Employee(
            name=name,
            email=email,
            department=department
        )

        db.session.add(emp)
        db.session.commit()

        return redirect("/employees")

    return render_template("add_employee.html")

@app.route("/delete/<int:id>")
def delete(id):

    emp = Employee.query.get(id)

    db.session.delete(emp)

    db.session.commit()

    return redirect("/employees")

@app.route("/health")
def health():
    return {"status":"UP"}

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=5000)
