Feature: Earning extra points from Frequent Flyer from flights
    Scenario: Earning standard points from an Economy flight
        Given the flying distance between Sydney and Melbourne is 878 km
        And I am a standard Frequent Flyer member
        When I fly from Sydney to Melbourne
        Then I should earn 439 points
