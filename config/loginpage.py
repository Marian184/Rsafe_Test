import time
from selenium import webdriver
import unittest

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_id     = "Login"
        self.verify_code_id      = 'emc'
        self.finish_link_id      = '//*[@title="Finish"]'
        self.save_code_link_id   = 'save'

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_username(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        driver.find_element_by_name('Login').click()

    def verify_code(self,code):
        driver.find_element_by_id(self.verify_code_id).send_keys(code)
        driver.find_element_by_id(self.save_code_link_id).click()
        time.sleep(3)
        driver.find_element_by_xpath(self.finish_link_id).click()

