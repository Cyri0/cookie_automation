from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')


def waitFor(xpath=False, id=False):
    wait = WebDriverWait(driver, 10)

    consentBtn = None

    if xpath:
        consentBtn = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    elif id:
        consentBtn = wait.until(
            EC.presence_of_element_located((By.ID, id))
        )

    return consentBtn

consentBtn = waitFor(xpath="/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
consentBtn.click()

englishLang = waitFor(xpath='//*[@id="langSelect-EN"]')
englishLang.click()

cookie = waitFor(id='bigCookie')

cookieNumber = waitFor(id='cookies')

cookie.click()

def testShop():
    items = driver.find_elements(By.CLASS_NAME, "unlocked")
    num = int(cookieNumber.text.split(' ')[0])

    for item in items:
        price = item.find_element(By.CLASS_NAME, "price")

        if int(price.text.replace(',','')) < num:
            item.click()

while True:
    testShop()
    cookie.click()

input("Press Enter to close the browser...")