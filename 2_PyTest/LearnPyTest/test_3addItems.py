
import pytest

def testLogin(tc_setup): # eg. of conftest.py
    print("Login Successful")


def testLogout():
    print("Logout succesful")


def testCalculation():
    assert 2+2 == 4


# launch browser
# login
# browse products
# Login Successful
# .Logoff
# close Browser
# Logout succesful
