# weather_app
Тестовое задание o-complex

Было выполнено:
- сделаны автодополнение (подсказки) при вводе города

Был использован плагин КЛАДР https://github.com/fias-api/jquery для получения списка всех городов России и автодополнения. API сервиса https://locationiq.com/ для получения значений долготы и широты по названию города.
Основной стек: Django, jQuery, Bootstrap5

Для запуска приложения нужен python 3.12.3 и установленные пакеты:
- Django              4.2.14
- django-bootstrap-v5 1.0.11
- numpy               2.0.0
- openmeteo_requests  1.2.0
- pandas              2.2.2
- requests            2.32.3
- requests-cache      1.2.1
- retry-requests      2.0.0

Для запуска приложения нужно выполнить команду **django-admin startproject weather**, затем из папки проекта выпольнить **python manage.py startapp get_weather**, скопировать файлы в папку get_weather и запустить командой **python manage.py runserver**
