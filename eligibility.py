# eligibility.py

def get_int_input(prompt):
    """Iegūst skaitlisku ievadi no lietotāja, pārbauda vai tas ir vesels skaitlis un pozitīvs."""
    while True:
        value = input(prompt)
        if not value.isdigit():
            print("Lūdzu, ievadi pozitīvu skaitli.")
            continue
        value_int = int(value)
        if value_int < 0:
            print("Vecums nevar būt negatīvs.")
            continue
        return value_int

def get_bool_input(prompt):
    """Iegūst lietotāja ievadi 'j' vai 'n' un pārvērš to bool."""
    while True:
        value = input(prompt).strip().lower()
        if value == 'j':
            return True
        elif value == 'n':
            return False
        else:
            print("Lūdzu, atbildi ar 'j' vai 'n'.")

# --- Ievade ---
vecums = get_int_input("Ievadi vecumu: ")
ir_aplieciba = get_bool_input("Vai ir autovadītāja apliecība? (j/n): ")
ir_students = get_bool_input("Vai ir students? (j/n): ")
ir_veterans = get_bool_input("Vai ir veterāns? (j/n): ")

# --- Pārbaudes ---
balsot = vecums >= 18
auto_ire = vecums >= 21 and ir_aplieciba
senioru_atlade = vecums >= 65 or ir_veterans
studentu_atlade = 16 <= vecums <= 26 and ir_students

# --- Rezultātu izvade ---
print("\n---")
print(f"Balsošana:         {'Jā ✓' if balsot else 'Nē ✗'}")
if auto_ire:
    print(f"Auto īre:          Jā ✓")
else:
    # precizē iemeslu
    if vecums < 21:
        print(f"Auto īre:          Nē ✗ (par jauns vecums)")
    elif not ir_aplieciba:
        print(f"Auto īre:          Nē ✗ (nav apliecības)")
    else:
        print(f"Auto īre:          Nē ✗")
print(f"Senioru atlaide:   {'Jā ✓' if senioru_atlade else 'Nē ✗'}")
print(f"Studentu atlaide:  {'Jā ✓' if studentu_atlade else 'Nē ✗'}")
