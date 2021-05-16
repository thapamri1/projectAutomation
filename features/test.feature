Feature: Check Orbitz website
  Scenario: go to orbitz website and close it
    Given launch chrome browser
    Then Open the website
    Then Select Flights
    Then Select RoundTrip
    Then Enter Leaving From "San Francisco" and Going to "New York" city
#    Then select select departing date and returning date
    Then click Search Button
    Then select most expensive flight
    Then Select Button
    And close browser