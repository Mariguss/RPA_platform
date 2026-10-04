import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from shared.customer import Customer


class NewCustomerPage:
    URL_PATH: str = "/societe/card.php?action=create"

    FIELDS_MAP = {
        "name": (By.NAME, "name"),
        "name_alias": (By.NAME, "name_alias"),
        "prospect" : (By.NAME, "prospect"),
        "customer": (By.NAME, "customer"),
        "customer_code": (By.NAME, "customer_code"),
        "address": (By.NAME, "address"),
        "zipcode": (By.NAME, "zipcode"), # почтовый индекс
        "town": (By.NAME, "town"),
        "country": (By.NAME, "country"),
        # Штат/Провинция (после утсановки страны)
        "phone": (By.NAME, "phone"),
        "fax": (By.NAME, "fax"),
        "url": (By.NAME, "url"),  # сайт
        "email": (By.NAME, "email"),
        "idprof1": (By.NAME, "idprof1"),
        "idprof2": (By.NAME, "idprof2"),
        "idprof3": (By.NAME, "idprof3"),
        "idprof4": (By.NAME, "idprof4"),
        "idprof5": (By.NAME, "idprof5"),
        "idprof6": (By.NAME, "idprof6"),
        "assujtva_value": (By.NAME, "assujtva_value"),  # Используется налог с продаж checkbox
        "tva_intra": (By.NAME, "tva_intra"),  # Код плательщика НДС
        "euid": (By.NAME, "euid"),  # EUID
    }

    def __init__(self, driver, base_url: str):
        print("New Customer Page: init")
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        print("New Customer Page: open")
        self.driver.get(self.base_url + self.URL_PATH)

    def select_by_typing(self, container_id: str, text_to_type: str):
        print("New Customer Page: select_by_typing")
        dropdown = self.wait.until(
            ec.element_to_be_clickable((By.ID, container_id))
        )
        dropdown.click()

        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.send_keys(text_to_type)
        actions.perform()

        time.sleep(2)



        # search_input = self.wait.until(
        #     ec.element_to_be_clickable((By.CSS_SELECTOR, "input.select2-search__field"))
        # )
        # search_input.clear()
        # search_input.send_keys(text_to_type)
        #
        first_result_xpath = "//li[contains(@class, 'select2-results__option') and not (contains(@class, 'loading'))]"
        first_result = self.wait.until(
            ec.element_to_be_clickable((By.XPATH, first_result_xpath))
        )
        first_result.click()


    def fill(self, schema: Customer):
        print("New Customer Page: fill")
        data_dict = schema.model_dump(exclude_unset=True)

        for field_name, value in data_dict.items():
            locator = self.FIELDS_MAP.get(field_name)
            if not locator:
                continue
            if field_name == "country":
                self.select_by_typing("select2-selectcountry_id-container", str(value))
                continue

            element = self.driver.find_element(*locator)

            if isinstance(value, bool):
                if value != element.is_selected():
                    element.click()
            else:
                element.clear()
                element.send_keys(value)


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