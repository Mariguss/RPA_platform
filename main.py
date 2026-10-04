import json
from pathlib import Path

from selenium import webdriver

from rpa_worker.pages import LoginPage
from rpa_worker.handlers.register_customer import register_customer
from shared.customer import Customer

BASE_URL = "http://localhost:8888"
print("before driver inited")

driver = webdriver.Chrome()
print("after driver inited")

def load_test_data():
    json_path = Path(__file__).parent / "test_data_customer.json"
    json_text= json_path.read_text(encoding="utf-8")
    data_dict = json.loads(json_text)["test_customer"]
    return Customer.model_validate(data_dict)

LoginPage(driver, BASE_URL).login("admin", "admin")

# register_customer(driver, BASE_URL, "test 6", "email") из-за email будет ошибка
test_data = load_test_data()
register_customer(driver, BASE_URL, schema=test_data)





#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# # Метод driver.get перейдет на страницу, указанную в URL.
# # WebDriver будет ждать полной загрузки страницы (то есть срабатывания события onload),
# # прежде чем вернуть управление вашему тесту или скрипту.
# # Имейте в виду, что если на странице при загрузке используется много AJAX,
# # WebDriver может не знать, когда она полностью загрузится:
# # !!!Если вам нужно убедиться, что такие страницы полностью загружены, вы можете использовать waits.
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q") # name="q"
# # Для надежности мы сначала удалим весь предварительно введенный текст в поле ввода
# # (например, «Поиск»), чтобы он не повлиял на результаты поиска:
# elem.clear() # очищаем поле ввода
# elem.send_keys("pycon") # ввод
# elem.send_keys(Keys.RETURN) # отправляет нажатие Enter в элемент
# assert "No results found." not in driver.page_source
# # Вместо close можно вызвать метод quit.
# # Метод quit завершает работу браузера, а close закрывает одну вкладку,
# # но если открыта только одна вкладка, то по умолчанию большинство браузеров завершают работу полностью.
# driver.close() # закрываем вкладку
