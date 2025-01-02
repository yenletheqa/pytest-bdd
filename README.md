# pytest-bdd

Welcome to **pytest-bdd**! This project is designed to give an example of **pytest-bdd** and how it works with **requests** and **WebDriver** for automated testing. It demonstrates how to integrate behavior-driven development (BDD) tests using **Gherkin syntax** along with **Selenium WebDriver** for browser automation and **requests** for API testing.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Installation

To get started, you'll need Python 3.8+ and pip installed. Once you have those, follow these steps to install the required dependencies:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/project-name.git
    cd project-name
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Testing
```bash
pytest
```
This command will discover and run all tests in the tests folder. By default, it will look for files starting with test_ and ending with .py or files matching the Gherkin feature syntax in the features folder.

### Running Tests with Logging Output
```bash
pytest -s
```
This will allow print statements and logging output from your tests to be displayed in the terminal.

### Gherkin Terminal Reporter with Verbose Output
```bash
pytest  -v --gherkin-terminal-reporter
```
This command will display your test results in Gherkin format, making it easier to track test progress and results for each scenario.
