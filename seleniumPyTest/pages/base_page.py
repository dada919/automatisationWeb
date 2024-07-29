class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)
