import matplotlib.pyplot as plt

with open('C://Users/Yura/Desktop/123/DS3.txt', 'r') as file:
    data = file.readlines()

coordinates = []
for line in data:
    x, y = map(int, line.split())
    coordinates.append((x, y))

plt.figure(figsize=(9.6, 5.4))

for coord in coordinates:
    plt.scatter(coord[0], coord[1], color='blue')

plt.xlim(0, 960)
plt.ylim(0, 540)

plt.savefig('result.png')
plt.show()
