# ScheldwoordenPolitie (SwearwordPolice)
This is a project created by me (and my classmates) for the Raspberry Pi Competition in our computer science class. The idea behind the project is that when things are said that might be hurtful to someone, and that person is unable to express their true feelings about what was said, the Raspberry Pi steps in and alerts them that potentially hurtful things have been said. The Pi does this by recording audio every ten seconds and having the audio analyzed by AI (Speech-to-Text). This generates a text, which is then sent to a (different) AI to analyze the text on a scale of 1 to 10, where 1 is very unfriendly and 10 is very friendly. If the value is less than or equal to three, the alarm goes off. We send the data to the AIs via API requests.

## Getting Started

### Prerequisites 
- Python 3.8+
- A raspberry pi
- A microphone

Get started by cloning this repository and (in the terminal) moving into the directory that contains the cloned repository and the src folder. Then use the following command to create a virtual environment: ``python -m venv $NAME`` 
$NAME is whatever you want the name of the virtual environment's name to be.
Then activate said virtual environment by running the following command (dependent on your operating system):

Windows
```bash
.\$NAME\Scripts\activate
```

Linux / Unix based systems (Includes Raspberry PI OS)
```bash
source ./$NAME/bin/activate
```

This project depends on the following libraries: gpiozero, lgpio, pigpio, assemblyai, mistralai and dotenv (python-dotenv). Note that lgpio and pigpio are dependencies of gpiozero that sometimes fail to download. To be absolutely sure, we've seperated the install command into two. Please run (in activated venv): 
```bash
pip install gpiozero lgpio pigpio
pip install assemblyai mistralai dotenv
```
This project is also dependent on the alsa-utils package for linux/unix based system. Install it by using the following commands:
```bash
sudo apt update && sudo apt upgrade
sudo apt install alsa-utils
```
After all dependencies have been downloaded, run either ``raspberry_pi_main.py`` or ```windows_main.py``` depending on your platform.

## AI-Declaration
Because AI has a reputation of plagiarism and it just seemed fair to do so, we decided to include this declaration of AI. We have used AI to create **some** of our code whenever we didn't know how to continue, or when a specific someone was tired.

## License
This code has been licensed under the GNU GPLv3 license because it is simple and permissive. 
