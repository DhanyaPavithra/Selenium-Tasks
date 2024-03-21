# Automation to fetch followers and following count from Guvi Instagram page using XPath:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# importing Exceptions:
from selenium.common.exceptions import NoSuchElementException


class GuviInstagram:

    def __init__(self,url):
        """
        Constructor to initialise the automation process to fetch the followers and following count

        """
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
    def boot(self):
        """
        Function to boot the webpage

        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def quit(self):
        """
        Function to quit / close the web browser
        :return:
        """
        self.driver.quit()

    def followersCount(self, key):
        return self.driver.find_element(by=By.XPATH, value=key).text

    def followingCount(self, key):
        return self.driver.find_element(by=By.XPATH, value=key).text

    def fetchdata(self):
        """
        Method to fetch the followers and following count from Guvi Instagram page

        """
        try:
            self.boot()
            print(self.followersCount('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button'))
            print(self.followingCount('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button'))

        except NoSuchElementException as e:
            print(e)

        finally:
            self.quit()

url = "https://www.instagram.com/guviofficial/"
obj = GuviInstagram(url)
obj.fetchdata()

