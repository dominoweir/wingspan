import logging
import time
import datetime
from suds.client import Client

username = 'whitenicholas'
apiKey = 'e0f7594a21220fb949e13146a8a0637fecf17e02'
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

logging.basicConfig(level=logging.INFO)
api = Client(url, username=username, password=apiKey)

# Get the weather
result = api.service.Metar('KAUS')
print result

# Get the flights enroute
result = api.service.Enroute('KAUS', 10, '', 0)
flights = result['enroute']

print "Aircraft en route to KAUS:"

# flightInfo = api.service.FlightInfoEx()


# testing for api

flightInfo = api.service.FlightInfoEx('FDX741', 10, 0)

print "%s" % flightInfo['flights'][0]['origin']
# print testing
returnedFlight = flightInfo['flights']

validFlights = []

for valid in returnedFlight:
    flightTime = valid['filed_departuretime']
    currentStamp = time.strftime('%m-%d', time.localtime(flightTime))
    validTime = time.strftime('%m-%d', time.localtime(time.time()))
    if currentStamp == validTime:
        if valid['origin'] == 'KMEM':
            returnTime = flightTime
            print "%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(returnTime))
            print "%s" % valid['origin']

for flight in returnedFlight:
    if flight['origin'] == 'KMEM':
        flightTime = flight['filed_departuretime']
        print "%s" % flight['filed_departuretime']
        print "%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(flightTime))

for flight in flights:
    print "%s (%s) \t%s (%s)" % (flight['ident'], flight['aircrafttype'],
                                 flight['originName'], flight['origin'])


# end of print testing






def getFlightTime(flightNumber, departAirport):

    returnArray = []

    flightNotice = api.service.FlightInfoEx(str(flightNumber), 1, 0)

    currentPlans = flightNotice['flights']

    for validPlans in currentPlans:
        timing = validPlans['filed_departuretime']
        currentTiming = time.strftime('%m-%d', time.localtime(timing))
        validTiming = time.strftime('%m-%d', time.localtime(time.time()))
        if currentTiming == validTiming:
            if validPlans['origin'] == str(departAirport):
                returnArray.append(validPlans)
                returnArray.append(timing)

    return returnArray
