import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    search_bar_id = (By.ID, "adsearch-input")
    search_option = (By.CLASS_NAME, "non-query-string")
    creatives = (By.CLASS_NAME, "er-creative-container")
    header_text = (By.XPATH, "//div[@class='creative-count']/span[@class='header-text']")
    load_more = (By.XPATH, "//a[@class='er-load-more']")

    def wait_for_element(self, element):
        wait = WebDriverWait(self.driver, 7).until(
            self.expected_conditions.presence_of_element_located((By.ID, element)))


    def enter_text_search_bar(self, creative):
        self.driver.find_element(*BasePage.search_bar_id).clear()
        self.driver.find_element(*BasePage.search_bar_id).send_keys(creative)
        time.sleep(1)
        options = self.driver.find_elements(*BasePage.search_option)
        for option in options:
            if option.text == creative:
                option.click()
                break

    def verify_the_creative(self):
        a = ActionChains(self.driver)
        while True:
            try:
                load_more = self.driver.find_element(*BasePage.load_more)
                a.move_to_element(load_more).click().perform()
                if load_more.is_displayed() == False:
                    break
            except TimeoutException:
                break
        creative_count = len(self.driver.find_elements(*BasePage.creatives))
        total_creatives = self.driver.find_element(*BasePage.header_text).text
        print(creative_count)
        print(total_creatives)
        return (creative_count, total_creatives)