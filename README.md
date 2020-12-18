# Сокращение длины ссылок с помощью сервиса Битли

### Описание

В программу вводится любая ссылка. 
Далее идет два варианта развития событий:
1. Если вы ввели несокращенную ссылку, то программа выводит ее укороченную версию.
2. Если вы ввели сокращенную ссылку, то программа выводит кол-во кликов по ссылке за все время.

### Как установить

1. Заре зарегистрируйтесь на сайте [bitly.com](https://bitly.com).
Затем сгенерируйте токен ([сделать это можно тут](https://bitly.is/accesstoken)).
2. Создайте файл `.env` и положите свой токен в переменную `BITLY_TOKEN`.
3. Python3 должен быть уже установлен. 
 Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).