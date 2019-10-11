import logging
from enum import Enum
from operations_service import add, subtraction
import requests


class Operation(Enum):
    ADD = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3


def get_numbers():
    """
    Get user input (str) and cast into int
    :rtype: two variables cast int
    """
    print("please, give me two numbers")
    nb1 = input("nb1:")
    nb2 = input("nb2:")
    nb1 = int(nb1)
    nb2 = int(nb2)
    return nb1, nb2


def toto():
    url = "https://us-central1-sandbox-tlengyel.cloudfunctions.net/multiply "



def main():
    logging.info(f"starting a program calculator. Welcome!")
    nb1, nb2 = get_numbers()
    print("Good! now, tell me which operation would you like to do:\n1. Add\n"
          "2. Subtraction\n3. Multiplication (API CALL)")
    operation = input("your selection:")
    result = 0

    if Operation.ADD:
        result = add.add_two_number(nb1, nb2)
    elif Operation.SUBTRACTION:
        result = subtraction.subs_two_number(nb1, nb2)
    elif Operation.MULTIPLICATION:
        result = "Not implemented yet"
    print("You result is " + str(result))


if __name__ == '__main__':
    main()
