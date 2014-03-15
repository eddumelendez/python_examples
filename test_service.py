import requests
import json

#Persona (name, lastname, alias)
#JSON 
#{"name" : "Pepito", "lastname" : "Perez", "alias" : "pperez"}
#XML
#<persona>
#<name>Pepito</name>
#<lastname>Perez</lastname>
#<alias>pperez</alias>
#</persona>

#HTTP methods
#GET (link, browser)
#POST (form)
#PUT
#DELETE

url = "http://urlService"
#user_service = "admin"
#password_service = "admin"

response = requests.post(url)
#response = requests.post(url, auth=(user_service, password_service))
jsonResponse = json.loads(response.text)
try:
	for item in range(len(jsonResponse)):
		print jsonResponse[item]
except AssertionError:
    print "Error"