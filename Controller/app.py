from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return {'name':'Afsar Khan'}

@app.route('/librarian')
def librarian():
    return {'Book':'Broken wings'}

@app.route('/poet')
def poet():
    return 'Jibran Khalil Jibran'

@app.route('/user/<name>')
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))
    
    if name == 'librarian':
        return redirect(url_for('librarian'))

if __name__ =='__main__':
    app.run(debug=True)