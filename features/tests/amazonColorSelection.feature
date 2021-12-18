Feature: Amazon color selection
  Scenario Outline: color selection
    Given amazon page for <product> is open
    When user clicks on every color selection
    Then text for each color appears correctly

    Examples:
    |product|
    |jean|
    |sweater|