import sys, time, telepot, json
from telepot.loop import MessageLoop
from pprint import pprint
import requests
from credentials import API_KEY, API_SECRET, TOKEN

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    
    if content_type == 'text':
        text = msg['text']
        if text == '/start':
            bot.sendMessage(chat_id, "Hi! Send me a JSON/txt file that contains the list of domains or text me the domain to check out.")
        else:
        	text = text.casefold()
        	bot.sendMessage(chat_id, "Searching "+ text + ".com ...")
        	CheckDomain(text, chat_id)

    elif content_type == 'document':

        documentName = msg['document']
        filename = documentName['file_name']
        mimetype = documentName['mime_type']

        if mimetype == 'application/json':
            filejson = open(filename)
            data = json.load(filejson)
            for name in data:
                CheckDomain(name.lower(), chat_id)


        elif mimetype == 'text/plain':
            with open (filename, 'rt') as filetxt:
                for name in filetxt:
                    CheckDomain(name.lower().rstrip(), chat_id)

        else:
            bot.sendMessage(chat_id, "Unsupported file format")

        	
def CheckDomain(text, chat_id):
	headers = {
        	'accept': 'application/json',
        	'Authorization': 'sso-key '+API_KEY+':'+API_SECRET,
        	}

	params = {
	('domain', text+'.com'),
	('checkType', 'FAST'),
	('forTransfer', 'false'),
	}

	response = requests.get('https://api.ote-godaddy.com/v1/domains/available', headers=headers, params=params)
	accessible = response.json().get('available')
	if accessible == True:
		bot.sendMessage(chat_id, text+ ".com is available!")
	else:
		bot.sendMessage(chat_id, text+ ".com is not available!")

	time.sleep(2)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
