from selenium import webdriver
import unittest
from time import sleep

class BookStore:
    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        driver_path = '/usr/local/bin/chromedriver'
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')


        self.driver = webdriver.Chrome(driver_path, chrome_options=chromeOptions)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        path = 'http://54.173.109.51:8080/books/CustomerRegister.html'
        self.base_url = path

    def test_user_name(self):
        time.sleep(2)  # Add a delay to ensure page load
        self.driver.find_element_by_xpath("//*[@id='Email']").send_keys("pratik@gmail.com")
        self.driver.find_element_by_id("passWord").send_keys("1234")
        self.driver.find_element_by_id("firstName").send_keys("pratik")
        self.driver.find_element_by_id("lastName").send_keys("rathi")
        self.driver.find_element_by_id("address").send_keys("pune")
        self.driver.find_element_by_id("phno").send_keys("1234567898")
        self.driver.find_element_by_name("acceptance").click()
        self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/input[7]").click()

    def test_login(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='navbarNav']/ul/li[2]/span/a").click()
        self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/a").click()
        self.driver.find_element_by_id("userName").send_keys("pratik@gmail.com")
        self.driver.find_element_by_id("Password").send_keys("1234")
        self.driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/input[3]").click()

    def test_books(self):
        time.sleep(2)
        self.driver.find_element_by_id("books").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/form/input[3]").click()
        self.driver.find_element_by_xpath("//*[@id='topmid']/form/input").click()
        self.driver.find_element_by_name("pay").click()

    def test_payment(self):
        time.sleep(2)
        self.driver.find_element_by_id("cname").send_keys("pratik")
        self.driver.find_element_by_id("ccnum").send_keys("1111-1111-2222-2222")
        self.driver.find_element_by_id("expmonth").send_keys("may")
        self.driver.find_element_by_id("cvv").send_keys("123")
        self.driver.find_element_by_id("expyear").send_keys("2032")
        self.driver.find_element_by_id("fname").send_keys("pratik rathi")
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys("pr210@gmail.com")
        self.driver.find_element_by_id("adr").send_keys("pune")
        self.driver.find_element_by_id("city").send_keys("pune")
        self.driver.find_element_by_id("zip").send_keys("41103")
        self.driver.find_element_by_id("state").send_keys("maharashtra")
        # self.driver.find_element_by_id("checked").click()
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/form/input").click()

    # def teardown_method(self):
    #     self.driver.quit()

if __name__ == "__main__":
    tests = BookStore()jhfdkj
    tests.test_user_name()
    tests.test_login()
    tests.test_books()
    tests.test_payment()
    # tests.teardown_method()
