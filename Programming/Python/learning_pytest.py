
#EXAMPLE 1
#grading.py

def get_average(results):
    # Make sure there are results in the list to prevent divide by zero errors
    if len(results) != 0:
        sum = 0             # holds the sum of the course results
        average = 0         # the calculated average of the results
 
        # Get total sum of all results
        for result in results:
            sum = sum + result
 
        average = sum / len(results)
        return average
 
# Returns the grade based on their mark
def get_grade(average):
    grade = 'N' # 0- 50
    if average > 80: # 81-100
        grade = 'A'
    elif average > 70: # 71 - 80
        grade = 'B'
    elif average > 60: # 61 - 70
        grade = 'C'
    elif average > 50: # 51 - 60
        grade = 'D'
 
    return grade
 
# Returns true if they receive a passing grade
def is_passing(avg):
    if avg > 49:
        return True
    else:
        return False



#EXAMPLE 1
# test_grading.py

# Import pytest in your testing files
import pytest

# We import our own file here, you do not need to add the .py
import grading

def test_getaverage():
    # Create a list of numbers to experiment with
    R = [10, 20, 30, -40]
    assert grading.get_average(R) == 5.0
    R = [7, 3, 304, 34]
    assert grading.get_average(R) == 87.0
    R = [-10, -5, -20, -5, -1]
    assert grading.get_average(R) == -8.2
    R = [2, 2, 2, 2, 2, 2, 2, 1, 3]
    assert grading.get_average(R) == 2.0

test_getaverage()
