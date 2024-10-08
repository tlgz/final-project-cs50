from flask import Flask, flash, redirect, render_template, request, session,url_for
import sqlite3
import requirements as req

db = sqlite3.connect('users.db')


app= Flask(__name__)

@app.route('/')
def main():
    

    return render_template("index.html")

@app.route('/apology')
def apology():
    
    result = request.args.get("result")
    return render_template("apology.html", result=result)

@app.route('/login')
def login():
    
    session.clear()

    if request.method == "POST":
            1==1


@app.route('/register', methods=['GET', 'POST'])
def register():
     
     if request.method == "POST":
        if not request.form.get("username"):
            return redirect(url_for('apology', result="Please insert username"))     
        if not request.form.get("password"):
            return redirect(url_for('apology', result="Please insert password"))  
        if not request.form.get("confirmation"):
            return redirect(url_for('apology', result="Please confirm password"))
        if request.form.get("confirmation")!=request.form.get("password"):
            return redirect(url_for('apology', result="Passwords doesn't match"))
        
        hash= req.hash_string(request.form.get("password"))
        print(hash)

        

     return render_template("register.html")





    
    








if __name__ == '__main__':
    app.run(debug=True)

