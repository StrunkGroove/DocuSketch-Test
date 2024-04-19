# Task
Создать docker-compose.yml разворачивающий приложение на python с простой реализацией REST API. Решение должно состоять из двух контейнеров:
- Любая NoSQL DB.
- Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.
- Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.
- Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.

# For start:
### Create .env and set:
```
REDIS_PASSWORD=STRONG_PASSWORD
REDIS_PORT=6379
REDIS_DATABASES=1

FLASK_APP=main.py
```

### Start:
docker-compose up --build
