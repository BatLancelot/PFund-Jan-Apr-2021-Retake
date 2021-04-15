class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, spieces, name):
        if spieces == 'mammal':
            self.mammals.append(name)
        elif spieces == 'fish':
            self.fishes.append(name)
        elif spieces == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            return f'Mammals in {self.name}: {", ".join(self.mammals)}\nTotal animals: {Zoo.__animals}'
        if species == 'fish':
            return f'Fishes in {self.name}: {", ".join(self.fishes)}\nTotal animals: {Zoo.__animals}'
        if species == 'bird':
            return f'Birds in {self.name}: {", ".join(self.birds)}\nTotal animals: {Zoo.__animals}'


zoo_name = Zoo(input())
entries = int(input())

for _ in range(entries):
    spieces, name = input().split(' ')
    zoo_name.add_animal(spieces, name)

zoo_info = input()
print(zoo_name.get_info(zoo_info))
