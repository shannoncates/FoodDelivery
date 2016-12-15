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