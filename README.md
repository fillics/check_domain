# CheckDomain

Quanto può essere lungo e noioso cercare se una serie di domini sono già stati presi? 
Con questo script python il controllo risulta rapido ed efficiente, sfruttando un sito di domini, chiamato [GoDaddy](https://it.godaddy.com/) e le sue API.
Tutto quello che devi fare è modificare il file [domains.txt](https://github.com/fillics/CheckDomain/blob/main/domains.txt), con la serie di domini che vuoi che lo script controlli e il gioco è fatto. Verrà creato un file con tutti quei domini che sono disponibili.
<hr>

## Features
* Possibilità di scegliere una lista di domini da un file .json (esempio: [animal.json](https://github.com/fillics/CheckDomain/blob/main/animals.json), array di nomi presi da questo [link](https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a)) oppure da un file di testo (esempio: [domains.txt](https://github.com/fillics/CheckDomain/blob/main/domains.txt), che contiene migliaia di nomi generati casualmente, che possono essere modificati) che può modificare/creare l'utente.
* Creazione di un file di testo con tutti i domini disponibili, direttamente nella cartella dello script .py.

## Prequisiti
* Python (3 o superiore): installare [Python](https://www.python.org/downloads/windows/) e, se si è su Windows, aggiungerlo al PATH di Windows ([guida](https://datatofish.com/add-python-to-windows-path/)) 
* Moduli requests, json: scaricabili con ```pip install requests``` e ```pip install ijson```
* [GoDaddy API Keys](https://developer.godaddy.com/keys)

## Come funziona
1) Registrarsi al sito di [GoDaddy API](https://developer.godaddy.com/) per ottenere le chiavi di accesso per lo script.

![Immagine](https://user-images.githubusercontent.com/24494773/99223251-73936b80-27e4-11eb-9b17-930e354574e0.png)

2) Sostituire le chiavi ottenute nel file [credentials.py](https://github.com/fillics/CheckDomain/blob/main/credentials.py). 
3) Modificare file _domains.txt_ con i domini che si vogliono controllare (non aggiungere il .com, ma semplicemente digitare il nome del sito. Esempio: _provadominio_ )
4) Eseguire lo script con il comando, da terminale, `python CheckDomain.py`.
A quel punto, il programma chiederà all'utente di inserire una preferenza riguardo al file da prendere in ingresso, con il comando ```choice = int(input("Text file [1] or Json file [2]? "))```.
5)Dopo aver scelto, lo script eseguirà una **request get** dopo l'altra, attraverso il sito di GoDaddy API, per trovare il dominio che ha _True_ come attributo _available_ del response body della request.

Se il dominio è disponibile, esso verrà stampato a video e verrà scritto su un file di testo, chiamato AvailableWebsites.txt, tramite il comando:

```
f = open('AvailableWebsites.txt', 'w')
f.write(name+'.com is available\r\n')
```
