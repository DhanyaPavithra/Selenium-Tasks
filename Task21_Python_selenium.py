from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Login:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(5)

    def wait (self, secs):
        sleep(5)

    def quit(self):
        self.driver.quit()

    def inputDetails(self, value, key):
        self.driver.find_element(by=By.NAME, value=value).send_keys(key)
        self.wait(5)

    def loginBtn(self):
        self.driver.find_element(by=By.ID, value="login-button").click()
        self.wait(5)

    def getCookies(self):
        return self.driver.get_cookies()


url ="https://www.saucedemo.com/"
obj = Login(url)
obj.boot()
print(obj.getCookies())
obj.inputDetails(value="user-name", key="standard_user")
obj.inputDetails(value="password", key="secret_sauce")
obj.loginBtn()
print(obj.getCookies())
obj.quit()


