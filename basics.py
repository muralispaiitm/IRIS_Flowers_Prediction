from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hme')
def hme():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)


