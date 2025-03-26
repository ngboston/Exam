class ReportService:
    def generate_residents_report(self, apartments):
        residents = []
        for apartment in apartments:
            residents.extend(apartment.residents)
        return "\n".join(str(r) for r in residents)

    def generate_apartments_report(self, apartments):
        return "\n".join(str(a) for a in apartments)

    def generate_apartment_info(self, apartments, apartment_number):
        for apartment in apartments:
            if apartment.number == apartment_number:
                return str(apartment)
        return "Apartment not found"

    def generate_floor_report(self, apartments, floor_number):
        floor_apartments = [a for a in apartments if a.floor == floor_number]
        return "\n".join(str(a) for a in floor_apartments)

    def generate_type_report(self, apartments, apartment_type):
        type_apartments = [a for a in apartments if a.type == apartment_type]
        return "\n".join(str(a) for a in type_apartments)