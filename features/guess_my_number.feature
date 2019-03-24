Feature: Guess my number

  Scenario Outline: One of many test cases
    Given guess = <guess>
    When function 'guess_my_number' is called with these params
    Then function 'guess_my_number' returns <result>

    Examples:
    | guess    | result         |
    | '0'      | '###-###-####' |
    | '01'     | '1##-##1-####' |
    | '012'    | '12#-##1-2###' |
    | '0123'   | '123-##1-23##' |
    | '01234'  | '123-4#1-234#' |
    | '012345' | '123-451-2345' |
