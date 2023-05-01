from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"


def click_for_five_secs(time_out):
    cookie = driver.find_element(By.CSS_SELECTOR, "div #cookie")
    while time.time() < time_out:
        cookie.click()


driver = webdriver.Chrome()

driver.get(URL)
driver.maximize_window()

store = driver.find_elements(By.CSS_SELECTOR, "#store div b")

store_dictionary = {}
for option in store:
    text = option.text.strip()
    if '-' in text:
        key, value = text.split('-')
        store_dictionary[key.strip()] = int("".join(value.strip().split(",")))

print(store_dictionary)

game_is_on = True
time_over = time.time() + 5*60
while game_is_on:
    timing = time.time() + 5
    click_for_five_secs(timing)
    product_list = []
    for key in store_dictionary:
        money = int("".join(driver.find_element(By.CSS_SELECTOR, "div #money").text.split(",")))
        if money >= store_dictionary[key]:
            product_list.append(key)
    affordable_product = driver.find_element(By.CSS_SELECTOR, f"#buy{product_list[-1]}")
    affordable_product.click()
    if time.time() > time_over:
        game_is_on = False
        cookies_per_sec = driver.find_element(By.CSS_SELECTOR, "#cps")
        print(cookies_per_sec.text)

driver.quit()
