from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# importing exceptions:
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
# importing Action chains:
from selenium.webdriver.common.action_chains import ActionChains

class DragAndDrop:
    def __init__(self,url):
        """
        Constructor to initialise the drag and drop automation class.
        """
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver) # Action chain object for performing action chains

    def boot(self):
        """
        boot function to boot the webpage

        """
        self.driver.get(self.url) # to open the webpage
        self.driver.maximize_window()
        self.wait(5)

    def wait(self,secs):
        sleep(secs)

    def quit(self):
        """
        To close the web browser

        """
        self.driver.quit()

    def findElementsById(self, key):
        return self.driver.find_element(by=By.ID, value=key)

    def findElementByXPATH(self,value):
        return self.driver.find_element(by=By.XPATH, value=value)

    def dragAndDropFunction(self):
        """
        Method to perform Drag and drop actions

        """
        try:
            self.boot()
            self.wait(5)
            # To locate the source element
            source = self.findElementsById("draggable")
            # To locate the destination element
            destination = self.findElementsById("droppable")
            # To perform the drag and drop action
            self.action.drag_and_drop(source,destination).perform()
            self.wait(5)

            dropText = self.findElementByXPATH("/html/body/div[2]/p").text
            if dropText == "Dropped!":
                print(" Success")
            else:
                print("Error")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.wait(5)
            self.quit()

url = "https://jqueryui.com/droppable/#default"
obj = DragAndDrop(url)
obj.dragAndDropFunction()
