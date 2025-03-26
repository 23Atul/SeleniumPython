
# this file was "test_7conftest.py" but renamed to "conftest.py" as conftest.py is its standard name and cant be changed

# conftest.py --> it is an configuration file which holds the methods or modules which are common to 
# all the test cases, so that we do not need to write the same code again and again.

# for eg.:--> almost in every test case we need to launch the browser open the link and login into the portal
# and after testing we need to logout the application, which is common among all the test cases.
# so instead of writing the setup and teardown again and again in every file we simply 
# define it in conftest.py and refer it when needed.




import pytest

# @pytest.fixture 
# lets assume that there are 100s of tc, then writing tc_setup as argument everywhere is not good idea
# so we write @pytest.fixture(autouse=True) then we no need to specify in argument, evry fille will auto use it.

@pytest.fixture(autouse=True)
def tc_setup():   # used in 3additems.py

    print("launch browser")
    print("login")
    print("browse products")
    yield
    print("Logoff")
    print("close Browser")


# we will use it like this
# def testLogin(tc_setup):  # eg. of conftest.py
#     print("Login Successful")



# Your test file test_items.py is using a fixture tc_setup, which is defined in test_conftest.py. 
# However, for PyTest to automatically detect and use this fixture, the fixture file should be 
# named conftest.py(not test_conftest.py).
# conftest.py is a special PyTest configuration file that automatically shares fixtures across test files.
# PyTest does not recognize files named test_conftest.py for global fixtures.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


# Fixture scopes
# Fixtures are created when first requested by a test, and are destroyed based on their scope:

# function: the default scope, the fixture is destroyed at the end of the test.
# class: the fixture is destroyed during teardown of the last test in the class .
# module: the fixture is destroyed during teardown of the last test in the module.
# package: the fixture is destroyed during teardown of the last test in the package.
# session: the fixture is destroyed at the end of the test session.

# @pytest.fixture(scope="session") 
