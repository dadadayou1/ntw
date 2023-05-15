from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test1():
    browser = webdriver.Chrome()
    # искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    link="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    browser.get(link)

    # Ищем кнопку Login и кликаем по ней
    option1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-lg")
    option1.click()

    # открываем выпадающее меню
    menu = browser.find_element(By.NAME,"userSelect" )
    menu.click()

    #Выбрали пользователя и кликаем по входу
    menu = Select(browser.find_element(By.NAME, "userSelect"))
    menu.select_by_value("1")
    button_login=browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button_login.click()
    
    browser.quit()

    time.sleep(15) 
test1()

 

 