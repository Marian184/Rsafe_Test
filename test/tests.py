import time
from selenium import webdriver
import unittest
from config.homepage import Homepage
from config.loginpage import LoginPage
from config.save_excel import Save_Excel
import htmltestrunner


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Programacion\Python\Web_Drivers\geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        homepage = Homepage(driver)
        save_xls = Save_Excel(driver)

        driver.get("https://vwg2-vwgroup--qa.cs87.my.salesforce.com/")

        login.username_textbox_id("user@rsafe.com.qa") #username
        login.password_textbox_id("Password") #password
        login.click_login()
        codigo = input('Write the code \n')
        login.verify_code_id(codigo)



        for test in range(1,400):
            try:
                homepage.click_welcome()
                homepage.search_VIN('VSSPVSKL7LR000014')
                save_xls.general_screenshot()
                save_xls.cut_image()
                save_xls.save_image_xls(test)
            except:
                print("The test {} fails").format(test)
                save_xls.test_fails(test)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
    # unittest.main(testRunner=htmltestrunner.HTMLtestRunner(output='C:/Programacion/Python/Programas/RSAFE_V2/Results'))
