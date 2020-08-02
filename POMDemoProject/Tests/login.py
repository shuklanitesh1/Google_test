from selenium import webdriver
import time
import unittest
import sys
import os
import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))  # dots depends on the directory structure
from SampleProject.POMDemoProject.Pages.loginPage import Loginpage
from SampleProject.POMDemoProject.Pages.homPage import HomePage


class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Nitesh Shukla\PycharmProjects\Google_test\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_valid_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        # homepage.click_logout() #its not working due to link_text locator not working
        time.sleep(3)

    def test_02_invalid_login_username(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Loginpage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        message = driver.find_element_by_xpath().text
        self.assertEqual(message, "Invalid credentials")
        
        #Code without POM
        # self.driver.find_element_by_id("txtUsername").send_keys("admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click() # Not working



    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=r"C:/Users/Nitesh Shukla/PycharmProjects/Google_test/SampleProject/POMDemoProject/Logs/html.logs"))
