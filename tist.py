import sys
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
i=1
while i <2:
    driver = webdriver.Chrome()
    driver = driver.get('https://selenium.dev/selenium/web/single_text_input.html')

    ActionChains(driver)\
        .key_down(Keys.SHIFT)\
        .send_keys("a")\
        .key_up(Keys.SHIFT)\
        .send_keys("b")\
        