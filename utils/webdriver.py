from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver:
    def get_driver(self):
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))