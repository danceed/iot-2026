class Printer:
    def __init__(self, name="Unknown", speed=0, price=0.0):
        
        self.__name = name
        self.__speed = speed
        self.__price = price

        self.warranty_years = 1
        self.connection_type = "USB"

    def get_name(self):
        return self.__name



    def get_speed(self):
        return self.__speed

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_speed(self, speed):
        self.__speed = speed

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return (
            f"Name: {self.__name}, "
            f"Speed: {self.__speed} pages/min, "
            f"Price: {self.__price} UAH, "
            f"Warranty: {self.warranty_years} year(s), "
            f"Connection: {self.connection_type}"
        )

    def __repr__(self):
        return (
            f"Printer(name={self.__name!r}, "
            f"speed={self.__speed!r}, "
            f"price={self.__price!r})"
        )

    def __del__(self):
        print(f"Printer {self.__name} is being destroyed.")


def main():
    printer1 = Printer()
    printer2 = Printer("HP LaserJet", 30, 6500.0)
    printer3 = Printer("Canon PIXMA", 15, 4200.0)
        

    printers = [printer1, printer2, printer3]

    for printer in printers:
        print(printer)
        print("Object representation:", repr(printer))
        print("Name:", printer.get_name())
        print("Speed:", printer.get_speed())
        print("Price:", printer.get_price())
        print("Warranty:", printer.warranty_years)
        print("Connection type:", printer.connection_type)
        print("-" * 60)


main()

