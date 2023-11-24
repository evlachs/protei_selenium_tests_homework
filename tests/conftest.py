import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    # chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    yield driver
    driver.close()
