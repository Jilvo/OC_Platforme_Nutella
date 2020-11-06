from selenium import webdriver
from selenium.webdriver import ActionChains
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

link = driver.find_element_by_id('choice_product_input')
link.click()

search = driver.find_elements_by_class_id('produit_choosen_result')
print(search)

link = driver.find_elements_b




time.sleep(1)

driver.close()