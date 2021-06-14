import pytest
from selenium import webdriver


""" This is a fixture method that is going to be called and reused for every test method
it will setup the resources that we need to run all the tests"""
@pytest.fixture
def setup(request):

    driver = webdriver.Chrome(executable_path="driver/chromedriver")
    driver.get("https://moat.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    driver.close()