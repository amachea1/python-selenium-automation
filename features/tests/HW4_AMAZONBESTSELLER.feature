# Created by 17132 at 7/21/2022
Feature: Amazon Best Seller Tests
  # Enter feature description here

  Scenario:Verify all Links on Amazon Best Sellers Page are shown
    Given Open Amazon Best Sellers Page
    Then  Verify 5 Amazon Best Sellers Links are Shown
