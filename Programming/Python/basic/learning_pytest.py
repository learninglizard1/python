
#how it works
def test_<name of function to test>():

# 1. code to setup the arguments to the function
# - test data
# - mocks
# - connection to database
# - network connections
# - etc.

# 2. The actual test of the function using the test data
assert <module name>.<function to test>(<test data)) = = <expected result>

# 3. The test teardown
# - close database or network connections
# - release any memory used
# - remove any objects create
# - remove any mocks
# - etc.




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





#GROUPING TESTS
#The xfail test will still run but will not display any results. 
#The skip test will be completely skipped and not run at all.

import pytest
import grading

# Using a marker
@pytest.mark.get_average
def test_average1():
    # Simple example list
    # Sum is 210
    # The average should be 35
    R = [10,20,30,40,50,60]
    assert grading.get_average(R) == 35

# No marker used
def test_average2():
    # Only one value, the result should be 50
    R = [50]
    assert grading.get_average(R) == 50

@pytest.mark.xfail(reason= "This test will run but not be part of the results")
def test_average3():
    R = [10,20,30,40]
    assert grading.get_average(R) == 25

@pytest.mark.skip(reason= "This test isn't needed right now")
def test_average4():
    R = [10,20,30,110]
    assert grading.get_average(R) == 42.5






#TEST EXCEMPTIONS
# test_grading.py

import pytest
import grading

# An example of checking for a specific exception
def test_exceptions():
    R = []      # In our code, we made it so if the list is empty it won't run
                # But if someone edited the code later and removed this
                # We would see this test fail, which alerts us something has gone wrong

    # Here we can use provide the exception
    with pytest.raises(ZeroDivisionError):
        grading.get_average(R)