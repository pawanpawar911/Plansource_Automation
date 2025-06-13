# UI Test Automation Framework

This is a modular and scalable Python-based UI test automation framework designed for web application testing. It follows the Page Object Model (POM) design pattern and integrates configuration management, logging, reporting, and utilities to ensure easy maintenance and high reusability.

---

## 📁 Project Structure

```
.
├── base_pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── employees_page.py
│   └── login_page.py
│
├── configuration/
│   └── config.ini
│
├── logs/
│   └── test.log
│
├── reports/
│   ├── assets/
│   └── plansource_report.html
│
├── test_pages/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_login_page.py
│
├── utilities/
│   ├── __init__.py
│   ├── customLogger.py
│   ├── locators.py
│   └── read_properties.py
```

---

## 🚀 Features

- **Page Object Model (POM)**: Organized page interaction logic in `base_pages`.
- **Test Configuration**: Centralized settings via `config.ini`.
- **Logging**: Real-time logging with logs saved in `logs/test.log`.
- **HTML Reports**: Auto-generated test execution reports in `reports`.
- **Utilities**: Common utilities like custom loggers and property readers in `utilities`.
- **Pytest Support**: Tests defined using `pytest` framework with `conftest.py` for fixtures.

---

## 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Install Dependencies**

Make sure you have Python 3.x installed, then run:

```bash
pip install -r requirements.txt
```

3. **Update Configuration**

Edit `configuration/config.ini` with your environment details.

4. **Run Tests**

```bash
pytest test_pages/ --html=reports/plansource_report.html --self-contained-html
```

---

## 📜 Test Example

Test file `test_login_page.py` contains sample login page test cases using POM classes.

---

## 📂 Reports and Logs

- **Logs**: `logs/test.log` contains all test run logs.
- **Reports**: `reports/plansource_report.html` shows test execution results with screenshots and details.

---

## 🧰 Utilities

- `customLogger.py`: Sets up custom logging.
- `locators.py`: Stores reusable element locators.
- `read_properties.py`: Reads data from configuration files.

---

## 🧪 Test Framework

This project uses:

- `pytest` for test execution
- `selenium` or `pywinauto` (assumed based on usage)
- `logging` for logs
- `configparser` for reading `.ini` files
- `pytest-html` for reports

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
