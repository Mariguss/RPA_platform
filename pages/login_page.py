from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver, base_url: str):
        print("Login Page: init")
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username: str, password: str):
        print("Login Page: login")
        self.driver.get(f"{self.base_url}")
        self.wait.until(ec.presence_of_element_located((By.ID, "username"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # признак успешного входа: страница больше не содержит форму логина
        self.wait.until(ec.invisibility_of_element_located((By.ID, "username")))
