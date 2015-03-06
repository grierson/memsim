Feature: Input Process Details
    As a Student
    I want to input Process details
    So that I can create processes

    Scenario Outline: Successfully input valid process details
        Given I enter process details "<process_name>", "<process_size>"
        When I press the create button
        Then process is created
    Examples:
        | process_name | process_size |
        | Calculator   | 100          |
        | Vim          | 800          |
        | Clock        | 30           |
        | Clock        | 40           |
