from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

url = r'https://play.typeracer.com/'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get(url)

privacy_prompt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "qc-cmp2-summary-buttons")))
privacy_prompt.find_elements_by_tag_name('button')[-1].click()

practice = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'gwt-Anchor')))
for obj in practice:
    if obj.text == 'Practice':
        obj.click()
        break

time.sleep(3)

text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.inputPanel')))
text_frag = text.find_elements_by_tag_name('span')

result = ''

for t in text_frag[:-1]:
    result += t.text
result += f' {text_frag[-1].text}'

time.sleep(4)

print(result)


input_field = driver.find_element_by_class_name('txtInput')
pyautogui.write(result, interval=0.003)

