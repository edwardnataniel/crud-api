import os
from flask import Flask, jsonify, request
from firebase_admin import firestore, credentials, initialize_app

# initializes flask
app = Flask(__name__)

# initializes firebase database
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
contact_ref = db.collection('contacts')

@app.route('/create', methods=['POST'])
def create():
	try:
		contact_id = request.json['id']
		contact_ref.document(contact_id).set(request.json)
		return jsonify({"success": True}), 200
	except Exception as e: 
		print(e)
		
@app.route('/read', methods=['GET'])
def read():
	try:
		contact_id = request.args.get('id')
		if contact_id:
			contact = todo_ref.document(contact_id).get()
			return jsonify(contact.to_dict()), 200
		else:
			contact_list = [contact.to_dict() for contact in contact_ref.stream()]
			return jsonify(contact_list), 200
	except Exception as e: 
		print(e)

@app.route('/update', methods=['POST', 'PUT'])
def update():
	try:
		contact_id = request.json['id']
		contact_ref.document(contact_id).update(request.json)
		return jsonify({"success": True}), 200
	except Exception as e: 
		print(e)
		
@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
	try:
		contact_id = request.args.get('id')
		contact_ref.document(contact_id).delete()
		return jsonify({"success": True}), 200
	except Exception as e:
		print(e)

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
	app.run(threaded=True, host='0.0.0.0', port=port)