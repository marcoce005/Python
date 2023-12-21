from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

def close():
    driver.close()

    path = "geckodriver.log"
    os.unlink(path)

driver = webdriver.Firefox()        ## open firefox
driver.get("https://google.com")                ## search the site

try:
    name = driver.find_element(by = By.ID, value = 'ft_un')         ##insert user name
    name.send_keys('marco.cellini')

    psw = driver.find_element(by = By.ID, value = 'ft_pd')          ## insert password
    psw.send_keys('PippoPluto')

    psw.send_keys(Keys.ENTER)

    close()

except:
    print("Login già effettuato connessione ad internet già presente")
    close()