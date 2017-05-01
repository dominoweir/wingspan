import urllib
import sys
import json as simplejson
import googlemaps
from flask import Flask, jsonify, render_template, request
from getTravelTime import getTravelTime
from FlightInfo import getFlightInfo
import time
import datetime

app = Flask(__name__)


@app.route('/get_time')
def getTotalTime(longString=""):
    timeArray = []
    parsed = []
    isTesting = False

    # to call a method from this class, basically do flightInstance.run() or .call() etc. 


    # check for arguments
    if (longString != ""):
        parsed = longString.split(',')
        isTesting = True

    # example input: q1,3849657,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no
    else:
        longString = request.args.get('stringified', 0, type=str)
        parsed = longString.split(',')

    # break down input to individual variables
    flight = parsed[1]
    address = parsed[3]
    parsedAddress = address.replace('%2C', ',')
    timing = parsed[5]
    kids = parsed[7]

    # flight status API- get airport location and flight departure time

    FlightInfo = getFlightInfo(flight)

    now = datetime.datetime.now()

    currentTime = (now - datetime.datetime(1970, 1, 1)).total_seconds()

    timeBeforeFlight = FlightInfo.actualDepartureTime - currentTime

    #FlightInfo.orgin returns the ICOA code for the departure airport

    driveTime = getTravelTime(parsedAddress, FlightInfo.origin) / 60

    timeArray.append(driveTime)

    if (timing == 'early'):
        timeArray.append(40)
    else:
        timeArray.append(20)

    if (kids == 'yes'):
        for i in timeArray:
            timeArray[i] = timeArray[i] * 2

    for i in timeArray:

            estimatedTime = + timeArray[i]

    estimatedTime = int(estimatedTime)

    estimatedTime = estimatedTime*60

    timeBeforeLeave = timeBeforeFlight - estimatedTime

    returnArray = [timeBeforeLeave]

    print "%s" % (returnArray[i])

    if isTesting:
        return str(returnArray)
    else:
        simplejson.dumps(str(returnArray))
        return jsonify(result=str(returnArray))

