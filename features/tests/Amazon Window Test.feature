# Created by 17132 at 8/4/2022
Feature:Amazon Window Test

  Scenario: User can open and close Amazon applications
    Given Open Amazon T&C Page
    When  Store Original Windows
    And   Click On Amazon Applications Link
    And   Switch to the newly opened window
    Then  Verify your Amazon App Page is opened
    And   User Can Close New Window and Switch back to original


