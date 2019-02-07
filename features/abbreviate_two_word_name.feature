Feature: Abbreviate two word name

  Scenario Outline: One of many test cases
    Given name equals <name>
    When called function 'abbreviate_two_word_name'
    Then returns <initials>

    Examples: Names
    | name           | initials |
    | Sam Smith      | S.S      |
    | some Name      | S.N      |
    | Some name      | S.N      |
    | Sam Harris     | S.H      |
    | Patrick Feenan | P.F      |
