import sys
sys.path.insert(0,"/Users/dominoweir/Documents/wingspan/python")
from getTime import getTotalTime

def run():
    results = open("timeActual.txt",'w')

    string1 = "q1,8141,q2,Star+Bar%2C+West+6th+Street%2C+Austin%2C+TX%2C+United+States,q3,early,q4,no"
    test1 = str(getTotalTime(string1))

    results.write(test1)
    results.close()
