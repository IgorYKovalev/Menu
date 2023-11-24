# Реализация древовидного меню

## Подключение 
1. Клонируйте репозиторий и перейдите в него в командной строке: https://github.com/IgorYKovalev/Menu.git
2. Установите виртуальное окружение: `python -m venv <название>`
3. Активируйте виртуальное окружение: `source venv/Scripts/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. В папке с файлом manage.py выполните миграции: `python manage.py migrate`
6. Создайте суперюзера, зайдите в админку: `python manage.py createsuperuser`
7. Запустите сервер: `python manage.py runserver`


### Основные библиотеки:
* [Django == 4.2.7](https://docs.djangoproject.com/) - основной фреймворк
* [django-mptt==0.15.0](https://pypi.org/project/django-mptt/) - пакет Django, который предоставляет расширение ORM для работы с деревьями экземпляров моделей. 

### Условия:

1) `+` Меню реализовано через template tag
2) `+` Хранится в БД.
3) `+` Редактируется в стандартной админке Django
4) `+` На отрисовку каждого меню требуется ровно 1 запрос к БД
