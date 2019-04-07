Feature: Array diff

  Scenario Outline: One of many test cases
    Given first_array = <first_array>, second_array = <second_array>
    When function 'array_diff' is called with these params
    Then function 'array_diff' returns <result>

    Examples:
    | first_array | second_array | result    |
    | [1, 2]      | [1]          | [2]       |
    | [1, 2, 2]   | [1]          | [2, 2]    |
    | [1, 2, 2]   | [2]          | [1]       |
    | [1, 2, 2]   | []           | [1, 2, 2] |
    | []          | [1, 2]       | []        |
