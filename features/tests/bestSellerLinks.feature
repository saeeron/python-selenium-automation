Feature: Amazon bestseller and Customer Service
  Scenario: check the number of links on amazon bestseller
    Given Open Amazon website
    And Navigate to best sellers
    Then there are 5 links on the top panel

  Scenario: all elements in Customer Services' UI are present
    Given Navigate to customer service
    Then UI elements are present
