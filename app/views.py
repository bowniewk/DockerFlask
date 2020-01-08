from app import app

@app.route('/')
def home():
   return "hello world!"

@app.route('/welcome')
def welcome():
   return "hello good evening and welcome"