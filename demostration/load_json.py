import json
from pprint import pprint

with open('data_dev.json') as data_file:
	data = json.load(data_file)
pprint(data)
