from statistics import mean, median, mode


class Student:
    """Create a Student Object with two properties, name and grade"""

    def __init__(self, name: str, grade: int) -> None:
        self._name = name
        self._grade = grade

    def get_grade(self) -> int:
        return self._grade

    def get_name(self) -> str:
        return self._name


def basic_stats(students: list[Student]) -> tuple:
    """Takes list of student objects and returns a tuple of the mean, median, and mode of the student grades"""
    student_grades = [student.get_grade() for student in students]
    mn = mean(student_grades)
    md = median(student_grades)
    mo = mode(student_grades)
    return (mn, md, mo)


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values
