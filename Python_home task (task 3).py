postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}

postcards['Petra'] = 'Paris'
postcards['Ivan'] = 'Moscow'
postcards['Oleg'] = 'Sydney'

unique_cities = set()

for i in postcards:
    unique_cities.add(postcards[i])

print(*unique_cities)