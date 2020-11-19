from credentials import API_KEY, API_SECRET, TOKEN
import sys, telepot, json
from telepot.loop import MessageLoop
from pprint import pprint
import requests
import os, telebot
from flask import Flask

server = Flask(__name__)

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


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# SERVER SIDE 
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='YOUR_HEROKU_APP_URL' + TOKEN)
   return "!", 200

if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
