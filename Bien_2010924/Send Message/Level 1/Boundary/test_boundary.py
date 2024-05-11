from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import unittest
import csv
import time


class TestTest4(unittest.TestCase):
    def __init__(self, arg):
        super().__init__(arg)

    def set_up_drive(self):
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            "/Users/bientran/Downloads/chromedriver-mac-arm64/chromedriver")
        self.vars = {}
        self.driver.get(
            "https://school.moodledemo.net/my/courses.php")
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher")
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()

    def test_level1_boundary(self):
        count = 0

        with open("./boundary.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if count == 4:
                    self.set_up_drive()
                    time.sleep(10)
                    self.driver.find_element(
                        By.CSS_SELECTOR, ".fa-comment-o").click()
                    time.sleep(10)
                    self.driver.find_element(
                        By.CSS_SELECTOR, "#view-overview-messages-toggle .font-weight-bold").click()
                    time.sleep(10)
                    self.driver.find_element(
                        By.XPATH, "//div[3]/div[2]/div[2]/a/div/p/span").click()
                    time.sleep(10)
                    self.driver.find_element(
                        By.CSS_SELECTOR, ".d-flex > .form-control").click()
                    time.sleep(10)
                    self.driver.find_element(
                        By.XPATH, "//textarea").send_keys(f"{row[1]}")
                    time.sleep(10)
                    self.driver.find_element(
                        By.CSS_SELECTOR, ".fa-paper-plane").click()
                    self.teardown_method()
                    print(f"Test {count}: Pass")
                    time.sleep(5)
                count += 1


if __name__ == "__main__":
    unittest.main(warnings='ignore')
