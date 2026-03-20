# ScheldwoordenPolitie (SwearwordPolice)
Dit is een project dat ik (samen met mijn klasgenoten) heb gemaakt voor de Raspberry Pi-wedstrijd in onze informatica-les. Het idee achter het project is dat wanneer er dingen worden gezegd die voor iemand kwetsend kunnen zijn, en die persoon niet in staat is om zijn of haar ware gevoelens over wat er is gezegd te uiten, de Raspberry Pi ingrijpt en hem of haar waarschuwt dat er mogelijk kwetsende dingen zijn gezegd. De Pi doet dit door elke tien seconden audio op te nemen en deze audio te laten analyseren door AI (Speech-to-Text). Dit genereert een tekst, die vervolgens naar een (andere) AI wordt gestuurd om de tekst te analyseren op een schaal van 1 tot 10, waarbij 1 erg onvriendelijk is en 10 erg vriendelijk. Als de waarde kleiner is dan of gelijk is aan drie, gaat het alarm af. We sturen de gegevens naar de AI's via API-verzoeken.

## Aan de slag

### Vereisten 
- Python 3.8+
- Een Raspberry Pi
- Een microfoon

Begin door deze repository te klonen en (in de terminal) naar de map te gaan die de gekloonde repository en de map src bevat. Gebruik vervolgens het volgende commando om een virtuele omgeving aan te maken: ``python -m venv $NAME`` 
$NAME is de naam die je aan de virtuele omgeving wilt geven.
Activeer vervolgens de virtuele omgeving door het volgende commando uit te voeren (afhankelijk van je besturingssysteem):

Windows
```bash
.\$NAME\Scripts\activate
```

Linux / Unix-gebaseerde systemen (inclusief Raspberry Pi OS)
```bash
source ./$NAME/bin/activate
```

Dit project is afhankelijk van de volgende bibliotheken: gpiozerolgpio, pigpio, assemblyai, mistralai en dotenv (python-dotenv). Let op: lgpio en pigpio zijn afhankelijkheden van gpiozero die soms niet kunnen worden gedownload. Voor de zekerheid hebben we het installatiecommando in tweeën gesplitst. Voer het volgende uit (in een geactiveerde venv): 
```bash
pip install gpiozero lgpio pigpio
pip install assemblyai mistralai dotenv
```
Dit project is ook afhankelijk van het alsa-utils-pakket voor Linux/Unix-gebaseerde systemen. Installeer dit met de volgende commando's:
```bash
sudo apt update && sudo apt upgrade
sudo apt install alsa-utils
```
Nadat alle afhankelijkheden zijn gedownload, voer je, afhankelijk van je platform, ofwel ``raspberry_pi_main.py`` ofwel ```windows_main.py``` uit.

## AI-verklaring
Omdat AI de reputatie heeft plagiaat te plegen en het ons gewoon eerlijk leek om dit te doen, hebben we besloten deze AI-verklaring op te nemen. We hebben AI gebruikt om **een deel** van onze code te maken wanneer we niet wisten hoe we verder moesten, of wanneer een specifiek persoon moe was.

## Licentie
Deze code is gelicentieerd onder de GNU GPLv3-licentie omdat deze eenvoudig en tolerant is. 



