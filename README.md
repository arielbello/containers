Docker Containers
=================
Here are some containers I'm playing around with.


Containers
-------

1. Flask \
    Lightweight python web framework based on Alpine Linux.

1. Selenium-Firefox \
    The most barebone version I could come up with of a selenium-based scraping \
    service. As the name suggests, it uses selenium with Firefox and therefore \
    geckodriver. This stack is comprised of:
    * Debian Linux (10-slim)
    * Python 3
    * Flask and Gunicorn
    * Selenium
    * Firefox browser and geckodriver

1. Selenium-Chrome \
    Same as above, but using Chrome instead of Firefox.


Credits
-------

* Selenium-Firefox packages a binary [geckodriver release]. \
Geckodriver is made available under the [Mozilla Public License].

* Selenium-Chrome Dockerfile is based on an example shown in this [article].

[geckodriver release]: https://github.com/mozilla/geckodriver/releases
[Mozilla Public License]: https://www.mozilla.org/en-US/MPL/2.0/
[article]: https://nander.cc/using-selenium-within-a-docker-container
