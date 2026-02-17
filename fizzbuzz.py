import sys

def fizzbuzz(n, rules):
    for i in range(1, n + 1):
        output = ""

        for divisor, word in rules:
            if i % divisor == 0:
                output += word

        print(output if output else i)


def main():
    # Pārbaude: vai ir arguments
    if len(sys.argv) < 2:
        print("Lūdzu norādi skaitli N. Piemērs: python fizzbuzz.py 15")
        return

    # Pārbaude: vai N ir skaitlis
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N jābūt veselam skaitlim.")
        return

    # Dalāmības noteikumi (var paplašināt)
    rules = [
        (3, "Fizz"),
        (5, "Buzz"),
        (7, "Jazz")  # bonuss
    ]

    fizzbuzz(n, rules)


if __name__ == "__main__":
    main()
