Feature: Calculator

  Scenario Outline: Evaluate multiple expressions
    Given I enter "<expression>"
    When I press "=" button
    Then I get the answer "<answer>"

    Examples:
    | expression | answer |
    | 3 + 2      |   5    |
    | 3 - 2      |   1    |
    | 3 * 2      |   6    |
    | 3 / 2      |  1.5   |
    | 3 +-*/ 2   | Invalid Input |
    | hello world| Invalid Input |
