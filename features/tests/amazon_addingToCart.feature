Feature: Testing amazon adding to cart

  Scenario: picking a random item and check if it is added to cart
    Given Open Amazon page
    When searching for scarfs for women
    And adding a random item to cart
    Then cart indicates 1 item(s)

