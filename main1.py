import tkinter as tk
from tkinter import messagebox
from models.person import Person
from models.apartment import Apartment
from services.data_service import DataService
from services.report_service import ReportService

class HouseManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("House Management App")
        root.geometry("460x280")

        self.data_service = DataService()
        self.report_service = ReportService()
        self.apartments = self.data_service.load_data()

        self.create_widgets()

    def create_widgets(self):

        tk.Button(self.root, text="Add Apartment", command=self.add_apartment).pack()
        tk.Button(self.root, text="Remove Apartment", command=self.remove_apartment).pack()
        tk.Button(self.root, text="Add Resident", command=self.add_resident).pack()
        tk.Button(self.root, text="Remove Resident", command=self.remove_resident).pack()
        tk.Button(self.root, text="Residents Report", command=self.residents_report).pack()
        tk.Button(self.root, text="Apartments Report", command=self.apartments_report).pack()
        tk.Button(self.root, text="Apartment Info", command=self.apartment_info).pack()
        tk.Button(self.root, text="Floor Report", command=self.floor_report).pack()
        tk.Button(self.root, text="Type Report", command=self.type_report).pack()
        tk.Button(self.root, text="Save and Exit", command=self.save_and_exit).pack()

    def add_apartment(self):
        window = tk.Toplevel(self.root)
        window.title("Add Apartment")

        tk.Label(window, text="Apartment Number:").grid(row=0, column=0)
        number_entry = tk.Entry(window)
        number_entry.grid(row=0, column=1)

        tk.Label(window, text="Floor Number:").grid(row=1, column=0)
        floor_entry = tk.Entry(window)
        floor_entry.grid(row=1, column=1)

        tk.Label(window, text="Apartment Type:").grid(row=2, column=0)
        type_entry = tk.Entry(window)
        type_entry.grid(row=2, column=1)

        def add():
            try:
                number = int(number_entry.get())
                floor = int(floor_entry.get())
                type = type_entry.get()
                self.apartments.append(Apartment(number, floor, type))
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Add", command=add).grid(row=3, column=0, columnspan=2)

    def remove_apartment(self):
        window = tk.Toplevel(self.root)
        window.title("Remove Apartment")

        tk.Label(window, text="Apartment Number:").grid(row=0, column=0)
        number_entry = tk.Entry(window)
        number_entry.grid(row=0, column=1)

        def remove():
            try:
                number = int(number_entry.get())
                self.apartments = [a for a in self.apartments if a.number != number]
                window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Remove", command=remove).grid(row=1, column=0, columnspan=2)

    def add_resident(self):
        window = tk.Toplevel(self.root)
        window.title("Add Resident")

        tk.Label(window, text="Apartment Number:").grid(row=0, column=0)
        number_entry = tk.Entry(window)
        number_entry.grid(row=0, column=1)

        tk.Label(window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=1, column=1)

        tk.Label(window, text="Surname:").grid(row=2, column=0)
        surname_entry = tk.Entry(window)
        surname_entry.grid(row=2, column=1)

        tk.Label(window, text="Phone:").grid(row=3, column=0)
        phone_entry = tk.Entry(window)
        phone_entry.grid(row=3, column=1)

        def add():
            try:
                number = int(number_entry.get())
                name = name_entry.get()
                surname = surname_entry.get()
                phone = phone_entry.get()
                person = Person(name, surname, phone)

                for apartment in self.apartments:
                    if apartment.number == number:
                        apartment.add_resident(person)
                        window.destroy()
                        return

                messagebox.showerror("Error", "Apartment not found")  # Якщо квартира не знайдена
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Add", command=add).grid(row=4, column=0, columnspan=2)

    def remove_resident(self):
        window = tk.Toplevel(self.root)
        window.title("Remove Resident")

        tk.Label(window, text="Apartment Number:").grid(row=0, column=0)
        number_entry = tk.Entry(window)
        number_entry.grid(row=0, column=1)

        tk.Label(window, text="Resident Name:").grid(row=1, column=0)
        name_entry = tk.Entry(window)
        name_entry.grid(row=1, column=1)

        def remove():
            try:
                number = int(number_entry.get())
                name = name_entry.get()

                for apartment in self.apartments:
                    if apartment.number == number:
                        for resident in apartment.residents:
                            if resident.name == name:
                                apartment.remove_resident(resident)
                                window.destroy()
                                return
                        messagebox.showerror("Error", "Resident not found in apartment")
                        return

                messagebox.showerror("Error", "Apartment not found")
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Remove", command=remove).grid(row=2, column=0, columnspan=2)

    def residents_report(self):
        report = self.report_service.generate_residents_report(self.apartments)
        self.show_report(report)

    def apartments_report(self):
        report = self.report_service.generate_apartments_report(self.apartments)
        self.show_report(report)

    def apartment_info(self):
        window = tk.Toplevel(self.root)
        window.title("Apartment Info")

        tk.Label(window, text="Apartment Number:").grid(row=0, column=0)
        number_entry = tk.Entry(window)
        number_entry.grid(row=0, column=1)

        def show_info():
            try:
                number = int(number_entry.get())
                info = self.report_service.generate_apartment_info(self.apartments, number)
                tk.Label(window, text=info).grid(row=2, column=0, columnspan=2)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Show Info", command=show_info).grid(row=1, column=0, columnspan=2)

    def floor_report(self):
        window = tk.Toplevel(self.root)
        window.title("Floor Report")

        tk.Label(window, text="Floor Number:").grid(row=0, column=0)
        floor_entry = tk.Entry(window)
        floor_entry.grid(row=0, column=1)

        def show_report():
            try:
                floor = int(floor_entry.get())
                report = self.report_service.generate_floor_report(self.apartments, floor)
                tk.Label(window, text=report).grid(row=2, column=0, columnspan=2)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(window, text="Show Report", command=show_report).grid(row=1, column=0, columnspan=2)

    def type_report(self):
        window = tk.Toplevel(self.root)
        window.title("Type Report")

        tk.Label(window, text="Apartment Type:").grid(row=0, column=0)
        type_entry = tk.Entry(window)
        type_entry.grid(row=0, column=1)

        def show_report():
            type_str = type_entry.get()
            report = self.report_service.generate_type_report(self.apartments, type_str)
            tk.Label(window, text=report).grid(row=2, column=0, columnspan=2)

        tk.Button(window, text="Show Report", command=show_report).grid(row=1, column=0, columnspan=2)

    def show_report(self, report):
        window = tk.Toplevel(self.root)
        window.title("Report")
        tk.Label(window, text=report).pack()

    def save_and_exit(self):
        self.data_service.save_data(self.apartments)
        self.root.destroy()

def main():
    root = tk.Tk()
    app = HouseManagementApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()