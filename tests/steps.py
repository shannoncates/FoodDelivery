from lettuce import step, world, before
from nose.tools import assert_equals
from app import app
import json

@before.all
def before_all():
	world.app = app.test_client()



############################ SIGNUP STARTS HERE ######################
#Scenario: Sign Up (Sunny)
@step(u'Given the user fills the form with these details')
def Given_the_user_fills_the_form_with_these_details(step):
	for item in step.hashes:
		firstname = item["first_name"]
		middlei = item["middle_initial"]
		lastname = item["last_name"]
		email = item["email"]
		contactno = item["contact_number"]
		address = item["address"]
	world.response = world.app.post('/registeruser', data = dict(firstname = firstname, middlei = middlei, lastname = lastname, email = email, password = "pass", contactno = contactno, address = address))

@step(u'When I submit the sign up form')
def When_I_submit_the_sign_up_form(step):
	assert True

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
	assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return these details:')
def And_it_will_return_these_details(step):
	assert_equals(step.hashes, [json.loads(world.response.data)])

#Scenario: Sign Up (Rainy) email address already exists
@step(u'Given the user fills the form with these details')
def Given_the_user_fills_the_form_with_these_details(step):

	for item in step.hashes:
		firstname = item["first_name"]
		middlei = item["middle_initial"]
		lastname = item["last_name"]
		email = item["email"]
		contactno = item["contact_number"]
		address = item["address"]
	world.response = world.app.post('/registeruser', data = dict(firstname = firstname, middlei = middlei, lastname = lastname, email = email, password = "pass", contactno = contactno, address = address))

@step(u'When I submit the sign up form')
def When_I_submit_the_sign_up_form(step):
	assert True

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
	assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return these messages')
def And_it_will_return_these_messages(step):
	assert_equals(step.hashes, [json.loads(world.response.data)])

#Scenario: Sign Up (Rainy) no email address
@step(u'Given the user fills the form with these details')
def Given_the_user_fills_the_form_with_these_details(step):
	for item in step.hashes:
		firstname = item["first_name"]
		middlei = item["middle_initial"]
		lastname = item["last_name"]
		email = item["email"]
		contactno = item["contact_number"]
		address = item["address"]
	world.response = world.app.post('/registeruser', data = dict(firstname = firstname, middlei = middlei, lastname = lastname, email = email, password = "pass", contactno = contactno, address = address))

@step(u'When I submit the sign up form')
def When_I_submit_the_sign_up_form(step):
	assert True

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
	assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return these messages')
def And_it_will_return_these_messages(step):
	assert_equals(step.hashes, [json.loads(world.response.data)])

######################################################################


############################ SEARCH STARTS HERE ######################
#Scenario: Search location with keyword Cebu
@step(u'Given I search with keyword Cebu')
def Given_I_search_with_keyword_free(step):
	assert True

@step('When I submit the search bar with the keyword \'(.*)\' for \'(.*)\'')
def When_I_submit_the_search_bar_with_the_keyword_group1_for_group2(step, keyword, searchtype):
	world.response = world.app.post('api/search', data = dict(keyword = keyword, searchtype = searchtype))

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
	assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return these search details')
def And_it_will_return_these_search_details(step):
	assert_equals(step.hashes, json.loads(world.response.data)["entries"])

@step(u'And it will return a status \'(.*)\'')
def And_it_will_return_a_status_group1(step, status):
	assert_equals(status, json.loads(world.response.data)["status"])

#Scenario: Search location with keyword saasfaaf
@step(u'Given I have no data with keyword saasfaaf')
def Given_I_have_access_to_the_search_bar(step):
    assert True
    
@step('When I submit the search bar with the keyword \'(.*)\' for \'(.*)\'')
def When_I_submit_the_search_bar_with_the_keyword_group1_for_group2(step, keyword, searchtype):
    world.response = world.app.post('/api/search', data = dict(keyword = keyword, searchtype = searchtype))
    
@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return a status \'(.*)\'')
def And_it_will_return_a_status_group1(step, status):
    assert_equals(status, json.loads(world.response.data)["status"])

#Scenario: Search restaurant with keyword Pancake
@step(u'Given I search with keyword Pancake')
def Given_I_search_with_keyword_free(step):
	assert True

@step('When I submit the search bar with the keyword \'(.*)\' for \'(.*)\'')
def When_I_submit_the_search_bar_with_the_keyword_group1_for_group2(step, keyword, searchtype):
	world.response = world.app.post('api/search', data = dict(keyword = keyword, searchtype = searchtype))

@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
	assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return these search details')
def And_it_will_return_these_search_details(step):
	assert_equals(step.hashes, json.loads(world.response.data)["entries"])

@step(u'And it will return a status \'(.*)\'')
def And_it_will_return_a_status_group1(step, status):
	assert_equals(status, json.loads(world.response.data)["status"])

#Scenario: Search restaurant with keyword saasfaaf
@step(u'Given I have no data with keyword saasfaaf')
def Given_I_have_access_to_the_search_bar(step):
    assert True
    
@step('When I submit the search bar with the keyword \'(.*)\' for \'(.*)\'')
def When_I_submit_the_search_bar_with_the_keyword_group1_for_group2(step, keyword, searchtype):
    world.response = world.app.post('/api/search', data = dict(keyword = keyword, searchtype = searchtype))
    
@step(u'Then I should get a \'(.*)\' response')
def then_i_should_get_a_group1_response_group2(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))

@step(u'And it will return a status \'(.*)\'')
def And_it_will_return_a_status_group1(step, status):
    assert_equals(status, json.loads(world.response.data)["status"])

###################################################################################

