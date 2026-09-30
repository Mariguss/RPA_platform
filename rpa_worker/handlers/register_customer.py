from urllib.parse import urlparse, parse_qs

from selenium.webdriver.remote.webdriver import WebDriver

from pages import NewCustomerPage
from rpa_worker.exceptions import BusinessException


def extract_socid(url: str) -> int | None:
    qs = parse_qs(urlparse(url).query)
    return int(qs["socid"][0]) if "socid" in qs else None

def register_customer(driver: WebDriver, base_url_, name_, email_) -> int | None:
    page = NewCustomerPage(driver, base_url_)
    page.open()
    page.fill(name=name_, email=email_)
    page.submit()
    # print(driver.current_url)  # куда перекинуло после сохранения?

    socid = extract_socid(driver.current_url)
    if socid is None:
        error = page.read_error_message()
        raise BusinessException(error or "Клиент не создан")
    return socid
