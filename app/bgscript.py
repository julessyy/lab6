from app import app
from flask import Flask,render_template
#from flask.ext.script import Manager

app = Flask(__name__)

#manager = Manager(app)

@app.route('/')
def main():
     return 'Hello there!'

@app.route('/gender')
def gender():

   return render_template("schools.html") 

@app.route('/native_american')
def native_american():
    return render_template("indian.html")



	
