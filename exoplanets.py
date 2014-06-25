from flask import Flask, url_for
from flask import render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def index(name=None, text=None):
    name = data()
    print name
    text = 'This planet is hot!'
    return render_template('index.html', name=name, text=text)

def data():
    data = np.genfromtxt("/Users/angusr/Documents/websites/exoplanets/data.txt", dtype=str, delimiter=',', skip_header=2).T

    name = data[0]
    msini = data[1]
    a = data[2]
    period = data[3]
    ecc = data[4]
    omega = data[5]
    T0 = data[6]
    K = data[7]

    return name[0]

def text():
    data = np.genfromtxt("/Users/angusr/Documents/websites/exoplanets/data.txt", dtype=str, delimiter=',', skip_header=2).T

    name = data[0]
    msini = data[1]
    a = data[2]
    period = data[3]
    ecc = data[4]
    omega = data[5]
    T0 = data[6]
    K = data[7]

    return text

if __name__ == '__main__':
    app.run(debug=True)
