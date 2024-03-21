from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# importing exceptions
from selenium.common.exceptions import NoSuchWindowException
# importing Action chains
from selenium.webdriver.common.action_chains import ActionChains
# importing alerts
from selenium.webdriver.common.alert import Alert
# importing requests
import requests

class LaborGovWebpage:
    def __init__(self, url):
        """
        Constructor to create automation process in the webpage
        """
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # To perform actions
        self.action = ActionChains(self.driver)


    def boot(self):
        """
        To boot the webpage using url

        """
        self.driver.get(self.url)
        self.driver.maximize_window()

    def wait(self,secs):
        sleep(secs)

    def quit(self):
        """
        to quit the browser

        """
        self.driver.quit()

    def findElementByXpath(self, xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def labourGovPage(self):
        try:
            self.boot()
            self.wait(10)
            element= self.findElementByXpath('//*[@id="nav"]/li[7]/a')
            # to hover over an element:
            self.action.move_to_element(element).perform()
            self.wait(5)
            self.findElementByXpath('//*[@id="nav"]/li[7]/ul/li[2]').click()
            self.wait(5)
            self.findElementByXpath('/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
            self.wait(3)
            # to accept / decline alerts
            alert = Alert(self.driver)
            # accepting alert
            alert.accept()
            # to download the monthly progree report pdf
            janMonthlyReport = self.driver.current_url
            response = requests.get(janMonthlyReport)
            if response.status_code == 200:
                fileDownloadPath = "JanMonthlyProgressReport.pdf"
                f = open(fileDownloadPath, "wb")
                f.write(response.content)
                f.close()
            else:
                print("Error, Cannot download the Monthly progress report")

        except NoSuchWindowException as e:
            print(e)

        finally:
            self.quit()

url="https://labour.gov.in/"
obj=LaborGovWebpage(url)
obj.labourGovPage()


