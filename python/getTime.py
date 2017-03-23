import sys
import urllib
import json as simplejson
import googlemaps
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

gmaps = googlemaps.Client('AIzaSyByNrotEcmJr9KlyPK8qQqxyxrt9_2RH9Y')

def getTravelTime(address):
    # geocode start address
    orig_coord = address

    #geocode airport address
    dest_coord = 'Austin-Bergstrom International Airport, Presidential Boulevard, Austin, TX'

    # request directions from google maps api and retrieve driving time
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(orig_coord, dest_coord)
    result= simplejson.load(urllib.urlopen(url))

    # dig through json formatting to get actual duration
    driveTime = result['rows'][0]['elements'][0]['duration']['value']
    return driveTime

@app.route('/get_time')
def getTotalTime():
    # example input: q1,3849657,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no
    longString = request.args.get('stringified', 0, type=str)
    parsed = longString.split(',')

    # break down input to individual variables
    flight = parsed[1]
    address = parsed[3]
    parsedAddress = address.replace('%2C',',')
    timing = parsed[5]
    kids = parsed[7]

    driveTime = getTravelTime(parsedAddress) / 60;

    simplejson.dumps(driveTime)

    return jsonify(result=driveTime)
