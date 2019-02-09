Feature: Replace with alphabet position

  Scenario Outline: One of many test cases
    Given text = <text>
    When function 'alphabet_position' called with these params
    Then function 'alphabet_position' returns <result>

    Examples: Alphabet positions
    | text                                  | result                                                                  |
    | "The sunset sets at twelve o' clock." | 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11 |
