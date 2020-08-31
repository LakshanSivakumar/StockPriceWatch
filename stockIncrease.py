# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from mail import sendmail
import time

# initial declaration
stockName = input("What is the stock you are looking for: ")
watchPrice = input("What is your watch price for the stock?")
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

'''
Finds the Stock
'''
driver.get("https://www.nasdaq.com/market-activity/stocks")
search_bar = driver.find_element_by_class_name("find-symbol__input")
search_bar.send_keys(stockName, Keys.ENTER)
time.sleep(4)
stockPrice = driver.find_element_by_xpath(
    "/html/body/div[4]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]")
initial_stockPrice = stockPrice.text
driver.minimize_window()

# Main code Execution
while True:
    updated_stockPrice = driver.find_element_by_xpath(
        "/html/body/div[4]/div/main/div[2]/div[3]/section/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/span[1]/span[2]")
    updated_stockPrice_text = updated_stockPrice.text
    if updated_stockPrice_text > initial_stockPrice:
        print(
            "The Stock Price of " + stockName + " has increased from " + initial_stockPrice + "to " + updated_stockPrice_text)
        initial_stockPrice = updated_stockPrice_text

    elif updated_stockPrice_text < initial_stockPrice:
        print(
            "The Stock Price of " + stockName + " has decreased from " + initial_stockPrice + "to " + updated_stockPrice_text)

        initial_stockPrice = updated_stockPrice_text

    else:
        print(
            "The Stock Price of " + stockName + " has not changed and the current to price is: " + updated_stockPrice_text)
    # watch price target
    if watchPrice == updated_stockPrice_text:
        sendmail()

    time.sleep(10)
