from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates/index.html")


####################   DATABASE CONNECTION   ###################


def spcall(qry, param, commit=False):
    """ Function which communicates with the database """

    try:
        dbo = DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()
        return res
    except:
        res = [('Error: ' + str(sys.exc_info()[0]) + ' '
               + str(sys.exc_info()[1]), )]
    return res


#################################################################

	
###################### SIGN UP #################################
@app.route('/api/registeruser', methods=['POST'])
def register():
	return send_file("templates/signup.html")

	passw = request.form["password"]
	passw = passw + key
	passw = hashlib.md5(passw.encode())
	email = request.form["email"]

	if email == '':
		return jsonify({'status': 'error2', 'message': 'email cannot be blank'})

	email_validity = False
	valid_email_ending = False

	for endings in valid_endings:
		if endings in email:
			valid_email_ending = True

	if "@" in email and valid_email_ending:
		email_validity = True


	if email_validity == False:
		return jsonify({'status': 'error2', 'message': 'invalid email'})



	recs = spcall('list_users', ())
	if 'Error' in str(recs[0][0]):
		return jsonify({'status': 'error', 'message': recs[0][0]})
	for element in recs:
		if email == str(element[0]):
			return jsonify({'status': 'error2', 'message': 'email already exists'})

	res = spcall('add_user', (
		request.form["email"],
		request.form["firstname"],
		request.form["middlei"],
		request.form["lastname"],
		request.form["contactno"],
		request.form["address"],
		passw
		), True)

	if 'Error' in str(res[0][0]):
		return jsonify({'status': 'error', 'message': res[0][0]})
	return jsonify({'status': 'ok', 'message': res[0][0]})

##################################################################


################################## SEARCH ########################
@app.route('/api/search', methods=['POST'])
def search():

	"""" Search a restaurant using keyword """
	passedkeyword = request.form["keyword"].lower() + "%"
	passed = [passedkeyword, 0]
	recs = []
	if request.form["keyword"] == "":
			return jsonify({'status': 'no entries', 'count': 0})
	if request.form["searchtype"] == "restaurant":
		res = spcall('get_restaurant_starting_with', passed[:1], True)
		for r in res:
			recs.append({'restaurant_id': str(r[0]), 'location_id': r[1], 'restaurant_name': r[2], 'restaurant_info': r[3], 'is_active': str(r[4])})
		if len(recs) == 0:
			return jsonify({'status': 'no entries', 'count': len(recs)})
		return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
	else:
		res = spcall('get_location_starting_with', passed[:1], True)
		for r in res:
			recs.append({'location_id': str(r[0]), 'location_name': r[1]})
		if len(recs) == 0:
			return jsonify({'status': 'no entries', 'count': len(recs)})
		return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

#######################################################


############# LOCATION ################################
@app.route('/api/location', methods=['GET'])
def get_locations():

	res = spcall('list_locations', ())
	if 'Error' in str(res[0][0]):
		return jsonify({'status': 'error', 'message': res[0][0]})

	recs = []
	for r in res:
		recs.append({'location_id': r[0], 'location_name': r[1]})
	return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/location/<int:locationid>', methods=['GET'])
def get_certain_location(locationid):

	res = spcall('get_location', str(locationid))
	if 'Error' in str(res[0][0]):
		return jsonify({'status': 'error', 'message': "location id does not exist"})

	for r in res:
		recs = {'location_id': str(r[0]), 'location_name': r[1]}
	return jsonify({'status': 'ok', 'entry': recs})

#############################################################################


############# RESTAURANT ##############################
@app.route('/api/restaurant/location/<int:location_id>', methods=['GET'])
def get_restaurant_location(location_id):

	location_list = spcall('list_locations', ())
	matched_restaurant = spcall('get_restaurant_by_location', [str(location_id)])

	if ((location_id > len(location_list)) or (location_id < 1) or (len(matched_restaurant)==0)):
		return jsonify({'status': 'error', 'message': 'no match found'})

	else:
		recs = []
		for i in matched_restaurant:

			recs.append({'restaurant_id': str(i[0]),
					'location_id': str(i[1]),
					'restaurant_name': i[2],
					'restaurant_info': i[3]})

		return jsonify({'status': 'successful', 'match': recs})

#######################################################


############# FOOD #####################################
@app.route('/api/food/restaurant/<int:restaurant_id>', methods=['GET'])
def get_food_restaurant(restaurant_id):


	restaurant_list = spcall('list_restaurants', ())
	matched_food = spcall('get_food_by_restaurant', [str(restaurant_id)])

	if ((restaurant_id > len(restaurant_list)) or (restaurant_id < 1) or (len(matched_food)==0)):
		return jsonify({'status': 'error', 'message': 'no match found'})

	else:
		recs = []
		for i in matched_food:

			recs.append({'food_id': str(i[0]),
					'restaurant_id': str(i[1]),
					'food_name': i[2],
					'food_info': i[3],
					'food_price': i[4]})

		return jsonify({'status': 'successful', 'match': recs})

######################################################################
	
if __name__ == "__main__":
    app.run(debug=True, port=5005)