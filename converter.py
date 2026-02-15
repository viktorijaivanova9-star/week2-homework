# Konversijas koeficienti
KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

def km_mi():
    print("Virziens: 1) km -> mi  2) mi -> km")
    choice = input("> ")
    value = input("Ievadi vērtību: ")
    try:
        value = float(value)
        if choice == "1":
            print(f"{value:.2f} km = {value * KM_TO_MI:.2f} mi")
        elif choice == "2":
            print(f"{value:.2f} mi = {value / KM_TO_MI:.2f} km")
        else:
            print("Nepareizs virziens")
    except ValueError:
        print("Lūdzu ievadi skaitli")

# Līdzīgi funkcijas kg_lb(), l_gal(), usd_eur() …

def main():
    print("Izvēlies konversiju: 1) km<->mi  2) kg<->lb  3) L<->gal  4) $<->€")
    choice = input("> ")
    if choice == "1":
        km_mi()
    elif choice == "2":
        kg_lb()
    elif choice == "3":
        l_gal()
    elif choice == "4":
        usd_eur()
    else:
        print("Nepareiza izvēle")

if __name__ == "__main__":
    main()
