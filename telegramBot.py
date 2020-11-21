from credentials import API_KEY, API_SECRET, TOKEN
import sys, telepot, json, time
from telepot.loop import MessageLoop
from pprint import pprint
import requests
import os, telebot


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    
    if content_type == 'text':
        text = msg['text']
        if text == '/start':
            bot.sendMessage(chat_id, "Hi! Text me the domain to check out.")
            bot.sendMessage(chat_id, "Don't write .com, but only the domain name. Thank you!")
        elif text == '/help':
            bot.sendMessage(chat_id, "Sometimes GoDaddy API doesn't work and it says that a domain is avalaible when it's not and I don't know why. To check if the domain is available, click the link that the script sends to you. Visit: https://github.com/fillics/CheckDomain if you need help")
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


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

while 1:
  time.sleep(10)
