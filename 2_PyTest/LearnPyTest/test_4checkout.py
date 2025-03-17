import pytest
def testLogin():
    print("Login Successful")


def testLogout():
    print("Logout succesful")


@pytest.mark.regression  # tc for regression testing makred explained in test_5groupingTests.py
def testCalculation():
    assert 2+2 == 4
