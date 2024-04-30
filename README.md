# UI_autotests

## How to work with a repository on your PC:
1. Clone the repository: git clone "Clone using the web URL".
2. Navigate to the project directory.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment: 
5. For Windows: `venv\Scripts\activate.bat`. 
6. For Linux and macOS: `source venv/bin/activate`.
5. Install the required dependencies: `pip install -r requirements.txt`.
6. Run the tests:
7. 1. Run the tests use the command `pytest -s -v`.
7. 2. Run the tests with Options `pytest -v -s --browser_name firefox`.
7. 3. Run the tests with generated Allure report `pytest -s -v --alluredir allure-results`
8. View Allure report `allure serve allure-results`.
9. Run the script to execute only the failed test cases from the previous run with generated Allure report `.\run_last_failed_tests.sh`
#### Options:
- --browser_name: is optional, browser name (chrome | firefox), default=chrome
- --lf (or --last-failed), is optional, running only failed test cases from the previous runs tests
