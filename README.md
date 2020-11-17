# CheckDomain [![](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/)
Check out the availability of a list of domains.

## What is it?
Do you want to know if a domain .com is available? With this script, you could find out the availability of a domain or a list of domains, saved in a JSON file or a text file.

### Telegram BOT
I've also created a Telegram bot ([@CheckDomainAPI_bot](https://web.telegram.org/#/im?p=%40CheckDomainAPI_bot)) that does the same thing of [CheckDomain.py](CheckDomain.py) script. 
You can send to it a JSON/txt file or just texting the domain to check out.

## Technologies
This script is created with:
* [Python](https://www.python.org/downloads/windows/), if you are using Windows, add it to the PATH ([guide](https://datatofish.com/add-python-to-windows-path/))  
* [requests](https://pypi.org/project/requests/) and json modules. You can easily download with ```pip install requests``` and ```pip install ijson``` (if ijson does not work, use jsonlib)
* [GoDaddy API Keys](https://developer.godaddy.com/keys)

## How does it work?
1) Create a [GoDaddy](https://developer.godaddy.com/) account to get the API Keys needed.
![Immagine](https://user-images.githubusercontent.com/24494773/99223251-73936b80-27e4-11eb-9b17-930e354574e0.png)
2) Insert them into the file [credentials.py](credentials.py).
3) Edit the file [domains.txt](domains.txt) with the list of domains that you want to check out (don't add .com, but only write the name of the website).
4) Run the script, using `python CheckDomain.py`, in the terminal.
After that, the script asks you which file to open, with the command line: 
``` choice = int(input("Text file [1] or Json file [2]? ")) ```

5) The script opens the file and reads the domains' name and for each domain, it executes a **request get**, one by one, throught the GoDaddy API.
6) If the domain is available, it will save in a text file, called AvailableWebsites.txt, with the command line: 

```
f = open('AvailableWebsites.txt', 'w')
f.write(name+'.com is available\r\n')
```

