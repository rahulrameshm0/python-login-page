from flask import Flask, request, render_template, flash, redirect, url_for
datas = {}

app = Flask(__name__)
app.secret_key = "mrahul"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm = request.form["confirm"]
        for user_data in datas.values():
            if user_data["username"] == username:
                flash("This is username is already taken!")
                return redirect(url_for("signup"))
            
        if password != confirm:
            flash("password does not match!","error")
            return redirect(url_for("signup"))
        
        datas[fname] = {
            "lname":lname,
            "email":email,
            "confirm":confirm,
            "password":password,
            "username":username
        }
        flash("Account created successfully!!", "success")
        return redirect(url_for("signup"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        for user in datas.values():
            if user["username"] == username and user["password"] == password:
                flash("login successful", "success")
                return redirect(url_for('home'))
         
        flash("username or password is incorrect!", "error")
        return redirect(url_for("login"))
    
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)