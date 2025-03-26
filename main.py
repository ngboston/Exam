from models.person import Person
from models.apartment import Apartment
from services.data_service import DataService
from services.report_service import ReportService

def main():
    data_service = DataService()
    report_service = ReportService()
    apartments = data_service.load_data()

    while True:
        print("\nHouse Management App")
        print("1. Add Apartment")
        print("2. Remove Apartment")
        print("3. Add Resident to Apartment")
        print("4. Remove Resident from Apartment")
        print("5. Residents Report")
        print("6. Apartments Report")
        print("7. Apartment Info")
        print("8. Floor Report")
        print("9. Type Report")
        print("10. Save and Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            number = int(input("Enter apartment number: "))
            floor = int(input("Enter floor number: "))
            type = input("Enter apartment type: ")
            apartments.append(Apartment(number, floor, type))
        elif choice == "2":
            number = int(input("Enter apartment number to remove: "))
            apartments = [a for a in apartments if a.number != number]
        elif choice == "3":
            number = int(input("Enter apartment number: "))
            name = input("Enter resident name: ")
            surname = input("Enter resident surname: ")
            phone = input("Enter resident phone: ")
            person = Person(name, surname, phone)
            for apartment in apartments:
                if apartment.number == number:
                    apartment.add_resident(person)
        elif choice == "4":
            number = int(input("Enter apartment number: "))
            name = input("Enter resident name to remove: ")
            for apartment in apartments:
                if apartment.number == number:
                    apartment.remove_resident(name)
        elif choice == "5":
            print(report_service.generate_residents_report(apartments))
        elif choice == "6":
            print(report_service.generate_apartments_report(apartments))
        elif choice == "7":
            number = int(input("Enter apartment number: "))
            print(report_service.generate_apartment_info(apartments, number))
        elif choice == "8":
            floor = int(input("Enter floor number: "))
            print(report_service.generate_floor_report(apartments, floor))
        elif choice == "9":
            type = input("Enter apartment type: ")
            print(report_service.generate_type_report(apartments, type))
        elif choice == "10":
            data_service.save_data(apartments)
            break

if __name__ == "__main__":
    main()