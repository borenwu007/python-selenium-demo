from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from get_random_link import get_link
import time

file_name = 'links.txt'
link_path = '//*[@id="resource-list"]/li/label/a'
button_path = '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button'

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'g:\\download'}
options.add_experimental_option('prefs', prefs)

link = get_link(file_name)
print(link)

browser = webdriver.Chrome(chrome_options=options)
browser.get(link)
time.sleep(3)

handle = browser.current_window_handle
browser.find_element_by_xpath(link_path).click()
handles = browser.window_handles

browser.switch_to_window(handles[-1])
elem = WebDriverWait(browser,30).until(lambda dirver:browser.find_element_by_xpath(button_path))
elem.click()

time.sleep(15)
browser.quit()
