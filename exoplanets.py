from flask import Flask, url_for
from flask import render_template
import numpy as np
app = Flask(__name__)

@app.route('/')
def index(name=None, text=None):
    name = nm()
    print name
    text = p_text(name)
    return render_template('index.html', name=name, text=text)

def nm():
    data = np.genfromtxt("/Users/angusr/Python/exoplanet_travel/transit_data.txt", dtype=str, delimiter=',', skip_header=2).T
    name = data[0]
    return name[0]

def p_text(name):
    data = np.genfromtxt("/Users/angusr/Python/exoplanet_travel/transit_data.txt", dtype=str, delimiter=',', skip_header=2).T
    n = data[0]
    periods = data[3]

    # find namez
    l = n == name
    p = float(periods[l][0])
    print p
    if p < 5:
        return "Better pack your spf 50 - this planet gets hot!"
    else:
        return "Might want to pack an extra jumper."

if __name__ == '__main__':
    app.run(debug=True)
