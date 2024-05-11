from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import csv
import time

class TestLogin(unittest.TestCase):
  def __init__(self, arg):
    super().__init__(arg)

  def set_up_drive(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    self.driver.get("https://school.moodledemo.net")
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(5)

  def teardown_method(self):
    self.driver.quit()

  def test_login(self):
    count = 0

    with open("Level1/login.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if count != 0:
                try:
                  self.set_up_drive()
                  self.driver.find_element(By.ID, "username").send_keys(row[0])
                  self.driver.find_element(By.ID, "password").send_keys(row[1])
                  self.driver.find_element(By.ID, "loginbtn").click()
                  time.sleep(10)
                except Exception as exc:
                  print(f"Test {count}: Fail with error of {exc}")
                else:
                  print(f"Test {count}: Pass")
                finally:
                  self.teardown_method()
                  time.sleep(5)

            count += 1

if __name__ == "__main__":
  unittest.main(warnings='ignore')
