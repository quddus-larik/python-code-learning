import json

file = open("first.json", "r") 
data = json.load(file)  # Not file.read()
print(data[1])