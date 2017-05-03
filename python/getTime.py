import sys
from flask import Flask, jsonify, render_template, request
from getTravelTime import getTravelTime
import datetime
from getFlightStatus import getFlightTime
import time

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
    departAirport = parsed[9]

    # flight status API- get airport location and flight departure time
    # returns an array with flight object in first element and departure time in second element
    flightInfo = getFlightTime(flight, departAirport)

    # time calculation
    currentFlight = flightInfo[0]

    currentTime = time.time()
    timeBeforeFlight = int(flightInfo[1]) - currentTime

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
        return jsonify(result=timeBeforeLeave, start=address, end=departAirport,
                       departure=time.strftime('%H:%M:%S', time.localtime(currentFlight['filed_departuretime'])),
                       arrival=time.strftime('%H:%M:%S', time.localtime(currentFlight['estimatedarrivaltime'])),
                       destination=currentFlight['destination'])
