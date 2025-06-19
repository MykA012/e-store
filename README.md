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
# Все URL
#### Условные обозначения:
Для удобства буду помечать url адреса уровнями защиты:
* public - может зайти любой пользователь
* protected - может зайти только авторизованый пользователь
* private - может зайти только админ

### Auth
* **POST** public - `/signup` - Регистрация с username, email и password
* **POST** public - `/login` - Вход по email и password

### Cart
* **GET** protected - `/cart` -Корзина пользователя
* **POST** protected - `/{product_slug}` - Добавить товар в корзину

### User
* **GET** protected - `/me` - Информация о пользователе
* **DELETE** protected - `/me` - Удалить аккаунт пользователя (cascade)
* **PATCH** protected - `/me/edit` - Редактировать информацию о пользователе
* **PATCH** protected - `/me/change-password` - Сменить пароль пользователя

### Products
* **GET** private - `/products/` - Все товары
* **POST** private - `/products/` - Добавить товар
* **GET** private - `/products/{product_id}` - Найти товар по id
* **PATCH** private - `/products/{product_id}` - Частично редактировать товар
* **PATCH** private - `/products/{product_id}` - Перезаписать товар
* **DELETE** private - `/products/{product_id}` - Удалить товар

### Categories
* **GET** private - `/categories/` - Все категории
* **POST** private - `/categories/` - Добавить категорию
* **GET** private - `/categories/{categories_id}` - Найти категорию по id
* **PATCH** private - `/categories/{categories_id}` - Частично редактировать категорию
* **PATCH** private - `/categories/{categories_id}` - Перезаписать категорию
* **DELETE** private - `/categories/{categories_id}` - Удалить категорию (cascade)

> Все пути прописаны относительно `http://localhost:8000`
---
# FAQ

### Как формируется slug товара/категории?
* Строка транслитерируется на английский с помощью  
библиотеки [Unidecode](https://pypi.org/project/Unidecode/)  
* Все символы приводятся в нижнему регистру
* Обрезаются пробелы по краям
* Пробелы заменяются на тире
> |      До               |         После          |
> |-----------------------|------------------------|
> |`Смартфоны и планшеты` | `smartfony-i-planshety`|
