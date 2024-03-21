from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# importing exceptions
from selenium.common.exceptions import NoSuchWindowException
# importing Action chains
from selenium.webdriver.common.action_chains import ActionChains


class CowinWebpage:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def wait(self,secs):
        sleep(secs)

    def quit(self):
        self.driver.quit()

    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def cowin(self):
        try:
            # booting the webpage using url
            self.boot()
            self.wait(5)
            # opening second tab:
            self.findElementByXpath('//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a').click()
            self.wait(5)
            # switching to the home page
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.wait(5)
            # opening third tab:
            self.findElementByXpath('//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
            self.wait(5)
            # switching to tab:
            self.driver.switch_to.window(self.driver.window_handles[1])
            print(self.driver.current_window_handle)
            print(self.driver.title)
            self.wait(5)
            self.driver.close()
            # switching to tab:
            self.driver.switch_to.window(self.driver.window_handles[1])
            print(self.driver.current_window_handle)
            print(self.driver.title)
            self.wait(5)
            self.driver.close()
            self.wait(5)
        except NoSuchWindowException as e:
            print(e)
        finally:
            self.quit()

url = "https://www.cowin.gov.in/"
obj = CowinWebpage(url)
obj.cowin()




