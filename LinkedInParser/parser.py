from linkedin_scraper import Person, actions
from selenium import webdriver
import time

driver = webdriver.Chrome()
email = "sanchitgupta456@gmail.com"
password = "Sls@J.123"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
time.sleep(30)
person = Person("https://www.linkedin.com/in/andre-iguodala-65b48ab5", driver=driver,scrape=False)
time.sleep(30)
person.scrape()
print(person)