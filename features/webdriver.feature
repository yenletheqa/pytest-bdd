Feature: showing off webdriver basic feature
  
  Scenario: start browsing
    Given we have a opened Chrome browser
    When we navigate to https://thecatapi.com/
    Then we should see the cat api logo