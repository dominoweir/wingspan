import collections
from getFlightStatus import getFlightInfo


def getFlightInfo(flightNumber):

    flightInfo = getFlightInfo(flightNumber)

    return flightInfo

    flightTime = flightInfo.actualDepartureTime

    departureAirport = flightInfo.origin
