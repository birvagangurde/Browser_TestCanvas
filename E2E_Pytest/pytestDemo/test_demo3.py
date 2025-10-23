# any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should make sense
# -k stands for method names execution, -s logs in out put -v stands for more information metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# fixtures are used as setup and tear down methods for test cases - conftest file to generalise
# fixture and make it available to all test cases

import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match "


@pytest.mark.xfail
def test_SecondCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
