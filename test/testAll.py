import os

# run sign in with testSignIn.py
os.system("testSignIn.py")
expected = open("signInExpected.txt", 'r')
actual = open("signInActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText)
    print("Sign in test failed")

expected.close()
actual.close()

# run form submission with testForm.py
os.system("testForm.py")
expected = open("formExpected.txt", 'r')
actual = open("formActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText)
    print("Form submission test failed")

expected.close()
actual.close()

# run maps tests with testMaps.py
os.system("testMaps.py")
expected = open("mapsExpected.txt", 'r')
actual = open("mapsActual.txt",'r')

expectedText = expected.read()
actualText = actual.read()

if (expectedText != actualText)
    print("Map verification test failed")

expected.close()
actual.close()
