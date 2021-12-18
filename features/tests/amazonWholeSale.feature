Feature: Amazon color selection
  Scenario: wholesale regular prices
    Given amazon wholesale page is open
    Then there are regular prices under every item
    And there are product names under every item