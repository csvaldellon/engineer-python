from typing import List

from database import Database
from logger import logger


def handle_set_command(db: Database, command: List[str]) -> None:
    if len(command) == 3:
        db.set(command[1], command[2])
    else:
        logger.error("Invalid 'set' command. Format: set <key> <value>")


def handle_get_command(db: Database, command: List[str]) -> None:
    if len(command) == 2:
        print(db.get(command[1]))
    else:
        logger.error("Invalid 'get' command. Format: get <key>")


def handle_delete_command(db: Database, command: List[str]) -> None:
    if len(command) == 2:
        db.delete(command[1])
    else:
        logger.error("Invalid 'delete' command. Format: delete <key>")


def handle_count_command(db: Database, command: List[str]) -> None:
    if len(command) == 2:
        print(db.count(command[1]))
    else:
        logger.error("Invalid 'count' command. Format: count <value>")


def handle_begin_command(db: Database, command: List[str]) -> None:
    if len(command) != 1:
        logger.error(
            "Invalid 'begin' command. 'begin' command should not have any arguments."
        )
    db.begin()


def handle_rollback_command(db: Database, command: List[str]) -> None:
    if len(command) != 1:
        logger.error(
            "Invalid 'rollback' command. 'rollback' command should not have any arguments."
        )
    db.rollback()


def handle_commit_command(db: Database, command: List[str]) -> None:
    if len(command) != 1:
        logger.error(
            "Invalid 'commit' command. 'commit' command should not have any arguments."
        )
    db.commit()


def handle_end_command(db: Database, command: List[str]) -> None:
    if len(command) != 1:
        logger.error(
            "Invalid 'end' command. 'end' command should not have any arguments."
        )
    raise SystemExit


# Create a dictionary mapping command names to their corresponding handler functions
COMMAND_HANDLERS = {
    "set": handle_set_command,
    "get": handle_get_command,
    "delete": handle_delete_command,
    "count": handle_count_command,
    "begin": handle_begin_command,
    "rollback": handle_rollback_command,
    "commit": handle_commit_command,
    "end": handle_end_command,
}
