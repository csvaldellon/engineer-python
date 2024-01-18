# Database CLI

This command line interface (CLI) interacts with a key-value store database. It supports basic operations like setting key-value pairs, retrieving values, deleting pairs, counting occurrences, and managing transactions.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository:
   git clone https://github.com/your-username/database-cli.git

2. Navigate to the project directory:
   cd database-cli

3. Install dependencies (if any):
   # No external dependencies for this project

## Running the Program

To start the CLI, run the following command:

python main.py

Supported commands:

- SET key value: Set a key-value pair in the database.
- GET key: Retrieve the value associated with a key from the database.
- DELETE key: Delete a key-value pair from the database.
- COUNT value: Get the count of occurrences of a value in the database.
- BEGIN: Start a transaction in the database.
- ROLLBACK: Rollback the current transaction in the database.
- COMMIT: Commit the current transaction in the database.
