Hello there,

This mini-project is made in Python and Django.
The instructions are:

1. Download the project.
2. Open a terminal or open the program in any IDE (I used VSC).
3. Install the requirements using this command in terminal: pip install -r requirements.txt (Install pyhton and pip https://phoenixnap.com/kb/install-pip-windows).
4. Use this command in terminal to launch the app: python manage.py runserver 0.0.0.0:8000 .

Now go to: http://localhost:8000 and you cand Edit, Post, Delete, Get the contacts.

Or open Postman and to GET all the contacts use: http://localhost:8000/contacts/
To POST: http://localhost:8000/contacts/ and this body as example:

{
        "first_name": "name",
        "last_name": "lname",
        "email": "email@yahoo.com",
        "phoneNumber": "070000000"
}

To GET one contact: http://localhost:8000/contacts/<id>
To PUT one contact: http://localhost:8000/contacts/<id> and his body with the updated fields.
To DELETE on contact: http://localhost:8000/contacts/<id>

There is a demo: https://www.youtube.com/watch?v=ckj0KDmUv3I
