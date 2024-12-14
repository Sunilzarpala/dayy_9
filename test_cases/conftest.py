import pytest
from selenium import webdriver



@pytest.fixture()
def setup():
    driver=webdriver.Firefox()
    driver.maximize_window()
    return driver


def pytest_metadata(metadata):
    metadata['class'] = 'Sunil'
    metadata['batch'] = 'ct15'
    metadata['device'] = 'hp'

@pytest.fixture(params=[
    ("Credencetest@test.com" , "Credence@123"),
    ("Credencetest@test.com" , "Credence@1223"),
    ("Credencetest@test.cmmm" , "Credence@123"),
    ("Credencetest@test.coom" , "Credence@1o23")
])
def getDataForLogin(request):
    return request.param