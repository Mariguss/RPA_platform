from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewCustomerPage:
    URL_PATH: str = "/societe/card.php?action=create"

    def __init__(self, driver, base_url: str):
        print("New Customer Page: init")
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        print("New Customer Page: open")
        self.driver.get(self.base_url + self.URL_PATH)

    def fill(self, name: str, email: str | None = None):
        print("New Customer Page: fill")
        self.wait.until(ec.presence_of_element_located((By.NAME, "name"))).send_keys(name)
        if email:
            self.driver.find_element(By.NAME, "email").send_keys(email)

    def submit(self):
        print("New Customer Page: submit")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][name='save']").click()

    def read_error_message(self, timeout: int = 3) -> str | None:
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".jnotify-notification-error")
                )
            )
            return element.text.strip() or None
        except TimeoutException:
            return None