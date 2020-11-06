from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://purbeurre-jilvo.herokuapp.com/")
driver.maximize_window
print(driver.title)

search = driver.find_element_by_id("query")
search.send_keys("steak")
print(search.send_keys(Keys.RETURN))

time.sleep(1)

driver.close()