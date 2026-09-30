from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


BASE_URL = "http://localhost:8888"

driver = webdriver.Chrome()

try:
    driver.get(f"{BASE_URL}")
    wait = WebDriverWait(driver, 10)

    wait.until(ec.presence_of_element_located((By.ID, "username"))).send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # признак успешного входа: страница больше не содержит форму логина
    wait.until(ec.invisibility_of_element_located((By.ID, "username")))
    print("Вошли, URL:", driver.current_url)
    wait.until(ec.presence_of_element_located((By.ID, "mainmenutd_companies"))).click()
    print("Переход на контрагенты, URL:", driver.current_url)

    # wait.until(ec.presence_of_element_located((By.CLASS_NAME, "vsmenu"))).click()
    driver.find_element(By.LINK_TEXT, "Список").click()
    print("Переход на список контрагентов, URL:", driver.current_url)

    elements = driver.find_elements(By.CLASS_NAME, "oddeven")
    element = driver.find_element(By.CLASS_NAME, "oddeven")
    print(*elements, sep="\n")
    print(element.text)

finally:
    driver.quit()