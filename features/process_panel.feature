Feature: User inputs process details
    As a User
    I want to create a new process
    So that I can add new processes to memory

    Scenario Outline: Input new valid process details
        Given "<process_name>" does not exist in memory
        When I enter process name "<process_name>" 
        And I enter process size "<process_size>" 
        And I press the create process button
        Then "<process_name>" should be in memory
    Examples:
        | process_name | process_size |
        | Calculator   | 100          |
        | Vim          | 300          |
        | Clock        | 30           |
