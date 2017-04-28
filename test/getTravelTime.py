import urllib
import json as simplejson
import googlemaps
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

gmaps = googlemaps.Client('AIzaSyByNrotEcmJr9KlyPK8qQqxyxrt9_2RH9Y')

def getTravelTime(address, airport):
    # geocode start address
    orig_coord = address

    #geocode airport address
    dest_coord = airport

    # request directions from google maps api and retrieve driving time
    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(orig_coord, dest_coord)
    result = simplejson.load(urllib.urlopen(url))

    # dig through json formatting to get actual duration
    driveTime = result['rows'][0]['elements'][0]['duration']['value']
    return driveTime
