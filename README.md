# Afraid Autologin

* Logs in freedns.afraid.org using USERNAME/PASSWORD from settings.py.
* Avoids account from being terminated due to inactivity (6 months).
* Run this script using cron every few months:
	`source bin/activate && python autologin.py`
* Uses firefox to go through the site. You may optionally install PhantomJS to use with the `--browser` flag.
* Can be run using a virtual display for headless systems by passing the `--headless` flag.

## Setting Up

To setup your virtualenv (once):

	$ cd afraid-autologin
	$ virtualenv venv

To use it:

	$ source venv/bin/activate
	$ pip install -r requirements.txt
	$ python autologin.py

