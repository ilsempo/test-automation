# Test-Automation

Small, self-contained demo project that shows how to write **browser end-to-end tests with Python, Selenium and Pytest**.  
It exercises a sample e-commerce site (the famous *saucedemo.com*) and tries to demonstrate clean, readable test code through:

* **Step definitions** – high-level reusable actions kept under `steps/`.
* **Externalised data & locators** – YAML files in `data/` so tests stay free of XPaths and magic strings. 
* **Very short test scripts** – scenario-style tests that read almost like English in `tests/`.

---

## Quick start

### 1. Requirements
* Python ≥ 3.10
* Selenium ≥ 4.27.1
* Pytest ≥ 8.4.0
* Pyyaml ≥ 6.0.2
* Google Chrome or Firefox installed locally

### 2. Install

```bash
git clone https://github.com/ilsempo/test-automation.git
cd test-automation
python -m venv .venv
source .venv/bin/activate          # Windows → .venv\Scripts\activate
pip install -r requirements.txt    # installs Selenium and pytest
```
### 3. Project structure
```graphql
.
├── data/                   # YAML with users, locators, expected texts
│   ├── data.yaml
│   └── website.yaml
├── steps/                  # High-level reusable actions & assertions
│   ├── action_steps.py
│   ├── navigation_steps.py
│   └── validation_steps.py
├── tests/                  # Very short scenario files marked with @pytest.mark
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_buying.py
├── utils/                  # Helpers (logging decorator, YAML loader, etc.)
├── conftest.py             # Global fixtures – mainly the WebDriver factory
├── requirements.txt
└── pytest.ini
````
### 4. Runing tests
To run the tests, you can use the various tags located above each test in the `tests/` folder.
There are three ways to run them: by individual test, by group of tests, or with the `regression` tag, which runs all the tests.
#### Feature test example:
```python
@pytest.mark.regression
@pytest.mark.login
class TestLogin:

    @pytest.mark.login_valid
    def test_login_valid(self):
        """
        Scenario: User logs in successfully
        """
        login()

    @pytest.mark.login_invalid
    def test_login_invalid(self):
        """
        Scenario: Locked user fails logging in
        """
        login("locked")
    
    @pytest.mark.login_logout
    def test_user_logs_in_and_out(self, driver):
        """
        Scenario: User logs in and out
        """
        login()
        user_clicks("item_name")
        logout()
```
For example, to run the test for the `User logs in successfully scenario`, you could use:
```bash
pytest -m login_valid              # if you want to see the browser UI running the test
pytest -m login_valid -H           # if you want to run the test in headless mode
pytest -m login_valid -B firefox   # if yo want to run the test in Firefox (default Chrome)
```
If you use `login` tag , all the tests under `login` tag will run, and if `regression` is used, all the written tests will run.
### 5. Writting tests
The idea is to group by "Features" as in Gherkin, depending on what part of the page is being tested.
You can use different types of steps (action, navigation, or validation) to write a test.
If a new test is added to an existing "Feature", it should simply be written inside the class and assigned a new tag (which must also be defined in `pytest.ini` under the `markers` section).
Steps are functions that contain their logic inside the `steps/` folder. The available ones are:
#### Action steps
* add_products_to_cart
* fill_form_with_data
* logout
* user_clicks
* user_sorts_by
#### Navigation steps
* go_to_cart
* finish_checkout
* login
* user_access_page
#### Validation steps
* page_loads
* message_is_displayed
* user_is_in_page
* element_is_present_in_page
* new_tab_appears
* validate_external_url
### 6. Locators and data
To keep the code clean, elements such as XPATHs, login credentials, messages, external URLs, etc., are stored in the `website.yaml` and `data.yaml` files, respectively. These can be accessed using functions like `get_xpath`, `get_message`, or `get_user_info`.
### 7. Adding new steps
If you want to add new steps, you must first define what type of step it is (validation, navigation, or action). Then, within the corresponding steps file, you can define the function and build the logic for the new step.
### 8. Logging
There is currently a dedicated logging file that provides more informative logs depending on the type of step. This is handled in the `log_handler.py` file.
Every time a test is executed, it goes through a wrapper that calls a function named `logging_adjustments`, which checks if the step is included in the `step_handlers` dictionary.
If the step is found there, the function containing the custom log for that step is executed; otherwise, the default logging is used.