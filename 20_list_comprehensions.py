temps = [221, 234, 340, 230]
new_temps = [temp/10 for temp in temps]
print(new_temps)


temps1  = [221, 234, 340, -9999, 230]
new_temps1 = [temp/10 for temp in temps1 if temp != -9999]
print(new_temps1)


temps2  = [221, 234, 340, -9999, 230]
new_temps2 = [temp/10 if temp != -9999 else 0 for temp in temps2]
print(new_temps2)