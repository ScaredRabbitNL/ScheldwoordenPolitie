# ScheldwoordenPolitie

## Het project
Dit is een project, gemaakt door mij (en mijn groepsgenoten) als project voor de [Raspberry PI Competitie](https://www.paconsulting.com/culture/pa-in-the-community/raspberry-pi-competition-nederland) voor het vak informatica. Het idee achter het project is dat wanneer er dingen worden gezegd die voor iemand kwetsend kunnen overkomen, en die persoon niet instaat is om zijn/haar échte gevoelens over datgene wat gezegd is te uiten, de raspberry pi ingrijpt en laat weten dat er potentiële kwetsende dingen zijn gezegd. Dat doet de pi door om de tien seconden audio op te nemen, de audio te laten analyseren door AI (Speech To Text). Daar komt dan een tekst uitrollen en die wordt dan naar een (andere) AI gestuurd om de tekst te laten analyseren op een schaal van 1 - 10 waarbij 1 heel onvriendelijk is en 10 heel vriendelijk is. Als de waarde kleiner of gelijk is aan drie dan gaat het alarm af. Wij sturen de data naar de AI's door middel van API Requests.


## Aan de slag
Begin met het clonen van deze repository in een nieuwe map. Creëer vervolgens een nieuwe virtual environment van python (venv) d.m.v. het volgende commando: 
```bash
python -m venv <VenvNaam>
```
Let op dat de venv gecreëerd moet worden in de map waarin de repo gecloned is. Activeer de venv door het volgende commando te runnen in de terminal:

Windows:
```bash

```
### Vereisten
Onze code is geschreven in python. Daar zijn de volgende bibliotheken voor nodig:
- gpiozero
- lgpio
- pigpio
- assemblyai
- mistralai
- dotenv (python-dotenv)

Je kunt deze bibliotheken installeren door de volgende twee commando's:
```bash

```
## AI-Verklaring
