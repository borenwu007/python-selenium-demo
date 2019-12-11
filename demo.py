from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

button_path = '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button'

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'g:\\'}
options.add_experimental_option('prefs', prefs)
 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://t00y.com/file/21552682-413122821")
time.sleep(1)

elem = WebDriverWait(driver,30).until(lambda dirver:driver.find_element_by_xpath(button_path))
elem.click()
time.sleep(50)
print("finish")

 
