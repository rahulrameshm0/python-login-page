from flask import Flask, request, render_template
datas = {}

app = Flask(__name__)
app.secret_key = "mrahul"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = None
        datas[request.form["fname"]] = {
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm": request.form["confirm"]
        }
        password = request.form["password"]
        confirm = request.form["confirm"]
        if password != confirm:
            name = "Your password does not match"
            return render_template("signup.html", name = name)
      
    return render_template("signup.html", success = "Account Created Successfully!")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        error = None
        fname = request.form['fname']
        password = request.form['password']
        if fname not in datas or datas[fname]["password"] != password:
            error = "Wrong username or password"
            return render_template('login.html', error = error)
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)