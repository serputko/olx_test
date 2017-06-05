# Created by arnsh at 04.06.17
Feature: login
  # Enter feature description here

  Scenario: successful login with valid credentials
    Given User is on 'Main' page
    And User clicked on 'My profile'
    When User login
    Then User should be logged in