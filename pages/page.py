from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.basepage import BasePage


class Pages(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.basepage = BasePage(driver)

    page_type = (By.XPATH, "//span[@class='page-type']")
    hover_on = (By.XPATH, "//div[@class='er-creative-container'][1]")
    share = (By.LINK_TEXT, "Share")
    random_brand = (By.LINK_TEXT, "Random Brand")

    # This method verifies the search bar autocomplete drop down text
    def search_autocomplete(self):
        search_txt = "Saturn"
        self.basepage.enter_text_search_bar(search_txt)
        text1 = self.driver.find_element_by_xpath("//span[@class='page-type']").text
        print("text is", text1)
        assert self.driver.find_element(*Pages.page_type).text == "Saturn"

    # This method verifies the creatives count on the search results page is correct for search term: Saturn
    def verify_the_creative_count_saturn(self):
        search_txt = "Saturn"
        self.basepage.enter_text_search_bar(search_txt)
        creative_count, total_saturn = self.basepage.verify_the_creative()

        assert str(creative_count) not in total_saturn

    # This method verifies the creatives count on the search results page is correct for search term:Saturday's Market
    def verify_the_creative_count_Saturday(self):
        search_txt = "Saturday's Market"
        self.basepage.enter_text_search_bar(search_txt)
        creative_count, total_creatives = self.basepage.verify_the_creative()

        assert str(creative_count) in total_creatives

    # This method verifies the creatives count on the search results page is correct for search term: Krux
    def verify_the_creative_count_Krux(self):
        search_txt = "Krux"
        self.basepage.enter_text_search_bar(search_txt)
        creative_count, total_creatives = self.basepage.verify_the_creative()
        assert str(creative_count) in total_creatives

    # This method is verifying does share link appears when we hover over an creatives
    def verify_the_share_link(self):
        search_txt = "Saturn"
        self.basepage.enter_text_search_bar(search_txt)

        hover_to = self.driver.find_element(*Pages.hover_on)
        a = ActionChains(self.driver)
        a.move_to_element(hover_to).perform()
        share_link = self.driver.find_element(*Pages.share).text
        assert share_link == "Share"

    # This method is verifying whether the random brand link is random every time we click on it
    def verify_the_random_brand_link(self):
        search_txt = "Intuit"
        self.basepage.enter_text_search_bar(search_txt)

        header_text1 = self.driver.find_element_by_xpath("//div/span[@class='page-type']").text
        self.driver.find_element(*Pages.random_brand).click()
        header_text2 = self.driver.find_element_by_xpath("//div/span[@class='page-type']").text
        print(header_text1, header_text2)
        assert header_text1 is not header_text2
