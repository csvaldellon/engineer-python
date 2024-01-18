from typing import List

from command_handler import COMMAND_HANDLERS
from database import Database
from logger import logger


def execute_command(db: Database, command: List[str]) -> None:
    """
    Execute a command on the specified database.

    Parameters:
    - db (Database): The database instance on which the command will be executed.
    - command (List[str]): The command to be executed as a list of strings.

    Returns:
    - None

    Raises:
    - Exception: If an error occurs during command execution.

    The function extracts the operation from the command, converts it to lowercase, and
    uses the COMMAND_HANDLERS dictionary to retrieve the corresponding handler function.
    If a valid handler function is found, it is executed with the provided database instance
    and command. If the operation is not recognized, an error is logged. Any exceptions
    that occur during command execution are also logged.

    Supported commands:
    - set: Set a key-value pair in the database.
    - get: Retrieve the value associated with a key from the database.
    - delete: Delete a key-value pair from the database.
    - count: Get the count of occurrences of a key in the database.
    - begin: Start a transaction in the database.
    - rollback: Rollback the current transaction in the database.
    - commit: Commit the current transaction in the database.
    - end: Exit the program.

    Example:
    >>> execute_command(my_database, ["set", "key", "value"])
    """
    try:
        operation = command[0].lower()

        # Use the dictionary to get the corresponding handler function for the command
        handler_function = COMMAND_HANDLERS.get(operation)

        if handler_function:
            handler_function(db, command)
        else:
            logger.error(
                "Invalid command. Supported commands: set, get, delete, count, begin, rollback, commit, end"
            )

    except Exception as e:
        logger.error(f"Error: {e}")
