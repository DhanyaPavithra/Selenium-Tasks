# visit url:www.saucedemo.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import requests

class VisitURL:

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, seconds):
        sleep(seconds)

    def inputDetails(self, value, key):
        self.driver.find_element(by=By.NAME, value=value).send_keys(key)
        self.sleep(5)

    def loginBtn(self):
        self.driver.find_element(by=By.ID, value="login-button").click()
        self.sleep(10)

    def fetchCurrentURL(self):
        current_url = self.driver.current_url
        print(current_url)

    def fetchTitle(self):
        title = self.driver.title
        print(title)
    def quit(self):
        self.driver.quit()

    def fetchContentsFromWebpage(self):
        page_content = self.driver.find_element(by=By.TAG_NAME, value="body").text
        with open("Webpage_task_11.txt","w") as file:
            file.write(page_content)

    def loginTo(self):
        self.boot()
        self.inputDetails("user-name", self.username)
        self.inputDetails("password", self.password)
        self.loginBtn()
        self.fetchCurrentURL()
        self.fetchTitle()
        self.fetchContentsFromWebpage()
        self.quit()


url ="https://www.saucedemo.com/"
obj = VisitURL(url, "standard_user", "secret_sauce")
obj.loginTo()




