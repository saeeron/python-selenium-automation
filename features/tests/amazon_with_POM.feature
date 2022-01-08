Feature: testing amazon
  Scenario: Logged out user sees Sign in page when clicking Orders
   Given Open Amazon page
   When Click Amazon Orders link
   Then Verify Sign In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
   Given Open Amazon page
   When Click on cart icon
   Then Verify "Your Amazon Cart is empty" text present

  Scenario: selecting and retaining department during search
    Given Open Amazon page
    When Department electronics is selected
    And searching for external hard drive
    Then Correct electronics is retained

  Scenario: seeing New Arrivals deals on a product page
    Given Open product page B074TBCSC8
    When Hovering mouse over New Arrivals
    Then Deals appear


