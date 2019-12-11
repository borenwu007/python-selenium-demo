#encoding=UTF-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import zipfile
import time 

link_path = '//*[@id="resource-list"]/li/label/a'
button_path = '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/button'

ip = 'proxy.wandouip.com'
port = 8090
username = 'borenwu@163.com'
password = '871120wbrW'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    }
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%(ip)s",
            port: %(port)s
          }
        }
      }
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "%(username)s",
            password: "%(password)s"
        }
    }
}
chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
)
""" % {'ip': ip, 'port': port, 'username': username, 'password': password}

# 会在本地创建一个manifest.json配置文件和background.js脚本来设置认证代理
# 运行代码后会生成proxy_auth_plugin.zip文件来保存当前配置

plugin_file = 'proxy_auth_plugin.zip'
with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)

prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'g:\\'}
chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_extension(plugin_file)

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://it.15kankan.com/info/toB792590')
time.sleep(3)



handle = browser.current_window_handle
browser.find_element_by_xpath(link_path).click()
handles = browser.window_handles

browser.switch_to_window(handles[-1])
elem = WebDriverWait(browser,30).until(lambda dirver:browser.find_element_by_xpath(button_path))
elem.click()
# cookie = browser.get_cookies()
# print(cookie)