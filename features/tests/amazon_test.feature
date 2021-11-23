# Created by saeed at 11/21/21
Feature: Tests for amazon search
  # Enter feature description here


  # they are not case-sensitive
  Scenario: Use can search for products
    Given Open amazon page
    When search for table
    And click search icon
    Then Search results have table
