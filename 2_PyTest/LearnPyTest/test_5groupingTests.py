
# grouping helops us to perform certain test on a group 
# -m MARKEXPR           Only run tests matching given mark expression. For example: -m 'mark1 and not mark2'.
# -m markExpression helps us to add any tag to particular test cases so that when it is required to run those tc with particular tag we can do it easily.

import pytest

def testLogin():
    print("Login Successful")


@pytest.mark.regression  # tc makred for regression testing (user defined)
def testLogout(): 
    print("Logout succesful")

@pytest.mark.skip    # tc marked for skipping while execution (pre defined keyword)
def testCalculation():
    assert 2+2 == 4
# 1 skipped
# test_5groupingTests.py::testCalculation SKIPPED (unconditional skip)                 [ 93%]



@pytest.mark.xfail   # tc written but functionality not implemented so it will give as expected failure.
def testfunctionality():
    assert 2+2 == 4
# 1 xpassed
# test_5groupingTests.py::testfunctionality XPASS                    [100%]

# if we do not mark the tc as xfail then it will show as failure and gives bad impression on our report,
# so instead of leaving tc unmaked we simply mark it with xfail.


# == == == == == == == == == == == == == == == == 3 passed, 12 deselected, 3 warnings in 0.03s == == == == == == == == == == == == == == == == =

# to run --> pytest -m sanity or pytest -m regression
