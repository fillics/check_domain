# CheckDomain

Quanto può essere lungo e noioso cercare se una serie di domini sono già stati presi? 
Con questo script python il controllo risulta rapido ed efficiente, sfruttando un sito di domini, chiamato [GoDaddy](https://it.godaddy.com/) e le sue API.
<hr>

## Features
* Possibilità di scegliere una lista di domini da un file .json (esempio: [animal.json](https://github.com/fillics/CheckDomain/blob/main/animals.json), array di nomi presi da questo [link](https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a)) oppure da un file di testo (esempio: [domains.txt](https://github.com/fillics/CheckDomain/blob/main/domains.txt), che contiene migliaia di nomi generati casualmente, che possono essere modificati) che può modificare/creare l'utente.
* Creazione di un file di testo con tutti i domini disponibili, direttamente nella cartella dello script .py.

## Requisiti
* Python (3 o superiore)
* Moduli requests, json: scaricabili con ```pip install requests``` e ```pip install json```
* [GoDaddy API Keys](https://developer.godaddy.com/keys)

## Come funziona
Per prima cosa, registrarsi al sito di [GoDaddy API](https://developer.godaddy.com/) per ottenere le chiavi di accesso per lo script. Una volta ottenute, sostituirle nel file [credentials.py](https://github.com/fillics/CheckDomain/blob/main/credentials.py). 

Dopo aver modificato il file _domains.txt_ con i domini che si vogliono controllare, far partire lo script con il comando, da terminale, `python CheckDomain.py`.
A quel punto, il programma chiederà all'utente di inserire una preferenza riguardo al file da prendere in ingresso, con il comando ```choice = int(input("Text file [1] or Json file [2]? "))```.
Dopo aver scelto, lo script eseguirà una **request get** dopo l'altra, attraverso il sito di GoDaddy API, per trovare il dominio che ha _True_ come attributo _available_ del response body della request.

Se il dominio è disponibile, esso verrà stampato a video e verrà scritto su un file di testo, chiamato AvailableWebsites.txt, tramite il comando:

```
f = open('AvailableWebsites.txt', 'w')
f.write(name+'.com is available\r\n')
```
