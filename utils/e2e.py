# functions for testing the game's flask service
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

chrome_service = Service('./chromedriver')
chrome_driver = webdriver.Chrome(service=chrome_service, options=options)


def test_scores_service(url):
    
    try:
        chrome_driver.get(url)

    except WebDriverException:
        print('Flask web server is not running')
        return -1

    else:
        whats_da_score = chrome_driver.find_element(By.XPATH, '//*[@id="score"]')
        value_as_int = int(whats_da_score.text)
        if 0 < value_as_int < 1001:
            return 0
        else:
            return -1


def main_function(url='http://localhost:8777/success'):
    
    web_service_test = test_scores_service(url)
    return web_service_test



if __name__ == '__main__':
    main_function()
