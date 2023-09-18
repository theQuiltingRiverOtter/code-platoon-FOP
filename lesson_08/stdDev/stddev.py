class Person:
    """Create a person object with name and age"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


def std_dev(people: list) -> int:
    """calculate the standard deviation of a list of person objects"""
    mean = avg_person(people)
    sq_differences = []
    for person in people:
        sq_dif = (person.get_age() - mean) ** 2
        sq_differences.append(sq_dif)
    variance = avg(sq_differences)
    return variance**0.5


def avg_person(people: list) -> int:
    """Calculate the average age of a list of person objects"""
    total = 0
    for person in people:
        total += person.get_age()
    return total / len(people)


def avg(numbers: list) -> int:
    """calculate the average of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


# Create 3 people objects
p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Beatrice", 48)

person_list = [p1, p2, p3]
answer = std_dev(person_list)

print(answer)
