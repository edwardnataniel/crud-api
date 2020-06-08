# CRUD API Using Flask (Python) and Firebase
The API can be used to create, read, update, and delete a contact from a contact list. The contact list is in a database table in Firebase.

## Requirements
The following software needs to be installed
#### 1. Latest version of Python
Download the latest version of Python compatible to your machine here: https://www.python.org/downloads/windows/

Make sure that Python is in your environment variable. You can check if Python is successfully installed by running <font color="green">python --version </font>in your command line.

<img src="md_images/python1.png" alt="drawing" width="300"/>

#### 2. Flask
Install Flask by running <font color="green">pip install -U Flask</font>  in your command line.

#### 3. Firebase Admin Python SDK
Install Firebase Admin Python SDK by running <font color="green">pip install firebase-admin</font>  in your command line.

#### 4. Postman
Postman will be used to send request and receive response.
Install it from https://www.postman.com/

## Running the API
1. Fork/clone the repository https://github.com/edwardnataniel/crud-api.

2. Open a command line inside the crud-api folder.

3. Run <font color="green">python crud.py</font>.

<img src="md_images/python2.png" alt="drawing" width="400"/>

## Create a new contact

1. To create a new contact, open Postman.

2. Click on the 'New' button on the upper-left hand of the window and choose 'Request'.

<img src="md_images/postman1.png" alt="drawing" width="400"/>

3. Add a request name and select a collection or folder to save to. You may create a new collection by clicking the 'Create Collection' button. Select the collection and press save.

<img src="md_images/postman2.png" alt="drawing" width="400"/>

4. To create a new contact, make a POST request and append the '/create' string in the url displayed in the command line. Select the 'Body' tab. Select 'raw' and choose the JSON file type.

5. Add the JSON object in the body of the request. Here is an example.

{
	"id": "1",
	"name": "John Doe",
	"mobile": "09271234567",
	"email": "john.doe@gmail.com"
}

Don't forget to add an "id" field (string).

<img src="md_images/create.png" alt="drawing" width="500"/>

6. Press the 'send' button. Scroll down to see the response message. The response message

{
    "success": true
}

means that request was successful. The new contact was added to the database.

<img src="md_images/create1.png" alt="drawing" width="500"/>

By looking at the database in firebase, we can see that a new entry is added at the contacts table.

<img src="md_images/firebase_create.png" alt="drawing" width="500"/>

## Read a contact / all contacts

You can read a single contact using its id or you can read all contacts when no id is specified.

1. To read all contacts, do a 'GET' request. Replace '/create' by 'read' in the request url. Leave the message body blank.

<img src="md_images/read.png" alt="drawing" width="500"/>

All contacts in the database will be returned in the response message.

<img src="md_images/read1.png" alt="drawing" width="500"/>

2. To read a specific contact, do a 'GET' request. Replace '/create' by 'read' in the request url. Append an "?id=<id number>" argument in the request url.
Example: 'http://0.0.0.0:8080/read?id=1' retrieves the record with id=1

<img src="md_images/read2.png" alt="drawing" width="500"/>

Here is the response:

<img src="md_images/read3.png" alt="drawing" width="500"/>

## Update a contact

1. To update a contact, make a 'POST' request. Append '/update' to the request url. In the body of the request, add the JSON object to update a contact. In this example, we are changing the mobile number of the contact with id=1.

<img src="md_images/update.png" alt="drawing" width="500"/>

Here is the response message that indicates a successful operation.

<img src="md_images/update1.png" alt="drawing" width="500"/>

By checking the database, we can see that the mobile number was now updated.

<img src="md_images/update3.png" alt="drawing" width="500"/>

## Delete a contacts

1. To delete a contact, make a 'DELETE' request. Append '/delete' in the url request. Also, append an "?id=<id number>" argument in the request url.

<img src="md_images/delete.png" alt="drawing" width="500"/>

Here is the response message that indicates a successful operation.

<img src="md_images/delete1.png" alt="drawing" width="500"/>

By checking the database, we can see that the contact has been deleted. Contact with id = 1 no longer exist.
<img src="md_images/delete2.png" alt="drawing" width="500"/>
