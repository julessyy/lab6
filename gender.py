
from flask import Flask,render_template
#import simplejson 


app = Flask(__name__)

@app.route('/')
def greetings():
     return 'Hello there!'

@app.route('/gender')
def gender():

   return render_template("schools.html") 

@app.route('/native_american')
def native_american():
    return render_template("indian.html")

if __name__ == '__main__':
    app.run(debug=True)

	
