
# pytest file should have the format test_X.py or X_test.py
# and test methods/functions should start with keyword "test"

def testLogin():
    print("Login Successful")

def testLogout():
    print("Logout succesful")

def testCalculation():
    assert 2+2 == 4


# we cannot directly run this script, we need to run it through pytest.
