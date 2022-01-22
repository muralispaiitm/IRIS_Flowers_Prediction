from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def Predict_Val():
    data1 = request.form['a']  # a=5.1
    data2 = request.form['b']  # b=2.2
    data3 = request.form['c']  # c=1.4
    data4 = request.form['d']  # d=0.2
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('result.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True, port=5002)















