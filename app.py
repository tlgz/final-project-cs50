from flask import Flask, flash, redirect, render_template, request, session,url_for, session
import sqlite3
import requirements as req
from flask_session import Session
import requests
from config import OMDB_API_KEY,app_secret_key
from datetime import datetime


app = Flask(__name__, static_folder="./static")
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
    post_data= db_cursor.execute("Select posts.*,users.username from posts join users on posts.userid = users.id order by time DESC").fetchall()
    star_data= db_cursor.execute("select movietitle, AVG(stars),imageurl from posts Group by movietitle order by AVG(stars) desc limit 3").fetchall()
    
    
    

    
    

    return render_template("index.html", post_data=post_data ,star_data=star_data)


@app.route('/post', methods=['GET', 'POST'])
def post(): 
    if session.get("user_id") is None:
            return redirect("/login")
    
    


    if request.method == "POST":
        if not request.form.get("moviename"):
            return redirect(url_for('apology', result="Please insert Movie name")) 
        movie_name = request.form.get("moviename")
        
        pyynti = requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}")
        
        if pyynti.status_code == 200:
            data = pyynti.json()
            if data.get('Response') == 'False':
                return redirect(url_for('apology', result="Movie not found"))
            movietitle=data["Title"]
            imageurl=data["Poster"]
            



        return render_template("post.html",movietitle=movietitle,imageurl=imageurl)
        



    return render_template("post.html")


@app.route('/posted', methods=['GET', 'POST'])
def posted(): 
    if session.get("user_id") is None:
            return redirect("/login")
    
    if request.method == "POST":
        1==1
        time = datetime.now()
        if not request.form.get("reviewtext"):
            return redirect(url_for('apology', result="Please enter review text"))
        if not request.form.get("selectedStars"):
             return redirect(url_for('apology', result="Please enter stars amount"))
    db_cursor.execute("INSERT INTO posts (userid,movietitle,imageurl,stars,review,time) VALUES (?,?,?,?,?,?)", \
    ((session["user_id"]),request.form.get("movietitle"),request.form.get("imageurl"),request.form.get("selectedStars"),request.form.get("reviewtext"),time))
    db.commit()
             
    return redirect("/")     

@app.route('/remove',methods=['POST'])
def remove():
        
        if session.get("user_id") is None:
            return redirect("/login")
        if int(session.get("user_id"))!=int(request.form.get("userid")):
              return redirect(url_for('apology', result="Häkkeri älä yritä"))
        db_cursor.execute("delete from posts where time=? and userid =? and movietitle =?",(request.form.get("time"),request.form.get("userid"),request.form.get("movie")))
    
        return redirect("/")



@app.route('/login', methods=['GET', 'POST'])
def login(): 

    if request.method == "POST":
        print(request.form.get("username"))
        if not request.form.get("username"):
            return redirect(url_for('apology', result="Please insert username"))     
        if not request.form.get("password"):
            return redirect(url_for('apology', result="Please insert password"))   
        
        user_details= db_cursor.execute("select * from users where username = ?",(request.form.get("username"),)).fetchall()
        if not user_details:
            return redirect(url_for('apology', result="User not found")) 
        hash_value= req.hash_string(request.form.get("password"))
        
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
    if session.get("user_id") is None:
            return redirect("/login")
    session["user_id"] = None
    return redirect("/")


    
    
@app.route('/apology')
def apology():
   
    
    result = request.args.get("result")
    return render_template("apology.html", result=result)







if __name__ == '__main__':
    
    
    app.secret_key = app_secret_key
    app.run(debug=True)

