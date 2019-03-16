Feature: KataGeneratorTemplater

    Scenario: #humanize_kata_name()
      Given kata name underscored
      When method 'humanize_kata_name' is called
      Then it returns kata name with separated words
      And capitalized first letter

    Scenario Outline: #format_params_string_for_given_clause()
      Given params = <params>
      When method 'format_params_string_for_given_clause' called
      Then method 'format_params_string_for_given_clause' returns <result>

      Examples: List of params
      | params             | result                            |
      | []                 | "no params"                       |
      | ["arg1"]           | "arg1 = <arg1>"                   |
      | ["a1", "a2"]       | "a1 = <a1>, a2 = <a2>"            |
      | ["a1", "a2", "a3"] | "a1 = <a1>, a2 = <a2>, a3 = <a3>" |

    Scenario Outline: #format_params_string_for_given_decorator()
      Given array of params = <params>
      When method 'format_params_string_for_given_decorator' called
      Then method 'format_params_string_for_given_decorator' returns <result>

      Examples: List of params
      | params             | result                            |
      | []                 | "no params"                       |
      | ["arg1"]           | "arg1 = {arg1}"                   |
      | ["a1", "a2"]       | "a1 = {a1}, a2 = {a2}"            |
      | ["a1", "a2", "a3"] | "a1 = {a1}, a2 = {a2}, a3 = {a3}" |

    Scenario Outline: #format_params_string_for_given_method_arguments()
      Given params like <params>
      When method 'format_params_string_for_given_method_arguments' called
      Then method 'format_params_string_for_given_method_arguments' returns <result>

      Examples: List of params
      | params             | result                |
      | []                 | "context"             |
      | ["arg1"]           | "context, arg1"       |
      | ["a1", "a2"]       | "context, a1, a2"     |
      | ["a1", "a2", "a3"] | "context, a1, a2, a3" |

    Scenario Outline: #format_params_string_for_given_method_definition()
      Given set of params = <params>
      When method 'format_params_string_for_given_method_definition' called
      Then method 'format_params_string_for_given_method_definition' returns <result>

      Examples: List of params
      | params             | result                                                            |
      | []                 | ""                                                                |
      | ["arg1"]           | "    context.arg1 = arg1\n"                                       |
      | ["a1", "a2"]       | "    context.a1 = a1\n    context.a2 = a2\n"                      |
      | ["a1", "a2", "a3"] | "    context.a1 = a1\n    context.a2 = a2\n    context.a3 = a3\n" |

    Scenario Outline: #format_params_for_method_call()
      Given list of params = <params>
      When method 'format_params_for_method_call' called
      Then method 'format_params_for_method_call' returns <result>

      Examples: List of params
      | params             | result                               |
      | []                 | ""                                   |
      | ["arg1"]           | "context.arg1"                       |
      | ["a1", "a2"]       | "context.a1, context.a2"             |
      | ["a1", "a2", "a3"] | "context.a1, context.a2, context.a3" |
