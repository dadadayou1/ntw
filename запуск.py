from selenium import webdriver
from login import login
from deposit import deposit

# Определение и задание браузера и ссылки на страницу
browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
browser.get(link)

login(browser)
deposit(browser)
