import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I willl execute in fixtureDemo method")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("Firefox", "Rahul"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
