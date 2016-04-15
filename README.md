# Scholarships
Scholarships API with Token based Authentication in Django Rest Framework

## How do I get set up? ##
Currently, the repo is setup only for development. Following steps setup the local env with sqlite db.
Steps to setup:

* Project Directory Creation
```
mkdir dirname && cd dirname
```
* Clone the repo
```
git clone git@github.com:sahilbhatt92/scholarships.git
```
* Setup virtualenv
```
virtualenv env
. env/bin/activate && cd scholarships
```
* Install requirements
```
pip install -r requirements.txt
```
* Run migrations
```
./manage.py migrate
```
* Create superuser (This is a onetime step)
```
./manage.py createsuperuser
```
* Run the server
```
./manage.py runserver
```

* Admin and API access locations:
  * Admin: http://localhost:8000/admin
  * Apis: http://localhost:8000/
