# Afraid Autologin

* Logs in freedns.afraid.org using USERNAME/PASSWORD from settings.py.
* Avoids account from being terminated due to inactivity (6 months).
* Run this script using cron every few months:
	`source bin/activate && python autologin.py`
* Uses firefox to go through the site. You may optionally install PhantomJS to use with the `--browser` flag.
* Can be run using a virtual display for headless systems by passing the `--headless` flag.

## Manual Set Up

To setup your virtualenv (once):

	$ cd afraid-autologin
	$ virtualenv venv

To use it:

	$ source venv/bin/activate
	$ pip install -r requirements.txt
	$ python autologin.py

## Docker
[Docker Hub](https://hub.docker.com/r/strenkml/afraid-autologin)
### Usage
#### docker-compose ([click here for more info](https://docs.linuxserver.io/general/docker-compose))
```yaml
---
version: "2.1"
services:
  afraid-autologin:
    image: strenkml/afraid-autologin
    container_name: afraid-autologin
    environment:
      - USERNAME=afraid_username
      - PASSWORD=afraid_password
```

#### CLI Usage
```bash
docker run -d \
  --name=afraid-login\
  -e USERNAME=afraid_username\
  -e PASSWORD=afraid_password\
  strenkml/afraid-autologin
```
### Parameters
| Parameter | Function |
| :----: | --- |
| `-e USERNAME=afraid_username` | Username for Afraid DNS |
| `-e PASSWORD=afraid_password` | Password for Afraid DNS |
