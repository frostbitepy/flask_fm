from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#the app works with "flask run", but doesn't run me with "py app.py".
#don't know why, but i will leave it that way for the moment and find out later


app = Flask(__name__)

#the database works only if it is in the main folder; 
#even if i change the sqlalchemy config to 'sqlite:////instance/song_library.db' 
#the application doesn't recognize the database in the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'

#create an SQLAlchemy object named `db` and bind it to the app
db = SQLAlchemy(app)

#a simple initial greeting
@app.route('/')
@app.route('/index')
def greeting():
    return render_template('greeting.html')

# app name 
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

#uncomment the code below here when you are done creating database instance db and models
import routes

#if __name__ == '__main__':
#    app.run(debug=True)