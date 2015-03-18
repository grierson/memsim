Feature: First Fit Allocation
        As a Memory Simulator
        I want to implement First Fit Allocation
        So that I demonstrate First Fit Allocation

        Scenario Outline: Enter Correct Process Details
                Given process size "<process_size>"
                When hole equals "<process_size>"
                Then allocate process to that address
        Examples:
                | process_size |
                | 100          |
                | 200          |
                | 300          |
