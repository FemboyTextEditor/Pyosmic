import os
import subprocess

if os.path.isfile('playerData.json'):
    subprocess.run(['python', 'launch.py'])
else:
    subprocess.run(['python', 'setup.py'])