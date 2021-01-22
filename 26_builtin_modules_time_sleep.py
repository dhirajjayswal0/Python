import time

while True:
    with open('Resources/Vegitables.txt') as file:
        print(file.read())
        time.sleep(10)