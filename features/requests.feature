Feature: showing off requests library

  Scenario: make a request
    Given we have a Cat Facts api: https://catfact.ninja/breeds
    When we make a GET request toward that API with param: limit = 2
    Then we validate that 200 returned with Abyssinian included in the body
