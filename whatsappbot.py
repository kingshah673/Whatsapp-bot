from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
element.send_keys("Mohaib Bhai")
element.send_keys(Keys.ENTER)
element=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
while(True):
    element=WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
    element.send_keys("Bot Successfull")
    element.send_keys(Keys.ENTER)
    time.sleep(1)
# driver.close()
