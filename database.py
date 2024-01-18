from typing import Dict, List


class Database:
    def __init__(self) -> None:
        """
        Initialize an empty database with dictionaries to store key-value pairs,
        transaction history, and the count of each value in the database.
        """
        self.data: Dict[str, str] = {}
        self.transactions: List[Dict[str, Dict[str, int]]] = []
        self.value_counts: Dict[str, int] = {}

    def set(self, key: str, value: str) -> None:
        """
        Set the value for a given key, updating the count of the previous value if it exists.

        Parameters:
        - key (str): The key for the key-value pair.
        - value (str): The value to be associated with the key.
        """
        if key in self.data:
            # Update the count for the old value
            old_value = self.data[key]
            self.value_counts[old_value] -= 1

        # Set the new value for the key
        self.data[key] = value
        self.value_counts[value] = self.value_counts.get(value, 0) + 1

    def get(self, key: str) -> str:
        """
        Retrieve the value for a given key, or return "NULL" if the key is not found.

        Parameters:
        - key (str): The key for which to retrieve the value.

        Returns:
        - str: The value associated with the key, or "NULL" if the key is not found.
        """
        return str(self.data.get(key, "NULL"))

    def delete(self, key: str) -> None:
        """
        Delete a key-value pair, updating the count for the deleted value.

        Parameters:
        - key (str): The key to be deleted from the database.
        """
        if key in self.data:
            value = self.data[key]
            del self.data[key]
            self.value_counts[value] -= 1
        else:
            print(f"Key '{key}' not found in the database.")

    def count(self, value: str) -> int:
        """
        Get the count of a specific value in the database.

        Parameters:
        - value (str): The value for which to get the count.

        Returns:
        - int: The count of the specified value in the database.
        """
        return self.value_counts.get(value, 0)

    def begin(self) -> None:
        """
        Begin a transaction by storing a snapshot of the current state of the database.
        """
        self.transactions.append((dict(self.data), dict(self.value_counts)))

    def rollback(self) -> None:
        """
        Rollback to the previous state of the database from the last transaction.

        Prints an error message if there are no transactions to rollback.
        """
        if self.transactions:
            self.data, self.value_counts = self.transactions.pop()
        else:
            print("No transaction to rollback.")

    def commit(self) -> None:
        """
        Commit the changes made during a transaction by clearing the transaction history.
        """
        self.transactions = []
