import logging


def add_two_number(nb_1: int, nb_2: int = 0):
    logging.info(f"Inside add function. Parameter to add {nb_1} and {nb_2}")
    return nb_1 + nb_2
