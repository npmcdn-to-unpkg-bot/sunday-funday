# sunday-funday
SVV Project
[![Build Status](https://travis-ci.org/mihaibivol/sunday-funday.svg)](https://travis-ci.org/mihaibivol/sunday-funday)

# first steps

```
git clone this
virtualenv sandbox
source sandbox/bin/activate
pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata fixtures/initial.json
./manage.py runserver
```


* go to http://localhost:8000
* go to http://localhost:8000/admin

* log in with your superuser credentials
* add events and users (btw, password does not work)

# after any pull

```
./manage.py migrate
```

if things are realy broken

```
rm db.sqlite3
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata fixtures/initial.json
```

# after altering models

Please migrate the initial fixtures

```
./manage.py makemigrations
./manage.py migrate
./manage.py dumpdata --format json > fixtures/initial.json
```

If shit hits the fan

```
rm -r sundayfunday/migrations/
rm db.sqlite3
./manage.py makemigrations
./manage.py migrate
# Add by hand any other fixtures
./manage.py dumpdata --format json > fixtures/initial.json
```

Don't forget to commit migrations

# things to know

* all users should have as password `sundayfunday`
* to change a user's pasword before we have the register form use the auth
  users table not the sundayfunday users table.

We might need these packages
* python-dev

