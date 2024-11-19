import json

print('Do you want the game to update automatically? (answer with y/n)')
updater = input()
if updater == 'y':
    jsonUpdater = True
else:
    jsonUpdater = False

print('Do you want to link your itchio account to cosmic reach so that you can play multiplayer properly (answer with y/n)')
itchioacc = input()
if itchioacc == 'y':
    print('Go to https://itch.io/user/settings/api-keys and extend the key and paste the whole key to the area below!')
    APIKey = input('Insert itchio API Key: ')
else:
    APIKey = 'none'

jsonData = {
    'playerAPI': APIKey,
    'autoUpdater': jsonUpdater,
    'crVersion': 'none'
}

with open('playerData.json', 'w') as file:
    json.dump(jsonData, file, indent=4)