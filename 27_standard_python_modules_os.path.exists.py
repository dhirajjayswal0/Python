import time
import os

while True:
    if os.path.exists('Resources/Vegitables.txt'):
        with open('Resources/Vegitables.txt') as myfile:
            print(myfile.read())
    else:
        print('file does not exists.')
    time.sleep(10)