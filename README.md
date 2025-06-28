# VulnProject

VulnProject is a CTF like game, there are two section:
1) Server Attacks: this section covers SQL injection topics
2) Client Attacks: this section cover CSRF,Cookies and XSS (admin is simulated by selenium bot)

## Requirements
docker compose is all you need
## Installation

Do not change any file, just run 

```bash
docker compose build
docker compose up
```

## Usage
After visualize:
```bash
VulnProject-flaskapp-1  |  * Serving Flask app 'app'
VulnProject-flaskapp-1  |  * Debug mode: off
```
connect to your localhost http://127.0.0.1:5000/

## Exploits
If you are stuck you can consult /exploits directory
```bash
~/VulnProject/exploits$ ls
cookies_bruteforce.py  exfilFlag.js  level4_exploit.py  level5_exploit.py  level6_exploit.py  orange-cats.html

```
