class LibraryItem:
    """Class for library item objects with an integer to represent the item id and a title"""

    def __init__(self, library_item_id: int, title: str) -> None:
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def __repr__(self):
        return f"ID: {self._library_item_id}, Title: {self._title}"

    def get_library_item_id(self) -> int:
        return self._library_item_id

    def get_location(self) -> str:
        return self._location

    def get_title(self) -> str:
        return self._title

    def get_checked_out_by(self) -> str:
        return self._checked_out_by

    def get_requested_by(self) -> str:
        return self._requested_by

    def get_date_checked_out(self) -> int:
        return self._date_checked_out

    def update_checked_out_by(self, person: str) -> None:
        self._checked_out_by = person

    def update_location(self, loc: str) -> None:
        self._location = loc

    def check_out(self, person: str, day: int) -> None:
        """updates person checked out, date checked out, and location"""
        self.update_checked_out_by(person)
        self._date_checked_out = day
        self.update_location("CHECKED_OUT")

    def update_requested_by(self, person: str) -> None:
        # updates who it is requested by
        if self._requested_by == person:
            self._requested_by = None
        else:
            self._requested_by = person


class Book(LibraryItem):
    """Extension of LibraryItem class with author and check out length"""

    def __init__(self, library_item_id: int, title: str, author: str) -> None:
        super().__init__(library_item_id, title)
        self._check_out_length = 21
        self._author = author

    def __repr__(self):
        return f"B: {self._title} by {self._author}"

    def get_check_out_length(self) -> int:
        return self._check_out_length

    def get_author(self) -> str:
        return self._author


class Album(LibraryItem):
    """Extension of LibraryItem class with artist and check out length"""

    def __init__(self, library_item_id: int, title: str, artist: str) -> None:
        super().__init__(library_item_id, title)
        self._check_out_length = 14
        self._artist = artist

    def __repr__(self):
        return f"A: {self._title} by {self._artist}"

    def get_check_out_length(self) -> int:
        return self._check_out_length

    def get_artist(self) -> str:
        return self._artist


class Movie(LibraryItem):
    """Extension of LibraryItem class with director and check out length"""

    def __init__(self, library_item_id: int, title: str, director: str) -> None:
        super().__init__(library_item_id, title)
        self._check_out_length = 7
        self._director = director

    def __repr__(self):
        return f"M: {self._title} directed by {self._director}"

    def get_check_out_length(self) -> int:
        return self._check_out_length

    def get_director(self) -> str:
        return self._director


if __name__ == "__main__":
    book1 = Book(123, "Lord of the Rings", "JRR Tolkien")
    book2 = Book(345, "One Fish Two Fish", "Dr. Seuss")

    album1 = Album(532, "Abbey Road", "The Beatles")
    album2 = Album(643, "Evolve", "Imagine Dragons")

    movie1 = Movie(764, "Onward", "Dan Scanlon")
    movie2 = Movie(987, "Uncle Buck", "John Huges")

    print(book1)
    print(book2)
    print(album1)
    print(album2)
    print(movie1)
    print(movie2)
