# Basic script to open schwab.com in a remote chrome browser with python and selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_ID = ""
PWD = ""


def get_head_driver() -> webdriver.Chrome:
    """
    Get a local driver with the remote debugging port enabled.
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    return webdriver.Chrome(
        service=Service(executable_path="chromedriver"), options=chrome_options
    )


def login(driver: webdriver.Chrome):
    """
    Login to schwab.com with the given credentials.
    """
    try:
        driver.get("https://client.schwab.com/Areas/Access/Login/")
        print(driver.current_url)

        # look for the login form and fill it out
        driver.switch_to.frame(
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "lmsIframe"))
            )
        )
        username = driver.find_element(By.ID, "loginIdInput")
        username.send_keys(LOGIN_ID)
        password = driver.find_element(By.ID, "passwordInput")
        password.send_keys(PWD)

        # Wait until the element is clickable
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
        element.click()

        # Handle two-step authentication if applicable

    except Exception as e:
        print("Exception:", e)
        driver.close()


if __name__ == "__main__":
    driver = get_head_driver()
    login(driver)
    # pause
    time.sleep(60)
    exit(0)
