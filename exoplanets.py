from flask import Flask, url_for
from flask import render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def index(name=None):
    name = data()
    print name
    return render_template('index.html', name=name)

def data():
    data = np.genfromtxt("/Users/angusr/Documents/websites/exoplanets/data.txt", dtype=str, delimiter=',', skip_header=2).T
#
    name = data[0]
    msini = data[1]
    a = data[2]
    period = data[3]
    ecc = data[4]
    omega = data[5]
    T0 = data[6]
    K = data[7]

    print name[0]

    return name[0]

#     return name[0]
#     return render_template('hello.html', name=name)

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

if __name__ == '__main__':
#     data()
#     raw_input('enter')
    app.run(debug=True)
