from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def log_in(email, pw):
    global browser
    browser = webdriver.Chrome(service=Service(r""))
    browser.get("https://pocketoption.com/en/login")

    # Login Process
    browser.implicitly_wait(10)
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys(email)

    pw_field = browser.find_element(By.NAME, "password")
    pw_field.send_keys(pw)

    # Mannual log in time
    time.sleep(20)

    # Keys
    global high
    global low
    global bet_amount

    high = browser.find_element(By.XPATH, "//span[@class='payout__text payout__text-lh']")
    low = browser.find_element(By.XPATH, "(//span[@class='payout__text payout__text-lh'])[2]")
    bet_amount = browser.find_element(By.XPATH, "(//input[@type='text'])[3]")

# Change buy amount
def change_buy(amount):
    global previous_amount
    bet_amount.send_keys(Keys.BACK_SPACE)
    bet_amount.send_keys(Keys.BACK_SPACE)
    bet_amount.send_keys(Keys.BACK_SPACE)
    bet_amount.send_keys(Keys.BACK_SPACE)
    bet_amount.send_keys(Keys.BACK_SPACE)

    time.sleep(0.1)
    bet_amount.send_keys(amount)

# Check current balance
def current_balance():
    balance = browser.find_element(By.XPATH, "//a[@class='balance_current']")
    return (float((balance.text)[1:]))

def buy_high(amount):
    change_buy(amount)
    high.click()

def buy_low(amount):
    change_buy(amount)
    low.click()


if __name__ == "__main__":

    # Login Credentials
    email = ""
    pw = ""

    # Login + Mannual Navigation
    log_in(email, pw)

    # Starts to trade
    print("Trade is starting...")
    amount = "1"
    previous_amount = current_balance()
    buy_high(amount)
    time.sleep(10)

    while True:
        if current_balance() > previous_amount:
            amount = "1"
            previous_amount = current_balance()
            buy_low(amount)
            time.sleep(10)

        else: 
            previous_amount = current_balance()
            amount = str(float(amount) * 2.5)
            buy_low(amount)
            time.sleep(10)

        if current_balance() > previous_amount:
            amount = "1"
            previous_amount = current_balance()
            buy_high(amount)
            time.sleep(10)

        else: 
            previous_amount = current_balance()
            amount = str(float(amount) * 2.5)
            buy_high(amount)
            time.sleep(10)

