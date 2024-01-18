import unittest
from io import StringIO
from unittest.mock import patch

from main import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_basic_commands(self):
        with patch(
            "builtins.input",
            side_effect=[
                "GET a",
                "SET a foo",
                "SET b foo",
                "COUNT foo",
                "COUNT bar",
                "DELETE a",
                "COUNT foo",
                "SET b baz",
                "COUNT foo",
                "GET b",
                "GET B",
                "END",
            ],
        ):
            output = self.run_database()
        expected_output = "NULL\n2\n0\n1\n0\nbaz\nNULL\n"
        self.assertEqual(output, expected_output)

    def test_multiple_transactions(self):
        with patch(
            "builtins.input",
            side_effect=[
                "SET a foo",
                "SET a foo",
                "COUNT foo",
                "GET a",
                "DELETE a",
                "GET a",
                "COUNT foo",
                "END",
            ],
        ):
            output = self.run_database()
        expected_output = "1\nfoo\nNULL\n0\n"
        self.assertEqual(output, expected_output)

    def test_nested_transactions(self):
        with patch(
            "builtins.input",
            side_effect=[
                "BEGIN",
                "SET a foo",
                "GET a",
                "BEGIN",
                "SET a bar",
                "GET a",
                "SET a baz",
                "ROLLBACK",
                "GET a",
                "ROLLBACK",
                "GET a",
                "END",
            ],
        ):
            output = self.run_database()
        expected_output = "foo\nbar\nfoo\nNULL\n"
        self.assertEqual(output, expected_output)

    def test_nested_transactions_with_commit(self):
        with patch(
            "builtins.input",
            side_effect=[
                "SET a foo",
                "SET b baz",
                "BEGIN",
                "GET a",
                "SET a bar",
                "COUNT bar",
                "BEGIN",
                "COUNT bar",
                "DELETE a",
                "GET a",
                "COUNT bar",
                "ROLLBACK",
                "GET a",
                "COUNT bar",
                "COMMIT",
                "GET a",
                "GET b",
                "END",
            ],
        ):
            output = self.run_database()
        expected_output = "foo\n1\n1\nNULL\n0\nbar\n1\nbar\nbaz\n"
        self.assertEqual(output, expected_output)

    def run_database(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with patch("sys.stdin", side_effect=""):
                while True:
                    command = input()
                    if not command:
                        continue
                    operation = command.split()[0].lower()
                    if operation == "end":
                        break
                    self.execute_command(command)
                return mock_stdout.getvalue()

    def execute_command(self, command):
        command_parts = command.split()
        operation = command_parts[0].lower()
        if operation == "set":
            self.db.set(command_parts[1], command_parts[2])
        elif operation == "get":
            print(self.db.get(command_parts[1]))
        elif operation == "delete":
            self.db.delete(command_parts[1])
        elif operation == "count":
            print(self.db.count(command_parts[1]))
        elif operation == "begin":
            self.db.begin()
        elif operation == "rollback":
            self.db.rollback()
        elif operation == "commit":
            self.db.commit()


if __name__ == "__main__":
    unittest.main()
