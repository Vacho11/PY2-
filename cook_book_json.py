import json 
from pprint import pprint

with open('cook_book.json') as cook_file:
	List = json.load(cook_file)
	pprint(List)
