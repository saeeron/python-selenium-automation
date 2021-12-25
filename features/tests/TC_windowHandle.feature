# Created by saeed at 12/24/21
Feature: Amazon TC window handling
  Scenario: User can open and close Amazon Privacy Notice
    Given Amazon T&C page is open
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original
