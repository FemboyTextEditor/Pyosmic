import json
import subprocess

print('Go to https://itch.io/user/settings/api-keys and extend the key and paste the whole key to the area below!')
APIKey = input('Insert itchio API Key: ')

jsonData = {
    'playerAPI': APIKey
}

with open('playerData.json', 'w') as file:
    json.dump(jsonData, file, indent=4)

subprocess.run(['python', 'main.py'])