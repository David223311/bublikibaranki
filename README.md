# Сокращение URL-адресов Bitly
Сокращение URL-адресов Bitly - это крутой проект, который позволит вам сокращать длинные ссылки и узнавать количество переходов по уже сокращенным ссылкам.

## Как установить
Скачайте необходимые файлы, затем используйте pip (или pip3 , если есть конфликт с Python2) для установки
зависимостей и установить зависимости.

```
pip install -r requirements.txt
``` 

## Пример запуска скрипта

Для запуска скрипта у вас уже должен быть установлен Python3.
Для получения сокращенной ссылки, необходимо написать команду в таком формате:
```
python main.py --url https://translate.google.ru
```

## Как получить токен
На сайте [Bitly](https://bitly.com/) вы получите строку наподобие такой:

BITLY_TOKEN = `17c09e20ad155405123ac1977542fecf00231da7`.

Это будет ваш токен.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org)
