Feature: Automorphic number

  Scenario Outline: One of many test cases
    Given number = <number>
    When function 'automorphic_number' is called with these params
    Then function 'automorphic_number' returns <result>

    Examples:
    | number | result        |
    | 1      | "Automorphic" |
    | 3      | "Not!!"       |
    | 6      | "Automorphic" |
    | 9      | "Not!!"       |
    | 25     | "Automorphic" |
    | 53     | "Not!!"       |
    | 76     | "Automorphic" |
    | 95     | "Not!!"       |
    | 625    | "Automorphic" |
    | 225    | "Not!!"       |
    | 471    | "Not!!"       |
    | 511    | "Not!!"       |
    | 9376   | "Automorphic" |
    | 4      | "Not!!"       |
    | 393    | "Not!!"       |
    | 3981   | "Not!!"       |
    | 31748  | "Not!!"       |
    | 35107  | "Not!!"       |
    | 322    | "Not!!"       |
    | 38058  | "Not!!"       |
    | 74     | "Not!!"       |
    | 25076  | "Not!!"       |
    | 63     | "Not!!"       |
    | 687    | "Not!!"       |
    | 376    | "Automorphic" |
    | 62705  | "Not!!"       |
    | 470    | "Not!!"       |
    | 728    | "Not!!"       |
    | 18415  | "Not!!"       |
    | 22041  | "Not!!"       |
    | 17949  | "Not!!"       |
    | 675    | "Not!!"       |
    | 6193   | "Not!!"       |
    | 780    | "Not!!"       |
    | 43     | "Not!!"       |
    | 12275  | "Not!!"       |
    | 20890  | "Not!!"       |
    | 10135  | "Not!!"       |
    | 40600  | "Not!!"       |
    | 7      | "Not!!"       |
    | 55445  | "Not!!"       |