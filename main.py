import logging
from enum import Enum
from operations_service import add, subtraction
import requests
import json


class Operation(Enum):
    ADD = "1" or "add"
    SUBTRACTION = "2" "substraction"
    MULTIPLICATION = "3" or "multiplication"


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

    if Operation.ADD.value == operation or Operation.ADD.name == operation:
        result = add.add_two_number(nb1, nb2)
    elif Operation.SUBTRACTION.value == operation or Operation.SUBTRACTION.name == operation:
        result = subtraction.subs_two_number(nb1, nb2)
    elif Operation.MULTIPLICATION.value == operation or Operation.MULTIPLICATION.name == operation:
        result = "Not implemented yet"
    print("You result is " + str(result))
    # print("and now: ")
    # toto()


if __name__ == '__main__':
    main()
