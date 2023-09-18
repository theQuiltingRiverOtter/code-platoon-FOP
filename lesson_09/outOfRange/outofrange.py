class OutofRangeError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message

    def __repr__(self):
        return self._message


def name_the_number(number: int) -> None:
    if number == 1:
        print("one")
    elif number == 2:
        print("two")
    elif number == 3:
        print("three")
    else:
        raise OutofRangeError("That's not one of the allowed values!")


try:
    name_the_number(1)
    name_the_number(4)
except OutofRangeError as error:
    print(error)
