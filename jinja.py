from flask import Flask,render_template

app = Flask(__name__)

@app.route('/user/<uname>')
def demo(uname):
    return render_template('jinja2.html', name=uname)

if __name__ == '__main__':
    app.run(debug=True)