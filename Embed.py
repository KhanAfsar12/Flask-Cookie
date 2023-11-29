from flask import Flask, render_template

app = Flask(__name__)

@app.route('/table/<int:num>')
def message(num):
    return render_template('messege.html')

if __name__ =='__main__':
    app.run(debug=True)