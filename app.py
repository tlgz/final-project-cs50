from flask import Flask, flash, redirect, render_template, request, session
import sqlite3




app= Flask(__name__)

@app.route('/')
def main():
    

    return render_template("index.html")


@app.route('/login')
def login():
    
    session.clear()

    if request.method == "POST":
            1==1


@app.route('/register')
def register():
     
     if request.method == "POST":
          if not request.form.get("username"):
               


     return render_template("register.html")



    
    








if __name__ == '__main__':
    app.run(debug=True)

