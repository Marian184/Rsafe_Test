import time
from locators.locators  import Locators

class Homepage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.search_link_id  = Locators.search_link_id
        #self.logout_link_id  = 'Logout'
        #driver.find_element_by_xpath( '//*//*[@id="oneHeader"]/div[3]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[1]/a/span"]').click()
        # driver.find_element_by_link_text("Home").click() #Hay dos valores con ese texto

    def click_welcome(self):
        driver.find_element_by_xpath(self.welcome_link_id).click()
        # driver.find_element_by_link_text("Home").click() #Hay dos valores con ese texto
        time.sleep(5)

    def search_VIN(self,VIN):
        driver.find_element_by_xpath(self.search_link_id).send_keys(VIN)

    def click_enter(self):
        driver.find_element_by_xpath(self.search_link_id).send_keys(Keys.ENTER)

