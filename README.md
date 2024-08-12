# DRF_KW_TRACKER
# Приложение для напоминаний о полезных привычках
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
## Что дает: 
Реализации советов из книги Джеймса Клира «Атомные привычки» через Телеграм
## Технологии:
- python 3.12
- SQL
- django 5.0.6
- PostgreSQL
- DRF
- Telegram
- Celery 
- GitHub
- Redis
- Docker

## Запуск проекта с использованием Docker

1. Убедитесь, что у вас установлены Docker и Docker Compose.

2. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

3. Создайте файл .env в корневой директории проекта и настройте переменные окружения.

4. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```
5. Примените миграции:

```bash
docker-compose exec web python manage.py migrate
```
6. Проект будет доступен по адресу http://localhost:8000

## Остановка проекта

Для остановки проекта выполните:

```bash
docker-compose down
```