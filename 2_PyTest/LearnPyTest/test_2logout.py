import pytest

def testLogin():
    print("Login Successful")


# tc for regression testing makred explained in test_5groupingTests.py
@pytest.mark.regression
def testLogout():
    print("Logout succesful")


def testCalculation():
    assert 2+2 == 4
