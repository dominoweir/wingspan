import logging

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

flightInfo = api.service.FlightInfoEx('SWA1745', 1, 0)

#print testing
returnedFlight = flightInfo['flights']

for flight in returnedFlight:
    print "%s" % flight['filed_departuretime']


for flight in flights:
    print "%s (%s) \t%s (%s)" % (flight['ident'], flight['aircrafttype'],
                                 flight['originName'], flight['origin'])
#end of print testing

def getFlightInfo(flightNumber):
    # type: (object) -> object
    flightInfo = api.service.FlightInfoEx(flightNumber, 1, 0)
    return flightInfo
