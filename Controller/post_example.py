from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      username=request.form['username']  
      passwrd=request.form['pass']  
      if username=="ayush" and passwrd=="google":  
          return "Welcome %s" %username  
   
if __name__ == '__main__':  
   app.run(debug = True)  