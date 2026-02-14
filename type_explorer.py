# Uzdevums 1: Tipu pētnieks
# --------------------------------------------------
# 1) Pamata tipu piešķiršana (vismaz viens piemērs katram no: str, int, float, bool, None)
# --------------------------------------------------
name = "Anna"                 # str
salute = 'Sveiki, pasaule!'     # str (var lietot dubultās vai vienkāršās pēdiņas)
age = 17                        # int (vesels skaitlis)
year_of_birth = 2008            # int
height_m = 1.72                 # float (decimāldaļas skaitlis)
pi_approx = 3.14159             # float
is_student = True               # bool (True / False)
has_pet = False                 # bool
middle_name = None              # NoneType — nozīmē "nav vērtības / tukšs"

# Drukājam vērtības un to tipu
print("--- Pamata piešķiršana ---")
variables = {
    'name': name,
    'salute': salute,
    'age': age,
    'year_of_birth': year_of_birth,
    'height_m': height_m,
    'pi_approx': pi_approx,
    'is_student': is_student,
    'has_pet': has_pet,
    'middle_name': middle_name,
}
for var, val in variables.items():
    print(f"{var:14} = {val!r:12}   (type: {type(val).__name__})")

# --------------------------------------------------
# 2) Teksta un skaitļu savienošana: kļūdas un pareizie veidi
# --------------------------------------------------
print('\n--- Teksta un skaitļu savienošana (konkatenācija) ---')
# Šis radīs TypeError: nevar + savienot str un int tieši
print("Piemērs: mēģinājums apvienot string + int ->" )
try:
    bad = "Age: " + age        # kļūda
except TypeError as e:
    print("  Neizdevās:", e)

# Pareizie veidi:
print('  Risinājumi:')
print("    f-string:", f"Age: {age}")
print("    str():", "Age: " + str(age))

# --------------------------------------------------
# 3) Int un float mijiedarbība (aritmētika)
# --------------------------------------------------
print('\n--- int un float aritmētika ---')
print(f"{age} + {height_m} -> {age + height_m}   (type: {type(age + height_m).__name__})")
print(f"{pi_approx} * 2 -> {pi_approx * 2}   (type: {type(pi_approx * 2).__name__})")

# Ja nepieciešams vesels skaitlis no float, var izmantot int() — tas noņem decimāldaļu (noapaļo uz leju).
f = 9.99
print(f"int({f}) -> {int(f)}   (noapaļo uz leju / šķeļ decimāldaļu)")

# --------------------------------------------------
# 4) Bool un to skaitliskā uzvedība
# --------------------------------------------------
print('\n--- bool tipa uzvedība skaitļos ---')
print(f"True kā int -> {int(True)}")
print(f"False kā int -> {int(False)}")
print(f"True + 1 -> {True + 1}  (bool darbojas kā 1 vai 0 skaitliskā kontekstā)")

# Bool no dažādiem tipi: tukšums / 0 / False -> False; pārējais -> True
print('Example: bool(0) ->', bool(0))
print('Example: bool("") ->', bool(""))
print('Example: bool("0") ->', bool("0"))
print('Example: bool(None) ->', bool(None))

# --------------------------------------------------
# 5) None tips — ko drīkst un ko nedrīkst
# --------------------------------------------------
print('\n--- None uzvedība ---')
print('middle_name =', middle_name, '(type:', type(middle_name).__name__ + ')')
# str(None) ir 'None', bet int(None) izmet kļūdu
print('str(None) ->', str(None))
try:
    print('int(None) ->', int(None))
except TypeError as e:
    print('  Neizdevās int(None):', e)

# Droša pārbaude pirms operācijām ar None
if middle_name is None:
    print('  middle_name nav piešķirts — pirms lietošanas pārliecinieties, ka tas nav None')

# --------------------------------------------------
# 6) Pārveidošanas (casting) piemēri un biežāk sastopamās kļūdas
# --------------------------------------------------
print('\n--- Tipu pārveidošana (casting) ---')
# No string uz int (str jābūt pareizam vesela skaitļa tekstam)
s1 = "42"
s2 = "3.14"

print(f"int('{s1}') ->", int(s1))
try:
    print(f"int('{s2}') ->", int(s2))  # kļūda: '3.14' nav vesels skaitlis
except ValueError as e:
    print('  Neizdevās int(s2):', e)

# Pareizais ceļš no '3.14' uz int — vispirms float, tad int (noapaļo uz leju)
print("float('3.14') ->", float(s2))
print("int(float('3.14')) ->", int(float(s2)))

# No int uz str
n = 100
print('str(100) ->', str(n))

# No bool uz str / int
print('str(True) ->', str(True))
print('int(False) ->', int(False))

# Droša pārveidošana, ja neesam pārliecināti — izmantojam try/except
user_input = "not_a_number"
print('\nDroša pārveidošana ar try/except:')
try:
    x = int(user_input)
    print('konvertēts:', x)
except ValueError:
    print("Nevar konvertēt '", user_input, "' uz int — lietotāja ievade nav derīgs vesels skaitlis.")

# --------------------------------------------------
# 7) Tipu noteikšana un isinstance() — kā kontrolēt tipu pirms operācijām
# --------------------------------------------------
print('\n--- Tipu pārbaude ---')
print('isinstance(age, int) ->', isinstance(age, int))
print('isinstance(height_m, float) ->', isinstance(height_m, float))
print('isinstance(name, (str,)) ->', isinstance(name, (str,)))

# Piemērs: tikai veic darbību, ja ir pareizs tips
maybe_number = '123'
if isinstance(maybe_number, str):
    print('maybe_number ir string — var mēģināt to parsēt uz int')

# --------------------------------------------------
# 8) Kopsavilkums — praktiski padomi
# --------------------------------------------------
print('\n--- Kopsavilkums un praktiskie padomi ---')
print('- Pirms savienošanu ("+") starp str un skaitļiem pārvēršiet skaitļus uz str vai izmantojiet f-strings.')
print('- Kad pārvēršat string uz int/float, pārliecinieties, ka string satur derīgu formātu (izmantojiet try/except).')
print('- bool darbojas arī kā skaitļi (True==1, False==0) — izmantojiet to apdomīgi, bet izmantošana var būt noderīga.')
print('- None nav tas pats, kas "" vai 0. To jāpārbauda ar "is None".')
print('\nGatavs! Palaidiet skriptu un eksperimentējiet ar vērtībām.')
