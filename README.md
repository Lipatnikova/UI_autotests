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
7. 2. Run the tests with Options `pytest -v -s --browser_name=firefox`.
7. 3. Run the tests by GRID `pytest -s -v --browser_name=chrome --grid_address=http://ХХХ.ХХХ.Х.ХХХ:4444/wd/hub`
7. 4. Run the tests with generated Allure report `pytest -s -v --alluredir=allure-results`
8. View Allure report `allure serve allure-results`.
9. Run the script to execute only the failed test cases from the previous run with generated Allure report `.\run_last_failed_tests.sh`
10. Run tests in multithreading mode use: run_tests_grid.bat and run_tests_grid.sh.
#### Options:
- --browser_name: is optional, browser name (chrome | firefox | edge), default=chrome
- --hub_address: is optional, specify remote executor URL, if set executes remotely
- --lf (or --last-failed), is optional, running only failed test cases from the previous runs tests
