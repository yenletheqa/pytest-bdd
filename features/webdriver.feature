Feature: showing off webdriver basic features
  
  Scenario: start browsing
    Given we have a opened Chrome browser
    When we navigate to https://thecatapi.com/
    Then we should see the cat api logo