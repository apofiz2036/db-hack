# db-hack

Файл предназначен для взлома и изменения данных в базе данных электронного журнала. Для работы скриптов требуется развернуть сайт. Для работы требуется сделать слудующее:

1. скачать файл и положить его в папку datacenter.
2. Ввест в консоль команду: python manage.py shell.
3. Выбрать нужный скрип и прописать команду в консоль, например: from datacenter.scripts import create_commendation.
4. Вызвать скрипт с необходимыми аргументами, например: create_commendation('Иванов Иван', 'Физкультура')

Всего в файле находится 3 скрипта, fix_marks, remove_chastisements и create_commendation.

## Скрипт fix_marks
Скрипт позволяет исправить все оценки 2 и 3 на 5 выбранного ученика. Для запуска скрипта на четвёртом шаге нужно прописать: fix_marks('Имя ученика'). Если такой ученик отсутствует то будет выведено сообщение "Ученик не существует". Если будет найдено несколько учеников то будет выведено сообщение "Найдено несколько учеников с именем".

## Скрипт remove_chastisements
Скрипт позволяет удалить все негативные замечания выбранного ученика. Для запуска скрипта на четвёртом шаге нужно прописать: remove_chastisements('Имя ученика'). Если такой ученик отсутствует то будет выведено сообщение "Ученик не существует". Если будет найдено несколько учеников то будет выведено сообщение "Найдено несколько учеников с именем".

## Скрипт create_commendation
Скрипт позволяет добавлять похвалу выбранному ученики по выбранному предмету. Для запуска скрипта на четвёртом шаге нужно прописать: create_commendation('Имя ученика', 'Название предмета'). Если такой ученик отсутствует то будет выведено сообщение "Ученик не существует". Если будет найдено несколько учеников то будет выведено сообщение "Найдено несколько учеников с именем". Если такого предмета не существует то будет выведено сообщение "Такого предмета не существует".