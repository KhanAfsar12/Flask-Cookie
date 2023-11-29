from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/')  
def home():
    res = make_response("session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response'] = 'Afsar'
    return res

@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response']
        return render_template('getSession.html', name=s)
    

if __name__=="__main__":
    app.run(debug=True)