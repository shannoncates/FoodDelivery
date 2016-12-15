Scenario: Sign Up (Sunny)

Given the user fills the form with these details:
| first_name | middle_initial | last_name | email | password | contact_number | address |
| Paul | F | Lee | paul@gmail.com | pass | 09061234567 | address1 |
When I submit the sign up form
Then I should get a '200' response
And it will return these details:
| message | status |
| Sign Up success | ok |


Scenario: Sign Up (Rainy) email address already exists

Given the user fills the form with these details:
| first_name | middle_initial | last_name | email | password | contact_number | address |
| Paul | F | Lee | paulf00@gmail.com | pass | 09061234567 | address1 |
When I submit the sign up form
Then I should get a '200' response
And it will return these messages:
| message | status |
| Email address already exists | error1 |


Scenario: Sign Up (Rainy) no email address

Given the user fills the form with these details:
| first_name | middle_initial | last_name | email | password | contact_number | address |
| Paul | F | Lee | | pass | 09061234567 | address1 |
When I submit the sign up form
Then I should get a '200' response
And it will return these messages:
| message | status |
| Email address cannot be blank | error1 |