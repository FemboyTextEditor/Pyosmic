import json
import requests
import os

jsonURL = 'https://raw.githubusercontent.com/CRModders/CosmicArchive/refs/heads/main/versions.json'
print('Downloading versions.json ...')
jsonRequest = requests.get(jsonURL, allow_redirects=True)
open('versions.json', 'wb').write(jsonRequest.content)

with open('versions.json', 'r') as file:
    gameVersionsJson = json.load(file)

currentVersionNumber = str(gameVersionsJson['latest']['pre_alpha'])

with open('playerData.json', 'r') as file:
    playerDataJson = json.load(file)

if playerDataJson['crVersion'] != currentVersionNumber:
    print('Installing Cosmic Reach ' + currentVersionNumber + ' (This may take a few minutes depending on your internet connection)')

    gameDownloadStr = 'https://raw.githubusercontent.com/CRModders/CosmicArchive/refs/heads/main/versions/pre-alpha/' + currentVersionNumber + '/client/Cosmic-Reach-' + currentVersionNumber + '.jar'
    gameDownloadRequest = requests.get(gameDownloadStr, allow_redirects=True)
    crVersionName = 'Cosmic-Reach-' + currentVersionNumber + '.jar'
    open(crVersionName, 'wb').write(gameDownloadRequest.content)
    try:
        os.remove('versions/cosmic_reach.jar')
        print('Successfully deleted previous version')
    except FileNotFoundError:
        print('ERROR: Old version could not be found (if this happens on your first run dont be worried this is normal)')
    os.rename(crVersionName, 'versions/cosmic_reach.jar')
    print('Finished update!')


    playerDataJson['crVersion'] = currentVersionNumber

    with open('playerData.json', 'w') as file:
        json.dump(playerDataJson, file, indent=4)
else:
    print('Everything is up to date!')


os.remove('versions.json')