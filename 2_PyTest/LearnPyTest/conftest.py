
# conftest.py --> it is an configuration file which holds the methods or modules which are common to 
# all the test cases, so that we do not need to write the same code again and again.

# for eg.:--> almost in every test case we need to launch the browser open the link and login into the portal
# and after testing we need to logout the application, which is common among all the test cases.
# so instead of writing the setup and teardown again and again in every file we simply 
# define it in conftest.py and refer it when needed.




import pytest

@pytest.fixture 
def tc_setup():   # used in 3additems.py

    print("launch browser")
    print("login")
    print("browse products")
    yield
    print("Logoff")
    print("close Browser")





# Your test file test_items.py is using a fixture tc_setup, which is defined in test_conftest.py. 
# However, for PyTest to automatically detect and use this fixture, the fixture file should be 
# named conftest.py(not test_conftest.py).

# conftest.py is a special PyTest configuration file that automatically shares fixtures across test files.
# PyTest does not recognize files named test_conftest.py for global fixtures.
