#!/bin/sh

echo -e "\n\nInstalling and Running the web server\n\n"
python3 app.py &

sleep 5 ## Giving time for the server to get started


echo -e "\nKeeping the container running forever"
tail -f /dev/null