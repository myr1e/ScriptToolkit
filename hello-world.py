# Script básico em Selenium que escreve "Hello World" na barra de pesquisas do Google

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.google.com.br/")

element = driver.find_element(By.NAME, "q")

element.send_keys("Hello World!", Keys.ENTER)
driver.find_element(By.CLASS_NAME, "gNO89b")
