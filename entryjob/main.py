from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\\Users\\ximus\\Documents\\GitHub\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://hh.ru/account/login?backurl=%2F&hhtmFrom=main")

number = driver.find_element("name", "login")
number.send_keys("login")

button = driver.find_elements(By.CSS_SELECTOR, "button.bloko-link.bloko-link_pseudo")
button[-1].click()

password = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[2]/fieldset/input')
password.send_keys("password")

button = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/form/div[4]/div/button[1]')
button.click()
time.sleep(2)

button = driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div[2]/div/div/div/div/form/div/div[2]/button')
button.click()

vacancy = driver.find_elements(By.CSS_SELECTOR, "a.bloko-button.bloko-button_kind-primary.bloko-button_scale-small")
for i in vacancy:
    i.click()
