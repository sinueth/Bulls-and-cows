"""
Projekt: Bulls & Cows
Autor: sinueth
"""

import random
import time

DELKA_CISLA = 4
ODDELOVAC = "-" * 47


def generuj_tajne_cislo() -> str:
    """
    Vygeneruje tajné číslo o délce DELKA_CISLA.

    Číslice jsou unikátní a číslo nezačíná nulou.
    """
    prvni_cislo = random.randint(1, 9)
    # zbylé číslice vybíráme z 0-9 bez té, která už je na první pozici
    zbyva_cisel = list(range(10))
    zbyva_cisel.remove(prvni_cislo)
    zbytek_cisel = random.sample(zbyva_cisel, DELKA_CISLA - 1)
    # převedeme čísla na text a spojíme do jednoho řetězce
    return str(prvni_cislo) + "".join(map(str, zbytek_cisel))


def intro() -> None:
    """Vypíše úvodní text hry."""
    print(r"""
   ____        _ _         ___    ____
  | __ ) _   _| | |___    ( _ )  / ___|_____      _____
  |  _ \| | | | | / __|   / _ \ | |   / _ \ \ /\ / / __|
  | |_) | |_| | | \__ \  | (_) || |__| (_) \ V  V /\__ \
  |____/ \__,_|_|_|___/   \___/  \____\___/ \_/\_/ |___/

        \^__^                      (__)
        (oo)\_______               (oo)\_______
        (__)\       )\/\           (__)\       )\/\
            ||----w |                  ||----w |
            ||     ||                  ||     ||
    """)
    print("Hi there!")
    print(ODDELOVAC)
    print(f"I've generated a random {DELKA_CISLA} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(ODDELOVAC)


def hadej_cislo() -> str:
    """
    Načte tip od uživatele a ověří ho.

    Kontroluje délku, jen číslice, nulu na začátku a duplicity.
    Opakuje dotaz, dokud tip není platný, a pak ho vrátí.
    """
    while True:
        tip = input("Enter a number: ").strip()
        if len(tip) != DELKA_CISLA:
            print(f"Your guess must be {DELKA_CISLA} digits long.")
        elif not tip.isdigit():
            print("Your guess must contain only digits.")
        elif tip[0] == "0":
            print("Your guess cannot start with zero.")
        elif len(set(tip)) != DELKA_CISLA:
            print("Your guess must have unique digits.")
        else:
            return tip


def vyhodnot_tip(tip: str, tajne_cislo: str) -> tuple[int, int]:
    """Vrátí počet bulls a cows pro daný tip."""
    bulls = sum(1 for i in range(DELKA_CISLA) if tip[i] == tajne_cislo[i])
    # všechny shodné číslice minus ty, které už jsou bulls
    cows = sum(1 for cislo in tip if cislo in tajne_cislo) - bulls
    return bulls, cows


def format_vysledek(bulls: int, cows: int) -> str:
    """Vrátí výsledek ve tvaru '1 bull, 2 cows'."""
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def main() -> tuple[int, float]:
    """Odehraje jednu hru a vrátí počet pokusů a dobu hraní."""
    intro()
    tajne_cislo = generuj_tajne_cislo()
    start_time = time.time()
    counter = 0
    bulls = 0
    while bulls != DELKA_CISLA:
        tip = hadej_cislo()
        counter += 1
        bulls, cows = vyhodnot_tip(tip, tajne_cislo)
        print(format_vysledek(bulls, cows))
        print(ODDELOVAC)
    return counter, time.time() - start_time


if __name__ == "__main__":
    statistiky = []
    try_again = True
    while try_again:
        counter, elapsed_time = main()
        statistiky.append(counter)
        guess_text = "guess" if counter == 1 else "guesses"
        print("Correct, you've guessed the right number")
        print(f"in {counter} {guess_text}!")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Games played: {len(statistiky)}, best: {min(statistiky)}, "
              f"average: {sum(statistiky) / len(statistiky):.1f}")
        print(ODDELOVAC)
        print("That's amazing!")
        try_again = input("Try again? (y/n) ").strip().lower() == "y"