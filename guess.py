import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Esmu izvēlējies skaitli no 1 līdz 100.")
    print("Tev ir 10 mēģinājumi.")

    while attempts < max_attempts:
        guess_input = input("Tavs minējums: ")

        # Ievades validācija
        try:
            guess = int(guess_input)
        except ValueError:
            print("Lūdzu ievadi veselu skaitli.")
            continue  # spēle turpinās

        attempts += 1

        if guess < secret_number:
            print("Par mazu.")
        elif guess > secret_number:
            print("Par lielu.")
        else:
            print(f"Apsveicu! Uzminēji {attempts} mēģinājumos.")
            return  # beidz spēli

    # Ja sasniegts mēģinājumu limits
    print("Mēģinājumi beigušies.")
    print(f"Pareizā atbilde bija: {secret_number}")


def main():
    while True:
        play_game()
        again = input("Vai vēlies spēlēt vēlreiz? (j/n): ").lower()

        if again != "j":
            print("Paldies par spēli!")
            break


if __name__ == "__main__":
    main()
