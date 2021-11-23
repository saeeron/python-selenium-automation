
Feature: Tests for amazon

  Scenario: Searching for Cancel Items or Orders
    Given Open Amazon costumer service
    When Search for cancel order
    And click Enter
    Then We see Cancel Items or Orders

  Scenario: Seeing sign-in page when ordering
    Given Open Amazon website
    When Browse Orders
    Then We see Sign-In page
