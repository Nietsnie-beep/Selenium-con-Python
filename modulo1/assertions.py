import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException

class Assertions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15) #segundos
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    #how es tipo
    #what es valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__" :
    unittest.main(verbosity=2)



