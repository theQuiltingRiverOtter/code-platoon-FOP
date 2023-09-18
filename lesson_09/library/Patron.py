from LibraryItem import LibraryItem


class Patron:
    """Creates a Patron object with an integer for patron id and a name"""

    def __init__(self, patron_id: int, name: str) -> None:
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def __repr__(self):
        return f"ID: {self._patron_id}, Name: {self._name}, Checked Out: {len(self._checked_out_items)} Fine: {self._fine_amount}"

    def __str__(self):
        return f"{self._patron_id} : {self._name}"

    def get_name(self) -> str:
        return self._name

    def get_patron_id(self) -> int:
        return self._patron_id

    def get_fine_amount(self) -> float:
        """return fine amount rounded to two decimal places because it represents monetary value"""
        return round(self._fine_amount, 2)

    def get_checked_out_items(self) -> list:
        return self._checked_out_items

    def add_library_item(self, libraryItem: LibraryItem) -> None:
        self._checked_out_items.append(libraryItem)

    def remove_library_item(self, libraryItem: LibraryItem) -> None:
        """Finds the item in list and removes it if it is in there"""
        remove_id = libraryItem.get_library_item_id()
        for i in range(len(self._checked_out_items)):
            if self._checked_out_items[i].get_library_item_id() == remove_id:
                index = i
        if index:
            self._checked_out_items.pop(i)

    def amend_fine(self, amount: float) -> None:
        """increases fine if a positive number and decreases it if it is a negative number"""
        self._fine_amount += amount
