from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig( 
    encoding='utf-8',
    format="%(asctime)s %(message)s",
    level=logging.ERROR,
    handlers=[
        logging.FileHandler("failure.log"),
    ],
    )

NUMBER_OF_ASSETS = 5000
REFRESH_TIMEOUT = 45

url = "https://opensea.io/assets/matic/0x4055e3503d1221af4b187cf3b4aa8744332a4d0b"

driver = webdriver.Chrome()
for i in range(NUMBER_OF_ASSETS):
    driver.get(f'{url}/{i}')
    refresh_button = driver.find_element(By.XPATH,"//i[@value='refresh']").click()
    # find out if it has found the toast
    try:
        WebDriverWait(driver, REFRESH_TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
        print(f'{i} refreshed succesfully')
    except:
        logging.error(f'{i}')
driver.close()