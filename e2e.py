import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_scores_service(url):

    try:

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        #service = Service("C:/Users/LENOVO/Desktop/CHMD/chromedriver-win64/chromedriver.exe")
        #service = Service("C:/Users/LENOVO/OneDrive/Desktop/Crm_Driv/chromedriver-win64/chromedriver.exe")
        service = Service("C:/Users/LENOVO/OneDrive/Desktop/NCRM/chromedriver-win64/chromedriver.exe") #latest chrome version
        driver = webdriver.Chrome(service=service, options=options)


        driver.get(url)


        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)


        driver.quit()
        return 1 <= score <= 1000
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main_function():

    #url="localhost:5000/score"
    url = "http://127.0.0.1:5000/score"
    url = "http://127.0.0.1:5000/score"
    result = test_scores_service(url)
    if result:
        print("Test passed!")
        return 0
    else:
        print("Test failed!")
        return -1


if __name__ == "__main__":
    exit(main_function())
