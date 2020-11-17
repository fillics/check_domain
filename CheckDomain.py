import requests, json, time
from credentials import API_KEY, API_SECRET, TOKEN

def CheckDomain(name):
	print("Searching "+ name + ".com ...")
	headers = {
	    'accept': 'application/json',
	    'Authorization': 'sso-key '+API_KEY+':'+API_SECRET,
	}

	params = {
	    ('domain', name+'.com'),
	    ('checkType', 'FAST'),
	    ('forTransfer', 'false'),
	}

	response = requests.get('https://api.ote-godaddy.com/v1/domains/available', headers=headers, params=params)
	accessible = response.json().get('available')
	if accessible == True:
		print(name+'.com is available!')
		f.write(name+'.com is available\r\n')

	time.sleep(2)


file = open('animals.json')
data = json.load(file)
f = open('AvailableWebsites.txt', 'w')

choice = int(input("Text file [1] or Json file [2]? "))


if choice == 1:
	with open ('domains.txt', 'rt') as filetxt:  
	    for name in filetxt:              					
	        CheckDomain(name.lower().rstrip())
	        
        
elif choice == 2:
	print(choice)
	for name in data:
		CheckDomain(name)


f.close()
file.close()


