from flask import Flask

app = Flask(__name__)

@app.route('/excel')
def enter():
    return "<html><body><h1>Welcome to the Afsar show</h1></body></html>"

if __name__  == '__main__':
    app.run(debug=True)