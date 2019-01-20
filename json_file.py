import json

with open("xyz.json","r") as rd:
	data=json.load(rd)
	#print(data)
	#print(type(data))
	print(data.get("grades").get("C"))