# Активность пользователей GitHub

[![English](https://img.shields.io/badge/English-blue?style=for-the-badge)](../README.md)
![Russian](https://img.shields.io/badge/Русский-red?style=for-the-badge)

## Описание

Этот проект вдохновлен [roadmap.sh](https://roadmap.sh/projects/github-user-activity).

## Установка

> Заметка: Шаги для установки предоставлены только для системы Windows.

1. Клонируй репозиторий:
    
    ```shell
    git clone https://github.com/IliaStarchevus/GitHubActivity.git
    ```

2. Установи зависимости:
    
    ```shell
    pip install -r requirements.txt
    ```

3. Добавь путь к `ghact.py` в переменные среды своей системы.
   1. Нажми `Ctrl + R` и введи `sysdm.cpl`.
   2. Нажми кнопку `Дополнительно` сверху и выбери `Переменные среды`.
   3. Добавь путь к `ghact.py` в `Path` в переменных среды пользователя.
   4. Добавь `.PY` в `PATHEXT` в переменных системы.

4. Проверь работу программы:

    ```shell
    ghact -h
    ```