from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import shutil
from datetime import datetime
from datetime import timezone

def get_all_data( stock_names ):
    if isinstance(stock_names, list) != True:
        stock_names = [stock_names]

    chromePath = "/home/public/chrome_headless/chromedriver"
    chromeOptions = Options()
    chromeOptions.headless = True

    today = datetime.today()
    # .strftime('%Y-%m-%d')
    # dt = datetime(int(tod[0:4]), int(tod[4:6]), int(tod[6:8])-1).replace(tzinfo=timezone.utc).timestamp()
    dt = int((today - datetime(1970, 1, 1)).total_seconds())
    dt = str( dt )
    driver = webdriver.Chrome(executable_path=chromePath, options=chromeOptions)
    driver.set_window_size(1000, 800)
    driver.set_window_position(0,0)
    driver.implicitly_wait(5)

    for stock in stock_names:
        driver.get("https://finance.yahoo.com/quote/" + stock + "/history?period1=1420070400&period2=" + dt + "&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true")
        download = driver.find_element_by_xpath("//html//body//div[1]//div//div//div[1]//div//div[3]//div[1]//div//div[2]//section//div[1]//div[2]//span[2]//a//span")
        download.click()
        time.sleep(3)

    driver.quit()
    print('Successful!')

def get_new_data( stock_names ):
    if isinstance(stock_names, list) != True:
        stock_names = [stock_names]

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.set_window_size(1000, 800)
    driver.set_window_position(0,0)
    driver.implicitly_wait(5)

    for stock in stock_names:
        driver.get("https://finance.yahoo.com/quote/" + stock + "/history")
        download = driver.find_element_by_xpath("//html//body//div[1]//div//div//div[1]//div//div[3]//div[1]//div//div[2]//section//div[1]//div[2]//span[2]//a//span")
        download.click()
        time.sleep(3)

    driver.quit()
    print('Successful!')

