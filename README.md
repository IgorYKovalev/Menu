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
2) `-` Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) `+` Хранится в БД.
4) `+` Редактируется в стандартной админке Django
5) `-` Активный пункт меню определяется исходя из URL текущей страницы
6) `-` Меню на одной странице может быть несколько. Они определяются по названию.
7) `-` При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) `+` На отрисовку каждого меню требуется ровно 1 запрос к БД
