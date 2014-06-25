import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse
import matplotlib.image as mpimg
import StringIO
import numpy as np
import csv

# Each exoplanet has a transit depth, which is (radius of planet/ radius of star )^2
# eg depth = 0.01
# rp/rstar = 0.1
# They also have absolute radii for the planet (and therefore we can calc the absolute radius of the star)
# eg radius = 1 Jupiter, depth = .01, stellar radius = 10 Jupiters
# They also all have orbital periods and semi-major axes.
# Eg:
# NAME,MSINI,A,PER,TT,K,B,DEPTH,I,R,DENSITY,

# In units mjupiter,au,day,,deg,jd,m/s
# WASP-14 b,7.65457,0.0367693,2.243752,2454463.57583,993,0.535,0.0102,84.32,1.281
# Kepler-20 b,0.0266149,0.0453704,3.6961219,0,79.2157,2454966.34,3.72
# HD 4308 b,0.0477376,0.119192,15.56,0,359,2453314.7,4.07

RSUN_IN_AU = 0.00464913034

def load_data():
    data=csv.DictReader(open("pictogram_input_data.csv"))
    return list(data)


def rgb_from_jhk(J, H, K):
    g = 0.5
    r = J / (H/g)
    b = K / (H/g)
    color = (r,g,b)
    return color

def plot_data(name, semimajor, planet_radius, star_radius, star_color):
    center = np.array([0.5,0.5])
    angle = np.random.uniform(0, 2*np.pi)
    planet_center = center+semimajor*np.array([np.cos(angle), np.sin(angle)])
    # planet_radius = transit_depth**0.5 * star_radius

    fig = Figure(figsize=(6,6))
    axis = fig.add_subplot(1, 1, 1)
    print star_color
    star = Circle(center, radius=star_radius, color=star_color)
    orbit = Circle(center, radius=semimajor, fill=False, linestyle='dashed', color='gray')
    planet = Circle(planet_center, radius=planet_radius, color='green')

    axis.add_patch(star)
    axis.add_patch(orbit)
    axis.add_patch(planet)
    axis.axis('off')

    canvas = FigureCanvas(fig)
    fig.savefig("images/"+name.replace(" ", "_"))

def plot_exoplanet(planet):
    print planet['NAME']
    semimajor = float(planet["A"])
    try:
        period = float(planet["PER"])
    except ValueError:
        period = 0.0
    try:
        eccentricity = float(planet["ECC"])
    except ValueError:
        eccentricity = 0.0
    star_radius = float(planet["RSTAR"]) * RSUN_IN_AU
    transit_depth = float(planet["DEPTH"])
    planet_radius = star_radius * transit_depth**0.5
    name = planet["NAME"]
    J = np.exp(float(planet["J"]))
    H = np.exp(float(planet["H"]))
    K = np.exp(float(planet["KS"]))
    color = rgb_from_jhk(J, H, K)
    plot_data(name, semimajor, planet_radius, star_radius*4, color)




def make_plot():
    from flask import make_response
    data = plot_data()
    response = make_response(data.getvalue())
    response.mimetype = 'image/png'
    return response

if __name__ == '__main__':
    planets=load_data()
    for p in planets[5:]:
        try:
            plot_exoplanet(p)
        except Exception as e:
            # raise
            print e
            continue
