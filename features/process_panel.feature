Feature: Input Process Details
    As a Student
    I want to create Processes
    So that I can add processes to RAM
    Scenario Outline: Successfully input correct process details
        Given I what to create a new process
        When I enter name: "<process_name>" with size: "<process_size>"
        Then process "<process_name>" with "<process_size>" is created 
    Examples:
        | process_name | process_size |
        | Calculator   | 100          |
        | Vim          | 800          |
        | Clock        | 30           |
