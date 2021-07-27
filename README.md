# Garpix Instagram

Пакет интеграции с instagram.com

## Быстрый старт

Установка:

```bash
pip install garpix_instagram
```

Добавьте `garpix_instagram` в `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'garpix_instagram',
]
```

Также, добавьте переменные окружения (файл `.env`) значениями, полученными от profitbase.ru:

```bash
INSTAGRAM_USERNAME=???
INSTAGRAM_PASSWORD=???
```

Также, в settings.py необходимо добавить миксины:

```bash
GARPIX_INSTAGRAM_POST_MIXIN = 'garpix_instagram.models.empty_mixin.EmptyMixin'
```


## Использование

Для получения данных от инстаграма используйте следующую manage.py команду:

```
python3 backend/manage.py start_inst
```

## Дополнительно
Может потребоваться команда
```
sudo apt install firefox-geckodriver
```
# Changelog

Смотри [CHANGELOG.md](CHANGELOG.md).

# Contributing

Смотри [CONTRIBUTING.md](CONTRIBUTING.md).

# License

[MIT](LICENSE)

---

Developed by Garpix / [https://garpix.com](https://garpix.com)