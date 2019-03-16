@with_clean_up
Feature: KataGenerator

  Scenario: Generating kata files
    Given kata_name = 'test_kata'
    When method 'call' of class KataGenerator called
    Then it creates 'test_kata' directory inside 'katas' directory
    And creates '__init__.py' file inside 'test_kata' directory
    And creates 'README.md' file inside 'test_kata' directory
    And creates 'test_kata.py' file inside 'test_kata' directory
    And creates 'test_kata.feature' file inside 'features' directory
    And creates 'test_kata.py' file inside 'features/steps' directory
