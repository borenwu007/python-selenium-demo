from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

link_path = '//*[@id="resource-list"]/li/label/a'
button_path = '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button'

ip = '182.87.240.226'
port = 23564
username = 'borenwu@163.com'
password = '871120wbrW'

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'g:\\'}
options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(chrome_options=options)
browser.get("https://it.15kankan.com/info/toB792590")
time.sleep(3)

handle = browser.current_window_handle
browser.find_element_by_xpath(link_path).click()
handles = browser.window_handles

browser.switch_to_window(handles[-1])
elem = WebDriverWait(browser,30).until(lambda dirver:browser.find_element_by_xpath(button_path))
elem.click()
