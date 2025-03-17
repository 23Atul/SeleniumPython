
# a test is meant to look at the reasult of a particular behaviour and make sure that result aligns with what you would expect.
# fixture:- we can think of a test being broken into four steps.

# 1. Arrange:- presteps required to do before doing actual testing or test case comes under Arrange 
# eg. tc is to test add to cart feature then arrange is launch website,loggin in, opening portal, searching iteam....

# 2. Act:- the process of doing what is mentioned in test comes under act 
# eg. tc is add item in cart then when we click on add to cart then this is called act.

# 3. Assert:- when test is performed then we need to verify whether that test has happended or not.
# eg. after clicking add to cart we need to verify whether item is added to cart or not ie verifying.

# 4. Cleanup:- once the tc have been verified we need to reset the state of application from where we can restart our new test case.
# eg. logging off from application, closing the browser.
#------------------------------------------------------------------------------------------------------------------------------------------------

import pytest

@pytest.fixture
def setUp():  # its an fixture setup/arrange ie things we need to do before any tc execution
    # now just printing for demo, in actual we write the selenium code to perform below activity.
    print("launch browser")
    print("login")
    print("browse products")

# this is called tear down as the script under yield will run only after the setup is run, 
# test case is run and then at last we run tear down.
    yield 
    print("Logoff")
    print("close Browser")

def testAddItemtoCart(setUp):  # we pass the setUp fn as an argument bcoz we want setUp to run before any other fn.
    print("Add item Successful")


def testRemoveItemfromCart(setUp):
    print("Remove item succesful")



#  run: --> pytest -s test_6fixture.py
# launch browser
# login
# browse products
# Add item Successful
# .launch browser
# login
# browse products
# Remove item succesful
# .Logoff
# close Browser
