#!/bin/bash

# Переходимо в папку з проєктом
cd ~/DataBase || exit

# Завантажуємо останні зміни з гілки lab_4
git pull origin lab_4

# Встановлюємо/оновлюємо залежності
source venv/bin/activate
pip install -r requirements.txt

# Знаходимо і зупиняємо старий процес додатку, що слухає порт 5000
PID=$(sudo lsof -t -i:5000)
if [ -n "$PID" ]; then
  sudo kill -9 $PID
fi

# Запускаємо нову версію додатку у фоновому режимі
nohup python3 app.py > app.log 2>&1 &

echo "Deployment finished!"
