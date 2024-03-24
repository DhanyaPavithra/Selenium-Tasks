# Automation in IMDB search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# importing waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# importing action chains
from selenium.webdriver import ActionChains

# importing exceptions
from selenium.common.exceptions import *

# importing select:
from selenium.webdriver.support.ui import Select

class IMDB:
    def __init__(self,url):
        """
        Constructor for initialising the automation.

        Arguments:
            driver: WebDriver object for interacting with the browser.
            url : The URL of the web page to be automated.

        """
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)
        # Implementation of explicit wait
        self.wait = WebDriverWait(self.driver, 15)
        # Implementation of Implicit waits
        self.driver.implicitly_wait(15)


    def boot(self):
        """
        To boot the webpage with the url

        """
        self.driver.get(self.url)
        # explicit waits
        self.wait.until(EC.url_to_be(self.url))
        self.driver.maximize_window()

    def quit(self):
        """
        To quit the webpage

        """
        self.driver.quit()


    def findElementbyXpath(self, xpath):
        """
        Function to locate the element using Xpath

        """
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def findElementByID(self, id):
        """
        Function to locate the element using ID

        """
        return self.driver.find_element(by=By.ID, value=id)

    def selectFromDropDown(self,id, value):
        """
        Function to perform in Dropdown
        """
        dropdown_element = self.driver.find_element(by=By.ID, value=id)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(value)

    def search(self):
        self.boot()

        try:
            # Expanding all options
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button'))).click()
            # finding and sending data to input box
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input'))).send_keys("Tom")
            # Selecting in DropDown box
            self.wait.until(EC.element_to_be_clickable((By.ID,"within-topic-dropdown-id")))
            self.selectFromDropDown("within-topic-dropdown-id","Quotes")
            # Clicking the options
            self.wait.until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "accordion-item-pageTopicsAccordion"] / div / div / section / button[9]')))
            # Clicking to see the result
            self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button'))).click()
            # printing the result page url
            print(self.driver.current_url)
        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()

url = "https://www.imdb.com/search/name/"
obj = IMDB(url)
obj.search()





