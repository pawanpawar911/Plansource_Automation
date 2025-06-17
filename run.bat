pytest -rA .\test_pages\test_login_page.py --html="./reports/plansource_report.html" --alluredir="./reports/plansource"
allure serve "./reports/plansource"