Feature: Login
  # Enter feature description here

  Scenario: Successful login with valid credentials
    Given User is on 'Main' page
    And User clicked on 'My profile'
    When User login with valid credentials
    Then User should be logged in

  Scenario: Error message should be displayed while logging in with invalid credentials
    Given User is on 'Main' page
    And User clicked on 'My profile'
    When User login with invalid credentials
    Then Error message should be displayed