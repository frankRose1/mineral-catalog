# Mineral Catalog With Django
This website displays information about minerals in a database using Django. Views include a list of all database entries and a more detailed view which shows all the info available
for a given mineral. Also includes a search feature and a filter menu. I used migrations to populate the database with JSON data, which you can see in ```minerals/migrations/0002_auto_20190116_0020```

**NOTE** I purposely didn't commit the images as there are hundreds.

## App Features
* Minerals list view which shows a list of minerals in the databse
* Search feature that will search by name, mohs scale hardness, or crystal symmetry
* Filter allows filtering by group or aplhabetically
* Detailed mineral view for a single mineral
* Serves static css/images
* Custom filters/tags
* Unit tests

## Tests
- django-nose is used to run tests and track coverage
- run ```pipenv run python manage.py test```
- some command line args are passed in by default, can be seen in ```settings.py``` under ```NOSE_ARGS```

## Technologies Used
* Django 2.1.5