import time
import pytest_html

from pages.page import Pages


class TestMoats:

    # This test method verifies the search bar autocomplete drop down text
    def test_verify_search_bar_autocomplete(self, setup):
        page = Pages(self.driver)
        page.search_autocomplete()

    # This test method verifies the creatives count on the search results page is correct for search term: Saturn
    def test_verify_the_creative_saturn(self, setup):
        page = Pages(self.driver)
        page.verify_the_creative_count_saturn()

    # This test method verifies the creatives count on the search results page is correct for search term:Saturday's Market
    def test_verify_the_creative_saturday(self, setup):
        page = Pages(self.driver)
        page.verify_the_creative_count_Saturday()

    # This test method verifies the creatives count on the search results page is correct for search term: Krux
    def test_verify_the_creative_krux(self, setup):
        page = Pages(self.driver)
        page.verify_the_creative_count_Krux()

    # This test method is verifying does share link appears when we hover over an creatives
    def test_verify_the_share_link(self, setup):
        page = Pages(self.driver)
        page.verify_the_share_link()

    # This test method is verifying whether the random brand link is random every time we click on it
    def test_random_text_link(self, setup):
        page = Pages(self.driver)
        page.verify_the_random_brand_link()
        time.sleep(1)
