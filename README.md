######Скопировать проект:
```
git clone https://github.com/dmtmalin/eastwood_test_task.git
cd eastwood_test_task
```
######Установить зависимости:
```
pip install django
pip install django-filter
```
######Установить компоненты:
`bower install`
######Создать бд "employees":
И проверить настройки подключения DATABASES в eastwood_test_task/settings.py
######Провести миграцию
`python manage.py migrate`
######Создать суперпользователя
`python manage.py createsuperuser`
######Запустить сервер
`python manage.py runserver`
