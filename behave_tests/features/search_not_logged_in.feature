Feature: search goods in different categories while user is not logged in
  # Enter feature description here

  Scenario Outline: search goods in different categories
    Given User is on 'Main' page
    When User filled search field with <search>
    Then Clicked on Search button
    And Selected <category> from the Categories
    And A list of adverts with a <search> is displayed

    Examples:
      | search    | category    |
      | Крокодил  | Животные    |
      | Катамаран | Животые     |
      | Iphone s4 | Електроника |

  Scenario Outline: : search all goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Iphone    |

  Scenario Outline: search only private goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Selected private types of goods
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Samsung   |

  Scenario Outline: search only business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Selected business types of goods
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Nokia     |

  Scenario Outline: sort only new search results for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied new sort filter
    And Selected business types of goods
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Dell      |

  Scenario Outline: sort only cheap search results for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied cheap sort filter
    And Selected business types of goods
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Lenovo    |

  Scenario Outline: sort only expensive search results for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied expensive sort filter
    And Selected business types of goods
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Apple     |

  Scenario Outline: show search results in Hryvna for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied expensive sort filter
    And Selected business types of goods
    And Selected currency Hryvna
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Apple     |

  Scenario Outline: show search results in USD for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied expensive sort filter
    And Selected business types of goods
    And Selected currency USD
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Apple     |

  Scenario Outline: show search results in EUR for business goods in all categories
    Given User is on 'Main' page
    When User filled search field with <GoodsName>
    And Clicked on Search button
    And Applied expensive sort filter
    And Selected business types of goods

    And Selected currency EUR
    Then A list of adverts with a <GoodsName> is displayed
    Examples: phones
      | GoodsName |
      | Apple     |

