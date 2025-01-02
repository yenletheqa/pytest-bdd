import requests
import logging

logging = logging.getLogger(__name__)


def log_request_details(request: requests.PreparedRequest):
    """
    Logs the full details of an HTTP request.
    """
    logging.info("\n")
    logging.info("=== REQUEST DETAILS ===")
    logging.info(f"URL: {request.url}")
    logging.info(f"Method: {request.method}")
    logging.info(f"Headers: {request.headers}")
    logging.info(f"Body: {request.body}")
    logging.info("=======================")


def log_response_details(response: requests.Response):
    """
    Logs the full details of an HTTP response.
    """
    logging.info("=== RESPONSE DETAILS ===")
    logging.info(f"Status Code: {response.status_code}")
    try:
        logging.info(f"Body: {response.json()}")
    except ValueError:
        logging.info(f"Body: {response.text}")
    logging.info("=======================")


def send_request(method: str, url: str, **kwargs) -> requests.Response:
    """
    Sends an HTTP request and logs the details.

    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE, etc.).
        url (str): The endpoint URL.
        **kwargs: Additional arguments for the request.

    Returns:
        requests.Response: The HTTP response.
    """
    session = requests.Session()
    request = requests.Request(method, url, **kwargs)
    prepared = session.prepare_request(request)

    # Log the request details
    log_request_details(prepared)
    response = session.send(prepared)

    # Log the response details
    log_response_details(response)

    return response
