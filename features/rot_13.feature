Feature: Rot 13

  Scenario Outline: One of many test cases
    Given input = <input>
    When function 'rot_13' is called with these params
    Then function 'rot_13' returns <result>

    Examples:
    | input                               | result                              |
    | "EBG13 rknzcyr."                    | "ROT13 example."                    |
    | "This is my first ROT13 excercise!" | "Guvf vf zl svefg EBG13 rkprepvfr!" |
