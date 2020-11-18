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
            bot.sendMessage(chat_id, "Hi! Text me the domain to check out.")
        else:
        	text = text.casefold().split('\n')
        	for i in range(len(text)):
        		bot.sendMessage(chat_id, "Searching "+ text[i] + ".com ...")
        		CheckDomain(text[i], chat_id)

    else:
        bot.sendMessage(chat_id, "Don't send me files, please...")

        	
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
