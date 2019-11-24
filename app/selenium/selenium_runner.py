from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By


class TestSuite(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('no-sandbox')
        self.driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub', desired_capabilities=options.to_capabilities())
        self.driver.implicitly_wait(10)

    def test_home_page(self):
        self.home_page = "http://web:8000"
        self.driver.get(self.home_page)
        time.sleep(10)
        # elem = self.driver.find_element_by_name("q")
        print(self.driver.title)
        assert "UVA Furniture" in self.driver.title

    def test_register(self):
        self.home_page = "http://web:8000"
        self.driver.get(self.home_page)
        self.driver.find_element_by_id("register").click()
        assert "http://web:8000/register" in self.driver.current_url
        self.driver.find_element_by_id(
            "id_first_name").send_keys("test_user_first")

        self.driver.find_element_by_id(
            "id_last_name").send_keys("test_user_last")
        self.driver.find_element_by_id("id_password").send_keys("password")
        self.driver.find_element_by_id("id_email").send_keys("test@test.com")
        self.driver.find_element_by_id("submitbtn").click()
        assert "http://web:8000/register" in self.driver.current_url

    def login(self):
        self.home_page = "http://web:8000"
        self.driver.get(self.home_page)
        self.driver.find_element_by_id("login").click()
        assert "http://web:8000/login" in self.driver.current_url
        self.driver.find_element_by_id("email").send_keys("testing@manual.com")
        self.driver.find_element_by_id("login-input").send_keys("password")
        self.driver.find_element_by_id("loginbtn").click()
        assert "http://web:8000" in self.driver.current_url

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
