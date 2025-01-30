# Unit Converter

Проект **Unit Converter** — это веб-приложение, созданное с использованием Flask, которое позволяет конвертировать единицы измерения длины, веса и температуры. Приложение предоставляет простой и интуитивно понятный интерфейс для выполнения конвертаций.
Этот pet-проект разработан в рамках учебного процесса и взят с платформы [roadmap.sh](https://roadmap.sh/projects/unit-converter).

---

## Структура проекта

Проект состоит из следующих файлов:

### `app.py`
Основной файл приложения на Flask. Содержит логику конвертации и маршруты для обработки запросов.

### `templates/`
Папка с HTML-шаблонами для отображения страниц.

- **`index.html`**: Главная страница для конвертации длины.
- **`weight.html`**: Страница для конвертации веса.
- **`temperature.html`**: Страница для конвертации температуры.
- **`result.html`**: Страница с результатом конвертации.

### `requirements.txt`
Файл с зависимостями проекта

---

## Установка и запуск

### Требования
- Python 3.x
- Flask

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/unit-converter.git
   cd unit-converter
   ```

2. Установите зависимости:
   ```bash
   pip install Flask
   ```

3. Запустите приложение:
   ```bash
   python app.py
   ```

4. Откройте браузер и перейдите по адресу:
   ```
   http://127.0.0.1:5000
   ```

---

## Описание функциональности

### Конвертация длины
- Поддерживаемые единицы: миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, мили.
- Пример: конвертация 10 метров в футы.

### Конвертация веса
- Поддерживаемые единицы: миллиграммы, граммы, килограммы, унции, фунты.
- Пример: конвертация 500 граммов в унции.

### Конвертация температуры
- Поддерживаемые единицы: градусы Цельсия, Фаренгейта, Кельвина.
- Пример: конвертация 25 градусов Цельсия в Фаренгейты.

---

## Примеры использования

### Конвертация длины
1. Перейдите на главную страницу (`/`).
2. Введите значение, например, `10`.
3. Выберите единицу измерения "из" (например, `meter`) и "в" (например, `foot`).
4. Нажмите "Convert".
5. На странице результата вы увидите: `10 meter = 32.8084 foot`.

### Конвертация температуры
1. Перейдите на страницу температуры (`/temperature`).
2. Введите значение, например, `25`.
3. Выберите единицу измерения "из" (например, `celsius`) и "в" (например, `fahrenheit`).
4. Нажмите "Convert".
5. На странице результата вы увидите: `25 celsius = 77 fahrenheit`.

---

   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unit Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #444;
            padding: 10px 0;
        }
        nav a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            margin: 0 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        nav a:hover, nav a.active {
            background-color: #555;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .container h2 {
            margin-bottom: 20px;
        }
        .input-group {
            margin-bottom: 15px;
        }
        .input-group label {
            display: block;
            margin-bottom: 5px;
        }
        .input-group input, .input-group select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .input-group button {
            width: 100%;
            padding: 10px;
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .input-group button:hover {
            background-color: #555;
        }
    </style>
</head>
<body>

<header>
    <h1>Unit Converter</h1>
</header>

<nav>
    <a href="/" class="active">Length</a>
    <a href="/weight">Weight</a>
    <a href="/temperature">Temperature</a>
</nav>

<div class="container">
    <h2>Enter the length to convert</h2>
    <form action="/convert" method="POST">
        <div class="input-group">
            <label for="value">Value:</label>
            <input type="number" id="value" name="value" placeholder="Enter value" required>
        </div>
        <div class="input-group">
            <label for="from">Unit to convert from:</label>
            <select id="from" name="from" required>
                <option value="millimeter">Millimeter</option>
                <option value="centimeter">Centimeter</option>
                <option value="meter">Meter</option>
                <option value="kilometer">Kilometer</option>
                <option value="inch">Inch</option>
                <option value="foot">Foot</option>
                <option value="yard">Yard</option>
                <option value="mile">Mile</option>
            </select>
        </div>
        <div class="input-group">
            <label for="to">Unit to convert to:</label>
            <select id="to" name="to" required>
                <option value="millimeter">Millimeter</option>
                <option value="centimeter">Centimeter</option>
                <option value="meter">Meter</option>
                <option value="kilometer">Kilometer</option>
                <option value="inch">Inch</option>
                <option value="foot">Foot</option>
                <option value="yard">Yard</option>
                <option value="mile">Mile</option>
            </select>
        </div>
        <div class="input-group">
            <button type="submit">Convert</button>
        </div>
    </form>
</div>

</body>
</html>

