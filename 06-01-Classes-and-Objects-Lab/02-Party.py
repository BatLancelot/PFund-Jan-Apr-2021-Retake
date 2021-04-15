class Party:
    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.name = name
        self.people.append(name)

    def participants(self):
        return ", ".join(party.people)

    def total_people(self):
        return len(party.people)


party = Party()

while True:
    name = input()
    if name == 'End':
        break
    party.add_people(name)


print(f'Going: {party.participants()}')
print(f'Total: {party.total_people()}')
