import numpy
import scipy
import sys
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyByNrotEcmJr9KlyPK8qQqxyxrt9_2RH9Y')

# arg 0 will always be script name
unparsed = sys.argv[1]

# example input: q1=wo546738&q2=2707+Rio+Grande+Street%2C+Austin%2C+TX%2C+United+States&q3=early&q4=no
unparsed.replace('&','=')
responses = unparsed.split('=')
flightnum = responses[1]
address = responses[3].replace('+',' ')
address.replace('%2C',',')
early = responses[5]
kids = responses[7]

getTravelTime(address)

def getTravelTime(address):
    # geocode start address
    geocode_start = gmaps.geocode(address)

    now = datetime.now()
    directions = gmaps.directions("Sydney Town Hall", "Parramatta, NSW", departure_time=now)

    f = open('workfile', 'w')
    f.write(directions)
    f.close()
