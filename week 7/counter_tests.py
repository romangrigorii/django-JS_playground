import os
import pathlib
import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

# specify the filename if the .html file below
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome() # select the web broswer
# driver.get(file_uri("counter.html"))

class WebpageTests(unittest.TestCase):

    def test_title(self):
        """ title test """
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title,"Counter")

    def test_increase(self):
        """ increase test """
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")
    
    def test_decrease(self):
        """ decrease test """
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element("id","decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        """ multiple increase test """
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID,"increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME,"h1").text,"3")


if __name__ == "__main__":
    unittest.main()
