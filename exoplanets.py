from exoplanet_pictograms import plot_exoplanet, plot_name, remove_space
from flask import Flask, url_for
from flask import render_template
import numpy as np
import kplr
import csv
app = Flask(__name__)

@app.route('/')
def index(name=None, text=None):
    name = nm()
    print name
    text1 = p_text(name)
    text2 = d_text(name)
    text3 = price(name)
    return render_template('index.html', name=name, p_text=text1, d_text=text2, cut_name=remove_space(name), \
            dist = text3)

@app.route('/image/<name>')
def image(name):
    return plot_name(name)

def nm():
    data = np.genfromtxt("/users/angusr/python/exoplanet_travel/transit_data.txt", \
            dtype=str, delimiter=',', skip_header=2).t
    r = np.random.randint(0, len(data[0][0]))
    name = data[0]
    return name[r]

def p_text(name):
    data = np.genfromtxt("/Users/angusr/Python/exoplanet_travel/transit_data.txt", \
            dtype=str, delimiter=',', skip_header=2).T
    n = data[0]
    l = n == name
    periods = data[3]
    a = float(data[2][l][0])#/1.48e-11

    p = float(periods[l][0])
    print p
    if p < 20:
        tstar = 5000.
        albedo = .5
        rstar = 1.
        teq = int(600.)
#         teq = tstar*(1-albedo)**.25 * (rstar/(2*a))**.5
    if p < 20:
        r = np.random.randint(0,2)
        if r == 0:
            return "It's time to turn up the heat! With surface temperatures in excess of %s C, \
                    this planet is a scorcher"%teq
        elif r == 1:
            return "Love sunbathing? On this planet its so hot that even a moment of exposure will incinerate \
                    you. High factor Sun scream required."
        elif r == 2:
            return "Enjoy long summer evenings and 1000 degree days? You'll need to spend them all in a \
                    protective lead case, but they'll probably still be enjoyable."
    else:
        r = np.random.randint(0,1)
        if r == 0:
            return "This is a cool place to be - too cool in fact. At -100 degrees you'll need to \
                    take that extra layer for sure."
        else:
            return "Might want to pack an extra jumper."

def d_text(name):
    data = np.genfromtxt("/Users/angusr/Python/exoplanet_travel/transit_data.txt", \
            dtype=str, delimiter=',', skip_header=2).T
    n = data[0]
    l = n == name

    # find namez
    print data[0][l][0], 'name'
    mass = float(data[1][l][0])
    print mass
    print data[10][l]
    radius = 1.
    try:
        radius = float(data[10][l][0])
    except:
        pass
    print mass, radius
    d = mass/(4*radius)**3

    r = np.random.randint(0,1)
    # low g
    if d > .5:
        if r == 0:
            return "If things are getting a little 'heavy' back home, you'll feel lighter \
                    than air on this low-g planet"
        else:
            return "One of the big pulls for this destination is its gravitational field. At... Gs \
                    you'll come back feeling like Superman"

    # high g
    if d < .5:
        if r == 0:
            return "There are many attractions on this planet, but gravity isn't one of them. Its \
                    gravitational field is a mere 50 percent of the Earth's so you'll feel \
                    like you're floating the whole time"
        else:
            return "This is the perfect place to lose a few pounds. In fact you'll only weigh 0.1 Kg due to its \
                    low gravity"

def nm():
    data = np.genfromtxt("/Users/angusr/Python/exoplanet_travel/transit_data.txt", \
            dtype=str, delimiter=',', skip_header=2).T
    r = np.random.randint(0, len(data[0][0]))
    name = data[0]
    return name[r]

def price(name):
    distances = (500, 300, 100, 600, 1000, 10)
    # 12 litres per km
    # 2.82 dollars per gallon
    # 4.54 litres per gallon
    # .62 dollars per litre
    # 7.44 dollars per km
    # 4.3896 GBP per km
    # 1.317e+17 gbp per parsec
    r = np.random.randint(0, len(distances))
    cost = 1.317e+17 * distances[r]
#     stringy = str(cost)
#     z = str[-2:]
    r = np.random.randint(0,3)
    if r == 0:
        return "Only %s GBP!*" %cost
    elif r == 1:
        return "Special offer! %s GBP!*" %cost
    elif r == 2:
        return "%s GBP TODAY ONLY*" %cost
    elif r == 3:
        return "Only 2 seats left at %s GBP*" %cost

if __name__ == '__main__':
#     name = nm()
#     d_text(name)
#     raw_input('enter')
    app.run(debug=True)
