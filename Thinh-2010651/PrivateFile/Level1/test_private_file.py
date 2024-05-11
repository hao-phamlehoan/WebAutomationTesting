import os
import time
import csv
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPrivateFile(unittest.TestCase):
  def setup(self):
    self.current_dir = os.path.dirname(os.path.abspath(__file__))
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    self.driver.maximize_window()
    self.driver.get("https://school.moodledemo.net/login/index.php")
    self.driver.find_element(By.ID, "username").send_keys("student")
    self.driver.find_element(By.ID, "password").send_keys("moodle")
    self.driver.find_element(By.ID, "loginbtn").click()
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".avatar").click()
    time.sleep(3)
    self.driver.find_element(By.LINK_TEXT, "Private files").click()
    time.sleep(15)
  def teardown_method(self):
    self.driver.quit()

  def test_private_file(self):
    count = 0
    with open("Level1/privatefile.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if count != 0:
              try:
                self.setup()
                if len(self.driver.find_elements(By.XPATH, "//div[2]/a/div/div[3]"))>0:
                  self.driver.find_element(By.XPATH, "//div[2]/a/div/div[3]").click()
                  time.sleep(5)
                  self.driver.find_element(By.XPATH, "//form/div/button[2]").click()
                  time.sleep(5)
                  self.driver.find_element(By.XPATH, "//button[contains(.,\'Yes\')]").click()
                  time.sleep(5)
                  self.driver.find_element(By.XPATH, "//span/input").click()
                  time.sleep(5)
                self.driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
                time.sleep(15)
                file_path = os.path.join(self.current_dir, 'test_data', row[0])
                self.driver.find_element(By.XPATH, "//form/div/div/div/input").send_keys(file_path)
                time.sleep(5)

                upload_button = WebDriverWait(self.driver, 60).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]"))
                )
                self.driver.execute_script("arguments[0].click();", upload_button)
                if row[0] in ["1MiB.txt", "50MiB.txt"]:
                    time.sleep(5)
                else:
                    time.sleep(100)
                self.driver.find_element(By.XPATH, "//span/input").click()
              except Exception as exc:
                print(f"Test {count}: Fail with error of {exc}")
              else:
                print(f"Testcase {count} for {row[0]} passed\n")
              finally:
                self.teardown_method()
            count = count + 1

if __name__ == "__main__":
    unittest.main()