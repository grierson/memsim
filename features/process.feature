Feature: Create Process
        As a Simulator
        I want to create a process
        So that I add it to Memory

        Scenario Outline: Correct Details
                Given process name "<name>"
                And process size "<size>"
                And process address "<address>"
                When I create the process
                Then a process with the name "<name>"
                And process size "<size>"
                And should be at "<address>"

                Examples:
                        | name    | size | address |
                        | Firefox | 300  | 0       |
                        | Word    | 200  | 301     |
                        | Vim     | 100  | 501     |
