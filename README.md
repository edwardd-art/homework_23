# Домашнее задание #23

## Описание проекта
Проект интернет-магазина на Django с использованием PostgreSQL.

## Стек технологий
- Python 3.10+
- Django 4.2+
- PostgreSQL 15+
- psycopg2-binary
- python-dotenv
- Pillow
- IPython

## Установка и запуск

### 1. Клонировать репозиторий
git clone https://github.com/edwardd-art/homework_23.git
cd homework_23

### 2. Создать и активировать виртуальное окружение
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Настроить переменные окружения
Создайте файл .env в корне проекта:
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your-secret-key-here
DEBUG=True

### 5. Создать базу данных PostgreSQL
psql -U postgres

CREATE USER myuser WITH PASSWORD 'mypassword' CREATEDB;
CREATE DATABASE mydatabase OWNER myuser;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\q

### 6. Выполнить миграции
python manage.py makemigrations
python manage.py migrate

### 7. Создать суперпользователя
python manage.py createsuperuser

### 8. Загрузить тестовые данные
python manage.py load_test_data

### 9. Запустить сервер
python manage.py runserver

Админка: http://127.0.0.1:8000/admin/

## Модели данных

### Category (Категория)
- name - наименование
- description - описание

### Product (Продукт)
- name - наименование
- description - описание
- image - изображение
- category - категория (ForeignKey)
- price - цена
- created_at - дата создания
- updated_at - дата изменения

## Тестовые данные

### Категории
1. Электроника
2. Одежда
3. Книги
4. Дом и сад

### Продукты
1. Смартфон Galaxy S23 (Электроника) - 65 000 руб.
2. Ноутбук MacBook Pro (Электроника) - 120 000 руб.
3. Наушники Sony (Электроника) - 28 000 руб.
4. Футболка хлопковая (Одежда) - 1 500 руб.
5. Джинсы классические (Одежда) - 4 500 руб.
6. Куртка зимняя (Одежда) - 12 000 руб.
7. Python. Полное руководство (Книги) - 2 500 руб.
8. Садовый инвентарь (Дом и сад) - 3 500 руб.

## Автор
edwardd-art

## Дата
Июнь 2026 г.