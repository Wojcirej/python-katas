Feature: Find parity outlier

  Scenario Outline: One of many test cases
    Given integers = <integers>
    When function 'find_parity_outlier' is called with these params
    Then function 'find_parity_outlier' returns <result>

    Examples:
    | integers                        | result |
    | [2, 4, 6, 8, 10, 3]             | 3      |
    | [2, 4, 0, 100, 4, 11, 2602, 36] | 11     |
    | [160, 3, 1719, 19, 11, 13, -21] | 160    |
