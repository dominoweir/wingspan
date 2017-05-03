import os
import testForm
import testMaps
import testTime

# clear existing output files
try:
    os.remove("results/formActual.txt")
    os.remove("results/mapsActual.txt")
    os.remove("results/timeActual.txt")
except OSError:
    pass

# run form submission with testForm.py
testForm.run()
expected = open("results/formExpected.txt", 'r')
actual = open("results/formActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Form submission test failed")

# run form submission with testMaps.py
testMaps.run()
expected = open("results/mapsExpected.txt", 'r')
actual = open("results/mapsActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Maps test failed")

expected.close()
actual.close()

# run form submission with testTime.py
testTime.run()
expected = open("results/timeExpected.txt", 'r')
actual = open("results/timeActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText):
    print("Timing test failed")

expected.close()
actual.close()
