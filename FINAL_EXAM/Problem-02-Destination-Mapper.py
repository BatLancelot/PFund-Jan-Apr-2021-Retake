import re

regex = r"(=|/)([A-Za-z]{3,})\1"

test_str = input()

matches = re.findall(regex, test_str)

travel_points = 0
all_dest = []

for dest in matches:
    destination = dest[1]
    travel_points += len(destination)
    all_dest.append(destination)

print(f"Destinations: {', '.join(all_dest)}\nTravel Points: {travel_points}")
