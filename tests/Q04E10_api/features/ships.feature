Feature: Ships

    Scenario: Build ships in default fleet
        Given ship name is "interceptor"
        And quantity is "100"
        And metal stock is "100000"
        And crystal stock is "20000"
        And fleet name is "default"
        When call route /ship with POST
        Then following ships should be in space dock
            | fleet   | ship        | number |
            | default | interceptor | 100    |
        And return status code "201"

    Scenario: Build ships in new fleet
        Given ship name is "interceptor"
        And quantity is "100"
        And metal stock is "100000"
        And crystal stock is "20000"
        And fleet name is "attackers"
        When call route /ship with POST
        Then following ships should be in space dock
            | fleet     | ship        | number |
            | default   |             |        |
            | attackers | interceptor | 100    |
        And return status code "201"

    # Scenario: Build ships without enough metal
    #     Given ship name is "CRUISER"
    #     And quantity is "35"
    #     And metal stock is "800000"
    #     And crystal stock is "400000"
    #     And fleet name is "default"
    #     When call route /ship with POST
    #     Then ships should NOT be created in space dock
    #     And return status code "400"

    # Scenario: Build ships with invalid ship name
    #     Given ship name is "dethstar"
    #     And quantity is "1"
    #     And metal stock is "1000000"
    #     And crystal stock is "1000000"
    #     And fleet name is "default"
    #     When call route /ship with POST
    #     Then ships should NOT be created in space dock
    #     And return status code "404"

    Scenario: Get ships
        Given fleet name is "default"
        When call route /ship/fleet/<fleet_name> with GET
        Then return fleet report
        And return status code "200"
