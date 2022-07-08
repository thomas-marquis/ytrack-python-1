Feature: Ships

    Scenario Outline: Build ships in default fleet
        Given ship name is "<ship>"
        And quantity is "100"
        And there is enough metal
        And there is enough crystal
        And fleet name is "default"
        When call route /ship with POST
        Then following ships should be in space dock
            | fleet   | ship   | number |
            | default | <ship> | 100    |
        And return status code "201"

        Examples: Ship types
            | ship        |
            | interceptor |
            | bomber      |
            | destroyer   |
            | cruiser     |
            | frigate     |

    Scenario: Build ships in new fleet
        Given ship name is "interceptor"
        And quantity is "100"
        And there is enough metal
        And there is enough crystal
        And fleet name is "attackers"
        When call route /ship with POST
        Then following ships should be in space dock
            | fleet     | ship        | number |
            | default   |             |        |
            | attackers | interceptor | 100    |
        And return status code "201"

    Scenario: Build ships without enough metal
        Given ship name is "CRUISER"
        And quantity is "35"
        And there is NOT enough metal
        And there is enough crystal
        And fleet name is "default"
        When call route /ship with POST
        Then space dock should be empty
        And return status code "400"

    Scenario: Build ships with invalid ship name
        Given ship name is "dethstar"
        And quantity is "1"
        And there is enough metal
        And there is enough crystal
        And fleet name is "default"
        When call route /ship with POST
        Then space dock should be empty
        And return status code "404"

    Scenario: Get default fleet
        Given fleet name is "default"
        When call route /ship/fleet/[fleet_name] with GET
        Then return fleet report
            | alive_battleships | alive_fighters | dead_battleships | dead_fighters |
            | 0                 | 0              | 0                | 0             |
        And return status code "200"

    Scenario: Get non empty fleet
        Given fleet name is "defenders"
        And space dock contains following ships
            | fleet     | ship        | number |
            | default   |             |        |
            | defenders | interceptor | 150    |
            | defenders | bomber      | 50     |
            | defenders | cruiser     | 30     |
            | defenders | frigate     | 30     |
        When call route /ship/fleet/[fleet_name] with GET
        Then return fleet report
            | alive_battleships | alive_fighters | dead_battleships | dead_fighters |
            | 60                | 200            | 0                | 0             |
        And return status code "200"
