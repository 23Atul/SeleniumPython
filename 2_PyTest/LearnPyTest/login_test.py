
# pytest file should have the format test_X.py or X_test.py
# and test methods/functions should start with keyword "test"

def testLogin():
    print("Login Successful")

def testLogout():
    print("Logout succesful")

def testCalculation():
    assert 2+2 == 4
    # assert 2+2 == 6



# def testCalculation():

# > assert 2+2 == 6
# E assert (2 + 2) == 6

# login_test.py: 12: AssertionError
# == == == == == == == == == == == == == == == == == == == == == = short test summary info == == == == == == == == == == == == == == == == == == == == == ==
# FAILED login_test.py: : testCalculation - assert (2 + 2) == 6
# == == == == == == == == == == == == == == == == == == == == = 1 failed, 2 passed in 0.04s == == == == == == == == == == == == == == == == == == == == ==


# we cannot directly run this script, we need to run it through pytest.
