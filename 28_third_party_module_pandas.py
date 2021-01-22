import time
import os
import pandas

while True:
    if os.path.exists('Resources/temps_today.csv'):
        data = pandas.read_csv('Resources/temps_today.csv')
        print(data.mean())
    else:
        print('file does not exist.')
    time.sleep(10)