@with_data_for_test_kata
Feature: TestExamplesParser

  Scenario: Reading test data and creating list of tuples
    Given underscored kata name
    When method 'parse' is called
    Then method 'parse' returns list
    And list contains tuples
    And list contains as much tuples as lines in source file
