import sys
from suds import null, WebFault
from suds.client import Client
import logging


username = 'whitenicholas'
apiKey = 'e0f7594a21220fb949e13146a8a0637fecf17e02'
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'


logging.basicConfig(level=logging.INFO)
api = Client(url, username=username, password=apiKey)
#print api

# Get the weather
result = api.service.Metar('KAUS')
print result

# Get the flights enroute
result = api.service.Enroute('KSMO', 10, '', 0)
flights = result['enroute']

print "Aircraft en route to KSMO:"
for flight in flights:
    print "%s (%s) \t%s (%s)" % ( flight['ident'], flight['aircrafttype'],
                                  flight['originName'], flight['origin'])