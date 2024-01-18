from database import Database
from input_processor import execute_command
from logger import logger

if __name__ == "__main__":
    db = Database()

    try:
        while True:
            command = input().split()

            if not command:
                continue

            execute_command(db, command)

    except KeyboardInterrupt:
        logger.info("Execution interrupted by the user.")
