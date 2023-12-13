#!/bin/bash
printenv >> /etc/environment

# Run the script once initially to ensure everything is working
bash -c "PATH=$PATH:/usr/local/bin/; source /app/venv/bin/activate && python /app/autologin.py --headless"

cron && tail -f /var/log/cron.log