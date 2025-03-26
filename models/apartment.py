class Apartment:
    def __init__(self, number, floor, type):
        self.number = number
        self.floor = floor
        self.type = type
        self.residents = []

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        self.residents.remove(person)

    def __str__(self):
        return f"Apartment {self.number}, Floor: {self.floor}, Type: {self.type}, Residents: {', '.join(str(r) for r in self.residents)}"