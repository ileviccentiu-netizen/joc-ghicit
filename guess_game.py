import random

def joc_ghicit_numar():
    print("Bine ai venit la jocul de ghicit numărul!")
    numar_secret = random.randint(1, 100)
    incercari = 0

    while True:
        try:
            ghicit = int(input("Ghicește un număr între 1 și 100: "))
            incercari += 1
            if ghicit < numar_secret:
                print("Numărul este mai mare!")
            elif ghicit > numar_secret:
                print("Numărul este mai mic!")
            else:
                print(f"Felicitări! Ai ghicit numărul {numar_secret} în {incercari} încercări.")
                break
        except ValueError:
            print("Te rog introdu un număr valid.")

if __name__ == "__main__":
    joc_ghicit_numar()
