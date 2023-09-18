from LibraryItem import LibraryItem, Book, Movie, Album
from Patron import Patron


class Library:
    """A class describing library object which holds the patrons
    and library items in the library"""

    def __init__(self) -> None:
        self._holdings = []
        self._members = []
        self._current_date = 0

    def __repr__(self) -> str:
        return f"Library has {len(self._holdings)} library items and {len(self._members)} patrons"

    def __str__(self) -> str:
        return f"Library"

    def get_members(self) -> list:
        return self._members

    def get_holdings(self) -> list:
        return self._holdings

    def add_library_item(self, libraryItem: LibraryItem) -> None:
        self._holdings.append(libraryItem)

    def add_patron(self, patron: Patron) -> None:
        self._members.append(patron)

    def lookup_library_item_from_id(self, id: int) -> LibraryItem:
        """looks up the library item by id and returns it if it is in the library"""
        for item in self._holdings:
            if item.get_library_item_id() == id:
                return item
        return None

    def lookup_patron_from_id(self, id: int) -> Patron:
        """looks up a patron  by id and returns it if it is in the dictionary"""
        for person in self._members:
            if person.get_patron_id() == id:
                return person
        return None

    def check_out_library_item(self, patron_id: int, library_item_id: int) -> str:
        """Checks out a library item for a person"""

        # look up if person and library item are in library
        person = self.lookup_patron_from_id(patron_id)
        if person is None:
            return "patron not found"
        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        """ if the item is checked out and not on hold by another person, 
        it will add ot the hold shelf and say who has it on hold"""
        if item.get_location() == "CHECKED_OUT":
            if item.get_requested_by() is None:
                item.update_requested_by(person.get_name())
                item.update_location("ON_HOLD_SHELF")
            return "item already checked out"
        # checks if item is on hold by another peroson
        if (
            item.get_location() == "ON_HOLD_SHELF"
            and item.get_requested_by() != person.get_name()
        ):
            return "item on hold by other patron"

        # checks if item is on hold by person checking it out
        if (
            item.get_location() == "ON_HOLD_SHELF"
            and item.get_requested_by() == person.get_name()
        ):
            item.update_requested_by(person.get_name())

        # if it passes through above checks, item will be checked out and added to patron's items
        item.check_out(person.get_name(), self._current_date)
        person.add_library_item(item)
        return "check out successful"

    def return_library_item(self, library_item_id: int) -> str:
        """returns item to library"""
        item = self.lookup_library_item_from_id(library_item_id)

        # checks if item is in library and checked out
        if item is None:
            return "item not found"
        if item.get_location() == "ON_SHELF":
            return "item already in library"

        # finds which member has item checked out and removes it from their list
        for member in self._members:
            if item in member.get_checked_out_items():
                member.remove_library_item(item)
        # updates location
        if item.get_requested_by() is not None:
            item.update_location("ON_HOLD_SHELF")
        else:
            item.update_location("ON_SHELF")

        # updates who it is checked out by
        item.update_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_id: int, library_item_id: int) -> str:
        """Requests a library item to be put on hold"""
        person = self.lookup_patron_from_id(patron_id)

        # checks if patron and library item are in the library
        if person is None:
            return "patron not found"
        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        # checks if item is already on hold
        if item.get_requested_by() is not None:
            return "item already on hold"

        # updates requested by and location
        item.update_requested_by(person.get_name())
        if item.get_location() == "ON_SHELF":
            item.update_location("ON_HOLD_SHELF")
        return "request successful"

    def pay_fine(self, patron_id: int, amount: float) -> str:
        """Pays fine for patron"""
        person = self.lookup_patron_from_id(patron_id)

        # checks if patron is in library
        if person is None:
            return "patron not found"

        # updates fine
        person.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self) -> None:
        """Increases the date and updates fines for overdue library items"""
        self._current_date += 1
        for member in self._members:
            items = member.get_checked_out_items()
            for item in items:
                checked_out = item.get_date_checked_out()
                days_checked_out = self._current_date - checked_out
                if days_checked_out > item.get_check_out_length():
                    member.amend_fine(0.10)


if __name__ == "__main__":
    b1 = Book(123, "Phantom Tollbooth", "Juster")
    a1 = Album(456, "...And His Orchestra", "The Fastbacks")
    m1 = Movie(789, "Laputa", "Miyazaki")

    p1 = Patron(987, "Felicity")
    p2 = Patron(654, "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(m1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    lib.check_out_library_item(654, 456)
    for _ in range(7):
        lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item(654, 789)
    loc = a1.get_location()
    lib.request_library_item(987, 456)

    for _ in range(57):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    lib.pay_fine(654, p2_fine)
    lib.return_library_item(456)
    print(lib)
