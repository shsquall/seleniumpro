from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)

KEYWORD = "buy domain"

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://google.com")


search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements(By.CLASS_NAME, "g")

search_results = browser.find_elements(By.CSS_SELECTOR, "h3")
for result in search_results:
    print(result.text)