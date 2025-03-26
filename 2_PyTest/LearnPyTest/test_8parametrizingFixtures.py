
# @pytest.mark.parametrize allows one to define multiple sets of arguments and those arguments 
# can be taken iteratevely and executed.

# eg. when we test the login functionality, we test for both +ve and -ve cases 
# ie. correct username correct password, correct username wrong password.... and so on.
# in this case writing tests again & again and passing these usename password in different steps
# may not be efficient way, so we use parametrization for efficiency.

# URL: --> https://docs.pytest.org/en/6.2.x/parametrize.html#parametrize-basics


# pytest enables test parametrization at several levels:

# 1. pytest.fixture() allows one to parametrize fixture functions.
# 2. @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class .
# 3. pytest_generate_tests allows one to define custom parametrization schemes or extensions.
#----------------------------------------------------------------------------------------------------------------------------------

# 1. pytest.fixture() allows one to parametrize fixture functions.

import pytest

@pytest.fixture(params=["a","b"])  # this function has 2 argument values 

def demo_fixture(request):
    print(request.param)


def testLogin(demo_fixture): # testlogin function will run for each value in argument. here 2 times a,b
    print("Login Succesful")


# pytest -v -s test_8parametrizingFixtures.py

# [a] launch browser
# login
# browse products
# a
# Login Succesful
# PASSEDLogoff
# close Browser

# [b] launch browser
# login
# browse products
# b
# Login Succesful
# PASSEDLogoff
# close Browser

# --------------------------------------------------------------------------------------------------------------------------------------------

# 2. @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class .

# import pytest


@pytest.mark.parametrize("a, b, res",[(2,6,8),(5,8,15),(5,10,15)])
def testAdd(a, b, res):
    assert a+b == res


# a = 5, b = 8, res = 15

# @pytest.mark.parametrize("a, b, res", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
# def testAdd(a, b, res):

# > assert a+b == res
# E assert (5 + 8) == 15

# test_8parametrizingFixtures.py: 61: AssertionError
# == == == == == == == == == == == == == == == == == == == = short test summary info == == == == == == == == == == == == == == == == == == == =
# FAILED test_8parametrizingFixtures.py: : testAdd[5-8-15] - assert (5 + 8) == 15
# == =================================== 1 failed, 2 passed in 0.04s =====================================