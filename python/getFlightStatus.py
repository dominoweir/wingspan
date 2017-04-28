#!/usr/bin/env python
# import self as self
from SOAPpy import Config, HTTPTransport, SOAPAddress, WSDL

username = 'whitenicholas'
apiKey = 'abc123abc123abc123abc123abc123abc123'
wsdlFile = 'http://flightxml.flightaware.com/soap/FlightXML2'


# This is a custom HTTP transport that allows Basic Authentication.
class MyHTTPTransport(HTTPTransport):
    username = 'whitenicholas'
    passwd = 'serapio22'

    @classmethod
    def setAuthentication(cls, u, p):
        cls.username = u
        cls.passwd = p

    def call(self, addr, data, namespace, soapaction=None, encoding=None, http_proxy=None, config=Config, timeout=None):

        if not isinstance(addr, SOAPAddress):
            addr = SOAPAddress(addr, config)

        if self.username != None:
            addr.user = self.username + ":" + self.passwd

        return HTTPTransport.call(self, addr, data, namespace, soapaction, encoding, http_proxy, config)


    def run():
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
