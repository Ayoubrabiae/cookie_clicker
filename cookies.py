from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

lang_btn_id = "langSelect-EN"
cookie_id = "bigCookie"
cookies_id = "cookies"
product_prefex = "product"
product_price_prefex = "productPrice"

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID, lang_btn_id))
)

lang_btn = driver.find_element(By.ID, lang_btn_id)
lang_btn.click()

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies = driver.find_element(By.ID, cookies_id).text.split(" ")[0].replace(",", "")
    cookies = int(cookies)
    
    for i in range(6):
        product_price = driver.find_element(By.ID, product_price_prefex + str(i)).text.replace(",", "")
        
        if not product_price.isdigit():
            continue

        product_price = int(product_price)


        if cookies >= product_price:
            product = driver.find_element(By.ID, product_prefex + str(i))
            product.click()
            break



time.sleep(100)

driver.quit()