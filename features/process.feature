Feature: Create Process
    As a Student
    I want to Create a Process
    So that I can add new processes into memory

    Scenario Outline: Successfully creates process
        Given I enter <process_name>
        And I enter <process_size>
        When I press create process
        Then a process with <process_name> and <process_size> should be created
    Examples:
        | process_name | process_size |
        | Firefox      | 100          |


