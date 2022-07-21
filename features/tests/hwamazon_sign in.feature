# Created by 17132 at 7/15/2022
Feature: Amazon Sign In Tests
  # Enter feature description here

  Scenario: Logged Out User Sees Sign In when Clicking on Returns & Order
    Given Open Amazon page
    When Clicking on returns and orders on Amazon
    Then Verify Sign in page opened, Sign In header is visible, email input field is present.
