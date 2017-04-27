import urllib
import json as simplejson
import googlemaps
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/get_time')
def getTotalTime():
    timeArray = []

    # example input: q1,3849657,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no
    longString = request.args.get('stringified', 0, type=str)
    parsed = longString.split(',')

    # break down input to individual variables
    flight = parsed[1]
    address = parsed[3]
    parsedAddress = address.replace('%2C',',')
    timing = parsed[5]
    kids = parsed[7]

    # flight status API- get airport location and flight departure time
    airport, flightTime = getAirlineInfo(flight)

    driveTime = getTravelTime(parsedAddress, airport) / 60;
    timeArray.append(driveTime)

    if(timing == 'early'):
        timeArray.append(30)
    else:
        timeArray.append(10)

    if(kids == 'yes'):
        for i in timeArray:
            timeArray[i] = timeArray[i] * 2

    timeArray.append(str(flightTime))

    simplejson.dumps(str(timeArray))
    print(str(timeArray))
    return jsonify(result=str(timeArray))
