# 1. Використовуємо офіційний базовий образ Python 3.9
FROM python:3.9-slim

# 2. Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# 3. Копіюємо файл із залежностями
COPY requirements.txt .

# 4. Встановлюємо залежності ОС, Python-пакети І ОДРАЗУ ЧИСТИМО
#    Це "важкий" крок, який робить все в одній інструкції (RUN),
#    щоб зберегти розмір образу малим.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    pkg-config \
    libmariadb-dev && \
    \
    # Тепер запускаємо pip, коли в нас є компілятор
    pip install --no-cache-dir -r requirements.txt && \
    \
    # Видаляємо компілятор та бібліотеки, які більше не потрібні
    apt-get purge -y --auto-remove gcc pkg-config libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

# 5. Копіюємо решту коду твого проекту
COPY . .

# 6. Вказуємо порт (зміни, якщо потрібно)
EXPOSE 5000

# 7. Команда для запуску (переконайся, що в app.py є host='0.0.0.0')
CMD ["python", "app.py"]