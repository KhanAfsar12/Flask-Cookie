from flask import *

app = Flask(__name__)

@app.route('/')
def customer1():
    res = make_response('<h1>Cookie is set</h1>')
    res.set_cookie('foo','bar')
    return res

if __name__=='__main__':
    app.run(debug=True)