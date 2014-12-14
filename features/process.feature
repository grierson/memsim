Feature: Create Process
    Scenario Outline: Successfully creates process
        Given I enter "<process_name>" with "<process_size>"
        When I press create process
        Then a process with "<process_name>" with "<process_size>" is created 
    Examples:
        | process_name | process_size |
        | Firefox      | 100          |
        | Vim          | 800          |
        | MPD          | 400          |
        | VLC          | 650          |
