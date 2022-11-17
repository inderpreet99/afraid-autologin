FROM python:3.8-slim

SHELL ["/bin/bash", "-c"]
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y cron xvfb firefox wget
RUN wget -c https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz && tar -xzf geckodriver-v0.23.0-linux64.tar.gz -C /usr/local/bin/
RUN chown root:root /usr/local/bin/geckodriver

COPY afraid-cron /etc/cron.d/afraid-cron
RUN chmod 0644 /etc/cron.d/afraid-cron
RUN crontab /etc/cron.d/afraid-cron
RUN touch /var/log/cron.log

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install virtualenv
RUN virtualenv venv
RUN . /app/venv/bin/activate && pip3 install -r requirements.txt
COPY . .

RUN chmod +x entrypoint.sh

CMD ./entrypoint.sh
