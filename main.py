from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser.get("https://google.com")


search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_result = browser.find_elements(By.CLASS_NAME, "LC20lb MBeuO DKV0Md")

print(search_result)
