#!/bin/bash

cd ~/DataBase || exit

git pull origin lab_4

source venv/bin/activate
pip install -r requirements.txt

PID=$(sudo lsof -t -i:5000)
if [ -n "$PID" ]; then
  sudo kill -9 $PID
fi

nohup python3 app.py > app.log 2>&1 &

echo "Deployment finished!"
