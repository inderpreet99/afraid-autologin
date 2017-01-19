#!/usr/bin/env python
from __future__ import print_function
from selenium import webdriver
import argparse
import os
import sys
import time
import random

try:
    from settings import USERNAME, PASSWORD, URL
    if USERNAME == "" or PASSWORD == "":
        raise ImportError
except ImportError:
    print("You need the username and password in the settings.py file:")
    print("USERNAME = 'my_username_here'")
    print("PASSWORD = 'my_password_here'")
    sys.exit(-1)


def main():

    parser = argparse.ArgumentParser(description=' \
        Logs in freedns.afraid.org using USERNAME/PASSWORD from settings.py. \
        Avoids account from being terminated due to inactivity (6 months).\
        Run this script using cron every few months:\
            source bin/activate && python autologin.py')

    parser.add_argument('--browser', default='firefox', help='browser name \
                        must be supported by selenium \
                        (options: firefox, phantomjs')

    parser.add_argument('--verbose', action='store_true',
                        help='show extra output')

    parser.add_argument('--headless', action='store_true', help='initialise a \
                        virtual display for headless systems')

    args = parser.parse_args()

    # init virtual display, if required
    if args.headless:
        from pyvirtualdisplay import Display
        
        display = Display(visible=0, size=(1366, 768))
        display.start()

    # setup browser
    if args.browser == 'phantomjs':
        browser = webdriver.PhantomJS()
    else:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        # profile.set_preference("javascript.enabled", False)
        browser = webdriver.Firefox(firefox_profile=profile)

    browser.get(URL)
    time.sleep(random.randint(1,3))

    # go to login page
    browser.find_element_by_link_text("Domains").click()
    time.sleep(random.randint(1,3))

    # fill in login details
    username_field = browser.find_element_by_name('username')
    password_field = browser.find_element_by_name('password')
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    browser.find_element_by_name('submit').click()
    time.sleep(random.randint(1,3))

    # view the subdomains
    browser.find_element_by_link_text("Subdomains").click()

    browser.quit()

if __name__ == "__main__":
    main()
