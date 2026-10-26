from flask import Flask, render_template, request

app = Flask(__name__)

students = []


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Registration page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        age_text = request.form.get("age", "").strip()

        if not name or not email or not age_text:
            return render_template(
                "result.html",
                success=False,
                message="Please fill in all fields."
            )

        if "@" not in email or "." not in email.split("@")[-1]:
            return render_template(
                "result.html",
                success=False,
                message="Please enter a valid email."
            )

        try:
            age = int(age_text)
        except ValueError:
            return render_template(
                "result.html",
                success=False,
                message="Age must be a number."
            )

        if age < 1 or age > 120:
            return render_template(
                "result.html",
                success=False,
                message="Age must be between 1 and 120."
            )

        student = {
            "name": name,
            "email": email,
            "age": age
        }

        students.append(student)

        return render_template(
            "result.html",
            success=True,
            student=student,
            message="Registration Successful!"
        )

    return render_template("index.html")


# View registered students
@app.route("/students")
def view_students():
    return render_template(
        "result.html",
        success=True,
        message="Registered Students",
        students=students
    )


if __name__ == "__main__":
    app.run(debug=True)