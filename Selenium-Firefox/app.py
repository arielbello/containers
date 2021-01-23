from flask import Flask
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

app = Flask(__name__)


@app.route("/")
def index():
    return '<p>You\'ve reached the basic <b>Selenium-Firefox</b> Container</p>'


@app.route("/run")
def scrape():
    """
    An example of using selenium
    """
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver_options.add_argument("--disable-extensions")
    with webdriver.Firefox(options=driver_options) as driver:
        driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        source = driver.page_source
        print(source[0:100])

    return '<h1 align="center"> The requested page: </h1>' + source


if __name__ == "__main__":
    app.run()
