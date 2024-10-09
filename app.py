from flask import Flask, flash, redirect, render_template, request, session,url_for, session
import sqlite3
import requirements as req
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

db = sqlite3.connect('users.db',check_same_thread=False)
db_cursor = db.cursor()


app= Flask(__name__)

@app.route('/')
def main():
    if session.get("user_id") is None:
            return redirect("/login")

    
    

    return render_template("index.html")

@app.route('/apology')
def apology():
    
    result = request.args.get("result")
    return render_template("apology.html", result=result)

@app.route('/login', methods=['GET', 'POST'])
def login(): 

    if request.method == "POST":
        if not request.form.get("username"):
            return redirect(url_for('apology', result="Please insert username"))     
        if not request.form.get("password"):
            return redirect(url_for('apology', result="Please insert password"))   
        
        user_details= db_cursor.execute("select * from users where username = ?",(request.form.get("username"),)).fetchall()
        if not user_details:
            return redirect(url_for('apology', result="User not found")) 
        hash_value= req.hash_string(request.form.get("password"))
        print(user_details)
        if user_details[0][2]!=hash_value:
            return redirect(url_for('apology', result="incorrect password")) 
        rows = db_cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),)).fetchall()
        session["user_id"]= rows[0][0]
        return redirect(url_for('main'))
        

    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
     
     if request.method == "POST":
        if not request.form.get("username"):
            return redirect(url_for('apology', result="Please insert username"))  
        if db_cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),)).fetchall():
            return redirect(url_for('apology', result="Username already taken")) 
        if not request.form.get("password"):
            return redirect(url_for('apology', result="Please insert password"))  
        if not request.form.get("confirmation"):
            return redirect(url_for('apology', result="Please confirm password"))
        if request.form.get("confirmation")!=request.form.get("password"):
            return redirect(url_for('apology', result="Passwords doesn't match"))
        hash_value= req.hash_string(request.form.get("password"))
        db_cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?)",(request.form.get("username"),hash_value))
        db.commit()
        
        rows = db_cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"),)).fetchall()
        print(rows[0][0])
        session["user_id"]= rows[0][0]
        return redirect(url_for('main'))
        

     return render_template("register.html")


@app.route("/logout")
def logout():
    session["user_id"] = None
    return redirect("/")


    
    








if __name__ == '__main__':
    app.secret_key = 'jlkkklTestkey'
    app.run(debug=True)

