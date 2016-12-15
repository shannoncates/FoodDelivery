Feature: Search


Scenario: Search location with keyword Cebu
Given I search with keyword Cebu
When I submit the search bar with the keyword 'Cebu' for 'location'
Then I should get a '200' response
And it will return these search details:
| location_id | location_name |
| 1 | Cebu City |
And it will return a status 'ok'


Scenario: Search location with keyword saasfaaf
Given I have no data with keyword saasfaaf
When I submit the search bar with the keyword 'saasfaaf' for 'location'
Then I should get a '200' response
And it will return a status 'no entries'


Scenario: Search restaurant with keyword Pancake
Given I search with keyword Pancake
When I submit the search bar with the keyword 'Pancake' for 'restaurant'
Then I should get a '200' response
And it will return these search details:
| restaurant_id | location_id | restaurant_name | restaurant_info |
| 1 | 1 | Pancake House | info1 |
And it will return a status 'ok'


Scenario: Search restaurant with keyword saasfaaf
Given I have no data with keyword saasfaaf
When I submit the search bar with the keyword 'saasfaaf' for 'restaurant'
Then I should get a '200' response
And it will return a status 'no entries'

