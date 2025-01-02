import logging
import sys
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


# Add the root project directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

class Context:
    pass


@pytest.fixture(scope="session", autouse=True)
def context():
    """Create context variable to be shared across test steps."""
    return Context()


@pytest.fixture
def driver(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    yield context.driver
    context.driver.quit()


def pytest_configure(config):
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
