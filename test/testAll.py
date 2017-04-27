import os
import testForm
import testMaps

# clear existing output files
try:
    os.remove("formActual.txt")
except OSError:
    pass

try:
    os.remove("mapsActual.txt")
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


# run form submission with testForm.py
testMaps.run()
expected = open("mapsExpected.txt", 'r')
actual = open("mapsActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Maps test failed")

expected.close()
actual.close()
