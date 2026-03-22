# pulscen_project

Парсер каталога **Pulscen** на Python.

Проект предназначен для сбора данных о компаниях из каталога Pulscen по заданной категории и городу. В текущей версии основной рабочий сценарий использует **Selenium**, открывает страницы каталога, раскрывает номера телефонов и сохраняет результат в Excel.

## Что делает проект

Скрипт собирает информацию о компаниях из раздела каталога Pulscen:

- название компании
- ссылка на карточку компании
- адрес
- телефон

Результат сохраняется в Excel-файл.

## Стек

- Python
- Selenium
- pandas
- requests
- BeautifulSoup4
- lxml

## Структура проекта

```bash
pulscen_project/
├── README.md
├── chromedriver.exe
├── pulscen_bs.py
├── pulscen_parser.py
├── pulscen_selenium.py
└── test.py
