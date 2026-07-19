class Laserprinter:
    def print_document(self):
        print(f"Laser printing")

class Inkjetprinter:
    def print_document(self):
        print(f"Inkjet printing")

class Thermalprinter:
    def print_document(self):
        print(f"Thermal printing")

def print_with_printer(printer):
    printer.print_document()

print_with_printer(Laserprinter())
print_with_printer(Inkjetprinter())
print_with_printer(Thermalprinter())
