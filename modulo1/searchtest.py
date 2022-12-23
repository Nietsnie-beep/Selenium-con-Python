import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15) #segundos

    def test_search_tee(self):
        driver = self.driver;
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver;
        search_field = driver.find_element(By.NAME, 'q')
        search_field.send_keys("salt shaker")
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    def test_search_text_field(self):

        search_field = self.driver.find_element(By.ID, "search")

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element(By.NAME, "q")

    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME, "button")

    def test_count_of_promo_images(self):
        #div promos
        banner_list = self.driver.find_element(By.CLASS_NAME, "promos")
        banners = banner_list.find_elements(By.TAG_NAME, "img")
        #validaciones para ver si una condicion se cumple o no
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    def test_shoping_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__" :
    unittest.main(verbosity=2)
