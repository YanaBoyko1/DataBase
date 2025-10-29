# app/__init__.py

import os  # <-- ВАЖЛИВО: імпортуємо os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Ініціалізація об'єкта SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    Swagger(app)

    # --- ОНОВЛЕНИЙ БЛОК ПІДКЛЮЧЕННЯ ---

    # Отримуємо дані для підключення до БД зі ЗМІННИХ ОТОЧЕННЯ
    db_user = os.environ.get("MYSQL_USER")
    db_pass = os.environ.get("MYSQL_PASSWORD")
    db_host = os.environ.get("MYSQL_HOST")
    db_name = os.environ.get("MYSQL_DB")

    if not all([db_user, db_pass, db_host, db_name]):
        print("ПОМИЛКА: Не всі змінні оточення для БД встановлені!")

    # --- ЗМІНА ТУТ ---
    # Ми використовуємо 'mysql://' (для mysqlclient),
    # а не 'mysql+pymysql://'
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql://{db_user}:{db_pass}@{db_host}/{db_name}"
    )
    # --- КІНЕЦЬ ЗМІНИ ---

    # --- КІНЕЦЬ ОНОВЛЕНОГО БЛОКУ ---

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Ініціалізація бази даних
    db.init_app(app)

    # Імпорт та реєстрація маршрутів
    try:
        from app.my_project.auth.route.route import register_routes

        register_routes(app)
    except ImportError as e:
        print(f"ПОМИЛКА: Не вдалося імпортувати маршрути: {e}")

    return app
