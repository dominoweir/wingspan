import os
import testForm
import testMaps
import testTime

# clear existing output files
try:
    os.remove("formActual.txt")
except OSError:
    pass

try:
    os.remove("mapsActual.txt")
except OSError:
    pass

try:
    os.remove("timeActual.txt")
except OSError:
    pass

# run form submission with testForm.py
testForm.run()
expected = open("formExpected.txt", 'r')
actual = open("formActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Form submission test failed")

# run form submission with testMaps.py
testMaps.run()
expected = open("mapsExpected.txt", 'r')
actual = open("mapsActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Maps test failed")

expected.close()
actual.close()

# run form submission with testTime.py
testTime.run()
expected = open("timeExpected.txt", 'r')
actual = open("timeActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Timing test failed")

expected.close()
actual.close()
