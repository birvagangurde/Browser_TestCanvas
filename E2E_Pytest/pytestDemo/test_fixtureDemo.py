# 77 Video ----------------------------------------------
import pytest


# Decorator: @pytest.fixture()
# Method name can be anything (setup is common).


# @pytest.fixture()
def setup():
    print("I will be executing first")  #setup code (runs before the test).
    yield   #→ separates setup and teardown in a single fixture.
    print("I willl execute in fixtureDemo method") #teardown code (runs after the test).

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")