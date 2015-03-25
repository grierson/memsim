Feature: Input Process Details
    As a Student
    I want to input Process details
    So that I add a new process to RAM

    Scenario Outline: Successfully input valid process details
        Given that I am on the Process Panel
        When I enter process details "<process_name>" 
        And I enter process size "<process_size>" 
        And I press the create button
        Then process is added to the process list
    Examples:
        | process_name | process_size |
        | Calculator   | 100          |
        | Vim          | 800          |
        | Clock        | 30           |
