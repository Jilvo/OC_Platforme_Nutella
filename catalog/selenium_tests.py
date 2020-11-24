from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class Selenium_test:
    def funct(self):
        PATH = "C:/Program Files (x86)/chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://purbeurre-jilvo.herokuapp.com/")
        driver.maximize_window
        # print(driver.title)

        go_to_login_page = driver.find_element_by_id("login")
        go_to_login_page.click()

        login_user = driver.find_element_by_id("username")
        login_pwd = driver.find_element_by_id("password")
        # print(login_user)
        # print(login_pwd)
        login_user.send_keys("test1")
        login_pwd.send_keys("test1")
        driver.find_element_by_id("submit").click()

        # go_to_home = driver.find_element_by_id("")

        search = driver.find_element_by_id("query")
        search.send_keys("steak")
        print(search.send_keys(Keys.RETURN))

        link = driver.find_element_by_id("choice_product_input")
        link.click()

        lipids = driver.find_element_by_id("salts")
        print("Il y a " + lipids.text + " gramme(s) de sel pour 100g")

        time.sleep(5)

        driver.close()
