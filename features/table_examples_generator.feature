Feature: TableExamplesGenerator

    Scenario: #calculate_columns_sizes()
      Given set of data as list of tuples
      When method 'calculate_columns_sizes' is called
      Then it sets 'column_sizes' property
      And with the biggest size of item in each column
