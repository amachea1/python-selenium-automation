# Created by 17132 at 7/21/2022
Feature: Amazon Cart Test
  # Enter feature description here

  Scenario:Verify User Can Add Product To Cart
     Given Open Amazon
     When  Search for Elmer's Disappearing Purple School Glue Sticks, Washable, 7 Grams, 30 Count on Amazon
     And   Click on the first product
     And   Click on add to cart button
     And   Open Cart Page
     Then  Verify cart has 1 item(s)
    # Enter steps here