import logging

from pytest_bdd import scenario, given, when, then, parsers

from helpers.requests_helper import send_request

logger = logging.getLogger(__name__)


@scenario("requests.feature", "make a request")
def test_requests():
    pass


@given(parsers.cfparse("we have a Cat Facts api: {api}"))
def step_impl(context, api):
    context.api = api


@when(parsers.cfparse("we make a GET request toward that API with param: limit = {limit}"))
def step_impl(context, limit):
    headers = {'Accept': 'application/json'}
    params = {'limit': int(limit)}
    context.response = send_request(method='GET',
                                    url=f"{context.api}",
                                    headers=headers,
                                    params=params)


@then(parsers.cfparse("we validate that 200 returned with {breed} included in the body"))
def step_impl(context, breed):
    assert context.response.status_code == 200
    assert breed in context.response.text
