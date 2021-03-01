class Location:
    
    def __init__(self, name, country):
        self.name = name
        self.country = country

loc = Location("Kalil", "Belgium")

print(loc.name)
print(loc.country)

print(type(loc))

