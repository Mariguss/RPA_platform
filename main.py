from selenium import webdriver

from rpa_worker.pages import LoginPage
from rpa_worker.handlers.register_customer import register_customer

BASE_URL = "http://localhost:8888"
print("before driver inited")

driver = webdriver.Chrome()
print("after driver inited")
LoginPage(driver, BASE_URL).login("admin", "admin")

# register_customer(driver, BASE_URL, "test 6", "email") из-за email будет ошибка
register_customer(driver, BASE_URL, "test 7", "test@mail.com")
