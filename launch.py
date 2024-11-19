import os
import json

with open('playerData.json', 'r') as file:
    APIJson = json.load(file)

if APIJson['playerAPI'] != 'none':
    itchIoAPIKey = str(APIJson['playerAPI'])

    if os.name == 'nt':
        setAPI = 'set ITCHIO_API_KEY=' + itchIoAPIKey
    elif os.name == 'posix':
        setAPI = 'export ITCHIO_API_KEY=' + itchIoAPIKey

    os.system(setAPI + '; java -jar versions/cosmic_reach.jar')
else:
    os.system('java -jar versions/cosmic_reach.jar')