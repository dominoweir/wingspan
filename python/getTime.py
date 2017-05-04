from flask import Flask, jsonify, render_template, request
from getTravelTime import getTravelTime
from getFlightStatus import getFlightInfo
from getFlightStatus import getFlightTime
import time
import cgi, cgitb

data= cgi.FieldStorage()
form = data["form"]

estimatedTime = 0
parsed = []

longString = str(form)
parsed = longString.split(',')

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

with open('data.json', 'w') as outfile:
    outfile.truncate()
    json.dumps({result=timeBeforeLeave, start=address, end=departAirport,
            departure=time.strftime('%H:%M:%S', time.localtime(currentFlight['filed_departuretime'])),
            arrival=time.strftime('%H:%M:%S', time.localtime(currentFlight['estimatedarrivaltime'])),
            destination=currentFlight['destination']}, outfile)
