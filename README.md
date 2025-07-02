# Запуск Проекта

### Создать файл .env
```
DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
DB_NAME=
DB_URL=postgresql+asyncpg://{}:{}@{}:{}/{} # for postgres with asyncpg
```
### Создать папку certs и там сгенерировать ключи
```bash
mkdir certs
cd certs

openssl genrsa -out jwt-private.pem 2048

openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem

cd ..
```

### Запуск
```shell
python -m src.main
```
---
# FAQ

### Как формируется slug товара/категории?
* Строка транслитерируется на английский с помощью  
библиотеки [Unidecode](https://pypi.org/project/Unidecode/)  
* Все символы приводятся в нижнему регистру
* Обрезаются пробелы по краям
* Пробелы заменяются на тире
> |           До          |          После         |
> |-----------------------|------------------------|
> |`Смартфоны и планшеты` | `smartfony-i-planshety`|
