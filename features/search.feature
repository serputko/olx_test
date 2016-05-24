# Created by Arn at 4/6/2016
Feature: search
  # Enter feature description here

  Scenario Outline: search for a crocodile
    Given User is on 'Main' page
    When User filled search field with <search>
    Then Clicked on Search button
    And Selected <category> from the Categories
    And A list of adverts with a <search>

    Examples:
    |search       |category     |
    |Крокодил     |Животные     |
    |Катамаран    |Животные     |
    |Iphone s4    |Електроника  |