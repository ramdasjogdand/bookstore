from selenium import webdriver
import unittest
from time import sleep


class BookStoreTestCase(unittest.TestCase):
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
        
    # def test_script1(self):
    #     driver = self.driver
    #     driver.get(self.base_url)

    #     get_title = driver.title
    #     print(get_title)    

    def user_name(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id=\"Email\"]").send_keys("pratik@gmail.com")
        driver.find_element(By.ID, "passWord").send_keys("1234")
        driver.find_element(By.ID, "firstName").send_keys("pratik")
        driver.find_element(By.ID, "lastName").send_keys("rathi")
        driver.find_element(By.ID, "address").send_keys("pune")
        driver.find_element(By.ID, "phno").send_keys("1234567898")
        driver.find_element(By.NAME, "acceptance").click()
        driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/input[7]").click()

    # def login(self):
    #     self.driver.find_element(By.XPATH, "//*[@id=\"navbarNav\"]/ul/li[2]/span/a").click()
    #     self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[3]/td/a").click()
    #     self.driver.find_element(By.ID, "userName").send_keys("pratik@gmail.com")
    #     self.driver.find_element(By.ID, "Password").send_keys("1234")
    #     self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td/input[3]").click()

    # def books(self):
    #     self.driver.find_element(By.ID, "books").click()
    #     self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div[2]/form/input[3]").click()
    #     self.driver.find_element(By.XPATH, "//*[@id=\"topmid\"]/form/input").click()
    #     self.driver.find_element(By.NAME, "pay").click()

    # def payment(self):
    #     self.driver.find_element(By.ID, "cname").send_keys("pratik")
    #     self.driver.find_element(By.ID, "ccnum").send_keys("1111-1111-2222-2222")
    #     self.driver.find_element(By.ID, "expmonth").send_keys("may")
    #     self.driver.find_element(By.ID, "cvv").send_keys("123")
    #     self.driver.find_element(By.ID, "expyear").send_keys("2032")
    #     self.driver.find_element(By.ID, "fname").send_keys("pratik rathi")
    #     self.driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys("pr210@gmail.com")
    #     self.driver.find_element(By.ID, "adr").send_keys("pune")
    #     self.driver.find_element(By.ID, "city").send_keys("pune")
    #     self.driver.find_element(By.ID, "zip").send_keys("41103")
    #     self.driver.find_element(By.ID, "state").send_keys("maharashtra")
    #     self.driver.find_element(By.ID, "checked").click()  # Uncomment if necessary
    #     self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/form/input").click()

    def quit_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
