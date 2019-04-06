Feature: Greed is good

  Scenario Outline: One of many test cases
    Given dice = <dice>
    When function 'greed_is_good' is called with these params
    Then function 'greed_is_good' returns <result>

    Examples:
    | dice            | result |
    | [2, 3, 4, 6, 2] | 0      |
    | [1, 1, 1, 3, 3] | 1000   |
    | [2, 2, 2, 3, 3] | 200    |
    | [3, 3, 3, 3, 3] | 300    |
    | [4, 4, 4, 3, 3] | 400    |
    | [5, 5, 5, 3, 3] | 500    |
    | [6, 6, 6, 3, 3] | 600    |
    | [1, 1, 1, 1, 3] | 1100   |
    | [1, 1, 1, 1, 5] | 1150   |
    | [2, 4, 4, 5, 4] | 450    |
    | [3, 4, 5, 3, 3] | 350    |
    | [1, 5, 1, 3, 4] | 250    |
