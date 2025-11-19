"""
In-Class API: Student   (Flask + SQLite)
LAB API: Student Housing  option need to be added (Flask + SQLite)
*** LAB API PART WILL BE FOR LAB PARTICIPATION ASSIGNMENT***

Implements:
- Full Student CRUD (CREATE, READ, UPDATE, DELETE)
- Full Housing endpoints:
    1) GET /students/<int:id>/verify
    2) PUT /housing/<int:student_id>
    3) POST /housing
    4) DELETE /housing/<int:student_id>
"""

"""
How To:


STEP 1: CREATE A VIRTUAL ENV AND INSTALL REQUIRED PACKAGE THEIR [BEST PRACTICE]
            python -m venv .venv
            source .venv/bin/activate
            .venv/bin/activate  [WINDOWS USER]

STEP 2: INSTALL REQUIRE API PACKAGE AND IN-MEMORY SQLite DATABASE
            pip install flask
            pip install flask-sqlalchemy

STEP 3: YOU CAN STORE YOUR REQUIRED PACKAGES FOR PORTABILITY
            pip freeze > requirements.txt
            [IF YOU WANT TO RUN YOUR CODE IN A DIFFERENT PYTHON VERSION]
                pip install -r requirements.txt

STEP 4: DEVELOP YOUR CODE

STEP 5: ONCE YOUR APPLICATION IS READY TO TEST EXECUTE BELLOW COMMANDS IN TERMINAL

            UNIX USER:
                export FLASK_APP=app.py
                export FLASK_ENV=development
        
            WINDOWS USER:
                set FLASK_APP=app.py
                set FLASK_ENV=development

STEP 6: TEST YOUR APPLICATION
            flask run 
            --or---
            flask --app app.py run

NOW YOU CAN SEE YOUR PROGRAM RUNNING UNDER AN URL E.G. HTTPS://127.0.0.1:xxxx  [XXXX IS PORT NUMBER]

YOU CAN USE BELLOW COMMANDS FROM A DIFFERENT TERMINAL TO INVOKE YOUR ENDPOINTS
curl -Uri 127.0.0.1:XXXX -Method GET
curl -Uri 127.0.0.1:XXXX/students -Method GET
curl -Uri http://127.0.0.1:XXXX/students -Method POST -Body '{"name": "Alice", "major": "CS", email": "alice@floridapoly.edu"}'  -ContentType "application/json"
curl -Uri 127.0.0.1:XXXX/students/1 -Method GET
curl -Uri 127.0.0.1:XXXX/students/1 -Method  PUT -Body '{"name": "Alice",  "major": "CS", "email": "alice123@floridapoly.edu"}'  -ContentType "application/json"

"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# -------------------------
# MODELS
# -------------------------

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    major = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)

    housing = db.relationship("Housing", back_populates="student", uselist=False)

    def __repr__(self):
        return f"{self.name} - {self.major} - {self.email}"


class Housing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), unique=True, nullable=False)
    housing_status = db.Column(db.String(120), nullable=False)

    student = db.relationship("Student", back_populates="housing")

    def __repr__(self):
        return f"StudentID: {self.student_id} - Status: {self.housing_status}"


# Ensure the database tables are created when the app runs
with app.app_context():
    db.create_all()


# -------------------------
# BASIC INDEX
# -------------------------

@app.route('/')
def index():
    return 'Student & Housing API (Solution Version)'


# -------------------------
# STUDENT CRUD
# -------------------------

# GET all students
@app.route('/students')
def get_students():
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {
            "id": student.id,
            "name": student.name,
            "major": student.major,
            "email": student.email
        }
        output.append(student_data)
    return {"students": output}


# GET a single student by ID
@app.route('/students/<int:id>')
def get_student(id):
    student = Student.query.get_or_404(id)
    return {
        "id": student.id,
        "name": student.name,
        "major": student.major,
        "email": student.email
    }


# POST: add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json

    if not data or "name" not in data or "email" not in data:
        return {"error": "Missing 'name' or 'email' in request body"}, 400

    student = Student(
        name=data["name"],
        major=data.get("major", ""),
        email=data["email"]
    )
    db.session.add(student)
    db.session.commit()
    return {
        "message": "Student added successfully",
        "id": student.id
    }, 201


# PUT: update an existing student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if not student:
        return {"error": "Student not found"}, 404

    data = request.json or {}
    student.name = data.get("name", student.name)
    student.major = data.get("major", student.major)
    student.email = data.get("email", student.email)

    db.session.commit()

    return {
        "message": "Student updated successfully",
        "id": student.id,
        "name": student.name,
        "major": student.major,
        "email": student.email
    }, 200


# DELETE: remove a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student is None:
        return {"error": "Student not found"}, 404

    housing = Housing.query.filter_by(student_id=id).first()
    if housing:
        db.session.delete(housing)

    db.session.delete(student)
    db.session.commit()
    return {"message": f"Student {id} removed successfully"}, 200


# -------------------------
# HOUSING ENDPOINTS
# -------------------------

# 1) Get student information to be verified (including housing)
# Route: GET /students/<id>/verify
@app.route('/students/<int:student_id>/verify')
def verify_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {"error": "Student not found"}, 404

    housing = Housing.query.filter_by(student_id=student_id).first()
    if housing:
        housing_status = housing.housing_status
    else:
        housing_status = None

    return {
        "id": student.id,
        "name": student.name,
        "major": student.major,
        "email": student.email,
        "housing_status": housing_status
    }, 200
    

# 2) Update housing status for a given student_id
# route: PUT /housing/1 with JSON: {"housing_status": "off-campus-verified"}
@app.route('/housing/<int:student_id>', methods=['PUT'])
def update_housing(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {"error": "Student not found"}, 404

    data = request.json or {}
    new_status = data.get("housing_status")
    if not new_status:
        return {"error": "Missing 'housing_status' in request body"}, 400

    housing = Housing.query.filter_by(student_id=student_id).first()
    if not housing:
        # For this solution, we return 404 if record doesn't exist
        return {"error": "Housing record not found for this student"}, 404

    housing.housing_status = new_status
    db.session.commit()

    return {
        "message": "Housing status updated successfully",
        "student_id": student_id,
        "housing_status": housing.housing_status
    }, 200


# 3) Add a new housing record
# Route: POST /housing with JSON: {"student_id": 1, "housing_status": "pending"}
@app.route('/housing', methods=['POST'])
def add_housing():
    data = request.json or {}

    # TODO: Get student id and housing status from input JSON
    # Use data.get()
    student_id = data.get("student_id") # Your get code will be here
    housing_status = data.get("housing_status") # Your get code will be here

    if student_id is None or housing_status is None:
        return {"error": "Missing 'student_id' or 'housing_status' in request body"}, 400

    # Check that student exists
    student = Student.query.get(student_id)
    if not student:
        return {"error": "Student does not exist"}, 400

    # Check that there is not already a housing record for this student
    existing = Housing.query.filter_by(student_id=student_id).first()
    if existing:
        return {"error": "Housing record already exists for this student"}, 400

    housing = Housing(student_id=student_id, housing_status=housing_status)
    db.session.add(housing)
    db.session.commit()

    return {
        "message": "Housing record created successfully",
        "id": housing.id,
        "student_id": housing.student_id,
        "housing_status": housing.housing_status
    }, 201


# 4) Delete a housing record
# Example: DELETE /housing/1  (where 1 is student_id)
@app.route('/housing/<int:student_id>', methods=['DELETE'])
def delete_housing(student_id):
    housing = Housing.query.filter_by(student_id=student_id).first()
    if housing is None:
        return {"error": "Housing record not found for this student"}, 404

    db.session.delete(housing)
    db.session.commit()
    return {
        "message": f"Housing record for student {student_id} deleted successfully"
    }, 200


if __name__ == '__main__':
    app.run(debug=True)
