from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class FacebookTest(unittest.TestCase):
    def setUp(self):
        chromeOptions = webdriver.ChromeOptions()
        driver_path = '/usr/local/bin/chromedriver'
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--disable-gpu')
        chromeOptions.add_argument('--no-sandbox')


        self.driver = webdriver.Chrome(driver_path, chrome_options=chromeOptions)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        path = 'https://www.facebook.com/'
        self.base_url = path

    def test_registration(self):
        # Click on the Create New Account button
        create_account_button = self.driver.find_element(By.CSS_SELECTOR, "a[data-testid='open-registration-form-button']")
        create_account_button.click()

        # Enter first name
        first_name_field = self.driver.find_element(By.NAME, "firstname")
        first_name_field.send_keys("John")

        # Enter last name
        last_name_field = self.driver.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Doe")

        # Enter email
        email_field = self.driver.find_element(By.NAME, "reg_email__")
        email_field.send_keys("johndoe@example.com")

        # Enter password
        password_field = self.driver.find_element(By.ID, "password_step_input")
        password_field.send_keys("mypassword123")

        # Select date of birth
        day_dropdown = self.driver.find_element(By.ID, "day")
        self.select_dropdown_option(day_dropdown, "15")

        month_dropdown = self.driver.find_element(By.ID, "month")
        self.select_dropdown_option(month_dropdown, "May")

        year_dropdown = self.driver.find_element(By.ID, "year")
        self.select_dropdown_option(year_dropdown, "1990")

        # Select gender
        gender_radio_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='2']")
        gender_radio_button.click()

        # Click on the Sign Up button
        signup_button = self.driver.find_element(By.NAME, "websubmit")
        signup_button.click()

        # Verify registration is successful
        self.assertIn("https://www.facebook.com/checkpoint/", self.driver.current_url)

    def test_login(self):
        # Enter email
        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys("johndoe@example.com")

        # Enter password
        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys("mypassword123")

        # Click on the Log In button
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()

        # Verify login is successful
        self.assertIn("https://www.facebook.com/", self.driver.current_url)

    def select_dropdown_option(self, dropdown, option_text):
        options = dropdown.find_elements(By.TAG_NAME, "option")
        for option in options:
            if option.text == option_text:
                option.click()
                break

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()