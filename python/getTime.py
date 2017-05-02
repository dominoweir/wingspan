import sys
from flask import Flask, jsonify, render_template, request
from getTravelTime import getTravelTime
import datetime
from getFlightStatus import getFlightInfo

app = Flask(__name__)

testString = "q1,8141,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no"


@app.route('/get_time')
def getTotalTime(longString=""):
    print(longString)
    estimatedTime = 0
    parsed = []
    isTesting = False

    # check for arguments
    if longString != "":
        parsed = longString.split(',')
        isTesting = True

    # example input: q1,3849657,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no
    else:
        longString = request.get('stringified', 0, type=str)
        parsed = longString.split(',')

    print(isTesting)
    print(parsed)

    # break down input to individual variables
    flight = parsed[1]
    address = parsed[3]
    parsedAddress = address.replace('%2C', ',')
    timing = parsed[5]
    kids = parsed[7]

    # flight status API- get airport location and flight departure time
    flightInfo = getFlightInfo(flight)
    print(flightInfo)
    now = datetime.datetime.now()
    currentTime = (now - datetime.datetime(1970, 1, 1)).total_seconds()
    timeBeforeFlight = flightInfo.actualDepartureTime - currentTime

    # FlightInfo.orgin returns the ICOA code for the departure airport
    driveTime = getTravelTime(parsedAddress, flightInfo.origin) / 60
    estimatedTime = driveTime

    if timing == 'early':
        estimatedTime += 40
    else:
        estimatedTime += 20

    if kids == 'yes':
        estimatedTime *= 1.5

    estimatedTime = estimatedTime * 60
    timeBeforeLeave = timeBeforeFlight - estimatedTime

    print(timeBeforeLeave)

    if isTesting:
        return str(timeBeforeLeave)
    else:
        return jsonify(result=timeBeforeLeave, start=address, end=FlightInfo.origin)
