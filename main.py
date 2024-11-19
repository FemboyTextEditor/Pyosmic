import os
import subprocess
import json

if not os.path.isfile('playerData.json'):
    subprocess.run(['python', 'setup.py'])

with open('playerData.json', 'r') as file:
    jsonContent = json.load(file)

if not jsonContent['autoUpdater'] and jsonContent['crVersion'] == 'none':
    subprocess.run(['python', 'updater.py'])
elif jsonContent['autoUpdater']:
    subprocess.run(['python', 'updater.py'])

subprocess.run(['python', 'launch.py'])