import os
import json

with open('playerData.json', 'r') as file:
    APIJson = json.load(file)

itchIoAPIKey = str(APIJson['playerAPI'])

if os.name == 'nt':
    setAPI = 'set ITCHIO_API_KEY=' + itchIoAPIKey
elif os.name == 'posix':
    setAPI = 'export ITCHIO_API_KEY=' + itchIoAPIKey

print('1 = Latest stable version')
print('2 = Latest private realease')

options = int(input('What version do you want to play?: '))

# options = 1

if options == 1:
    os.system(setAPI +'; java -jar versions/CR-0.3.6.jar')

if options == 2:
    print('Not found')
    #os.system(setAPI + '; java -jar versions/CR-0.3.2-pre10.jar')