#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import State, City

import django
django.setup()
# State.objects.all().delete()

dir_path = os.path.dirname(os.path.abspath(__file__))

cities_csv = os.path.join(dir_path, 'cities.csv')

csv_file = open(cities_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	state, created = State.objects.get_or_create(abbreviation=row['state'])
	try:
		state.save()
	except Exception, e:
		print state.name
		print e

	new_city, created = City.objects.get_or_create(name=row['city'])
	new_city.zip_code = row['zip_code']
	if row['latitude']:
		new_city.latitude = row['latitude']
	if row['longitude']:
		new_city.longitude = row['longitude']
	new_city.county = row['county']	
	new_city.state = state

	try:
		new_city.save()
	except Exception, e:
		print new_city.name
		print e
		print row