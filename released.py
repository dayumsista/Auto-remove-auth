email = "blizzard@email.here"
password = "password.here"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import requests

driver = webdriver.Chrome()
time.sleep(2)
driver.get('https://account.battle.net/login/zh/') 
time.sleep(2)

auth_key = input("Please enter ur Auth key: ")
time.sleep(2)

wait = WebDriverWait(driver, 10)
time.sleep(2)
email_input = driver.find_element(By.ID, 'accountName')
password_input = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.ID, 'submit')
for char in email:
    email_input.send_keys(char)
    time.sleep(random.uniform(0.07, 0.14)) 
time.sleep(1)
for char in password:
    password_input.send_keys(char)
    time.sleep(random.uniform(0.07, 0.14)) 
time.sleep(1)
submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
submit_button.click()

url = f"https://blizzard.xiaocaicai.com/api/directGet?secret={auth_key}"
response = requests.get(url)
data = response.json()
authValue = data['code']
auth_input = wait.until(EC.element_to_be_clickable((By.ID, 'authValue')))

for char in authValue:
    auth_input.send_keys(char)
    time.sleep(random.uniform(0.07, 0.14))
time.sleep(1)
submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
submit_button.click()
time.sleep(2)

driver.get('https://account.battle.net/security/authenticator/detach?locale=zh-tw') 
time.sleep(2)
confirm_button = wait.until(EC.element_to_be_clickable((By.ID, 'attach-detach-confirm')))
confirm_button.click()
time.sleep(5)

response2 = requests.get(url)
data2 = response2.json()
authValue2 = data2['code']
auth_input2 = driver.find_element(By.XPATH, '//input[@placeholder="驗證碼"]')

for char in authValue2:
    auth_input2.send_keys(char)
    time.sleep(random.uniform(0.07, 0.14))
time.sleep(1)
submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "提交")]')
submit_button.click()
time.sleep(5)

driver.quit()