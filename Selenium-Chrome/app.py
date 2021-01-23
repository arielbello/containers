from selenium.webdriver.chrome.options import Options
from flask import Flask
from selenium import webdriver
import time

app = Flask(__name__)

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.

    Chrome options for headless browser is enabled.

    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}

    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

    return chrome_options


@app.route("/")
def index():
    return '<p>You\'ve reached the basic <b>Selenium-Chrome</b> Container</p>'


@app.route("/run")
def scrape():
    """
    An example of using selenium
    """
    chrome_options = (set_chrome_options())
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        source = driver.page_source
        print(source[0:100])

    return '<h1 align="center"> The requested page: </h1>' + source


if __name__ == "__main__":
    app.run()