# Refresh metadata script
Simple script using selenium to refresh metadata and create a log of unsuccessfull updates.

## Install
- You need to install the webdriver of your choice, I've used chrome. Go ahead and choose the one of your choice.

    - Chrome:	https://sites.google.com/chromium.org/driver/

    - Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

    - Firefox:	https://github.com/mozilla/geckodriver/releases

    - Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/


    After downloading you have to uncompress add it to your path more instruction can be found [here](https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/). Then you are ready to go. Just make sure it calls the webdriver before proceeding.

- install selenium (I highly recommend use virtualenv, which creates isolated virtual python environments, but it is up to you).
  - `pip install selenium`

## Locating Elements
To this task we need to find 2 things: the refresh metadata button and detect the toast that notifies the data has been refreshed.

Those informations can be retrieved using inspect from dev tools. You can locate elements based on ID, Name, XPATH etc.. more info can be found [here](https://selenium-python.readthedocs.io/locating-elements.html).






