# CheckDomain

Quanto può essere lungo e noioso cercare se una serie di domini sono già stati presi? 
Con questo script python il controllo risulta rapido ed efficiente, sfruttando un sito di domini, chiamato [GoDaddy](https://it.godaddy.com/) e le sue API.
<hr>

## Features
* Possibilità di scegliere una lista di domini da un file .json (esempio: [animal.json](https://github.com/fillics/CheckDomain/blob/main/animals.json), array di nomi presi da questo [link](https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a)) oppure da un file di testo che può creare l'utente.
* Creazione di un file di testo con tutti i domini disponibili, direttamente nella cartella dello script .py.

## Requisiti
* Python (3 o superiore)
* Moduli requests, json: scaricabili con ```pip install requests``` e ```pip install json```
* [GoDaddy API Keys](https://developer.godaddy.com/keys)

## Come funziona
Per prima cosa, registrarsi al sito di [GoDaddy API](https://developer.godaddy.com/) per ottenere le chiavi di accesso per lo script. Una volta ottenute, sostituirle nel file (
