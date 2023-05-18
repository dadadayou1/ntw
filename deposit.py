from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
 

def deposit(browser):

    deposit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.tab[ng-click='deposit()'][ng-class='btnClass2']")
    deposit_button.click()

    sleep(15)

 
