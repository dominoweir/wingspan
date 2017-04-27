import sys
import urllib
import googlemaps
sys.path.insert(0,"/Users/dominoweir/Documents/wingspan/python")
from getTravelTime import getTravelTime

def run():
    results = open("mapsActual.txt",'w')

    startAddress = "Star Bar West 6th Street Austin TX United States"
    endAddress = "Austin Bergstrom International Airport"
    ambiguousAddress = "University of Texas"

    test1 = str(getTravelTime(startAddress, endAddress))

    if any(char.isdigit() for char in test1):
        results.write("Test 1 passed.\n")
    else:
        results.write("Test 1 failed, result was: " + str(test1)+"\n")

    test2 = str(getTravelTime(endAddress, endAddress))

    if any(char.isdigit() for char in test2):
        results.write("Test 2 passed.\n")
    else:
        results.write("Test 2 failed, result was: " + str(test2)+"\n")

    test3 = str(getTravelTime(ambiguousAddress, endAddress))

    if any(char.isdigit() for char in test3):
        results.write("Test 3 passed.\n")
    else:
        results.write("Test 3 failed, result was: " + str(test3))
