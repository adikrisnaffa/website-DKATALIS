from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import pyautogui
import pytest

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

@pytest.fixture
def context():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demo.midtrans.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.postive
def test_positive(context) :
    buy_now = context.find_element(By.XPATH, '//a[@data-reactid=".0.0.0.2.0.0.5"]')
    buy_now.click()

    name = context.find_element(By.XPATH, '//input[@data-reactid=".0.0.1.0.3.0.0.0.1.0"]')
    name.clear()
    name.send_keys('Adikrisna Nugraha')

    email = context.find_element(By.XPATH, '//input[@data-reactid=".0.0.1.0.3.0.0.1.1.0"]')
    email.clear()
    email.send_keys('adikrisnanugraha@gmail.com')

    phone = context.find_element(By.XPATH, '//input[@data-reactid=".0.0.1.0.3.0.0.2.1.0"]')
    phone.clear()
    phone.send_keys('0895356997421')

    address = context.find_element(By.XPATH, '//textarea[@data-reactid=".0.0.1.0.3.0.0.4.1.0"]')
    address.clear()
    address.send_keys('Tangerang Selatan')

    postal_code = context.find_element(By.XPATH, '//input[@data-reactid=".0.0.1.0.3.0.0.5.1.0"]')
    postal_code.clear()
    postal_code.send_keys('15540')


    checkout = context.find_element(By.XPATH, '//div[@data-reactid=".0.0.1.1.0"]')
    checkout.click()
    time.sleep(5)

    try:
        WebDriverWait(context,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="snap-body"]/div[1]')))
        print('modal muncul')
        credit_card = context.find_element(By.XPATH, '//a[@href="#/credit-card"]')
        credit_card.click()

    except TimeoutException :
        pass

    number_credit_card= context.find_element(By.CSS_SELECTOR, "input[type='tel'][autocomplete='cc-number']")
    number_credit_card.send_keys('')

    expiry = context.find_element(By.ID, 'card-expiry')
    expiry.send_keys('')

    cvv = context.find_element(By.ID, 'card-cvv')
    cvv.send_keys('')

    pay = context.find_element(By.CSS_SELECTOR, "button[type='button'].btn.full.disabled.inactive")
    pay.click()