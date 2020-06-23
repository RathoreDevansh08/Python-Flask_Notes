'''
Make sure to not call your application flask.py because this would conflict with Flask itself.
'''

from flask import Flask, render_template
#from wtf.app import app

#First we imported the Flask class. An instance of this class will be our WSGI application.

# referencing this file
app = Flask(__name__)
'''
If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as
application or imported as module the name will be different ('__main__' versus the actual import name). This is needed
so that Flask knows where to look for templates, static files, and so on.
'''

# creating index route
@app.route('/')
def index():   #function for this route
    return "Hello DSR!" #prints this message

@app.route('/git')
def hello():
    #return "It\'s my git"
    return render_template('index.html') #routes to the html page in /templates/index.html

if __name__ == "__main__":
    # debug=True : for giving out errors if any
    app.run(debug=True)
