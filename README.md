# In-Memory Database CLI

This command line interface (CLI) interacts with a key-value store database. It supports basic operations like setting key-value pairs, retrieving values, deleting pairs, counting occurrences, and managing transactions.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository:

   `git clone https://github.com/csvaldellon/engineer-python.git`

2. Navigate to the project directory:

   `cd engineer-python`

## Running the Program

To start the CLI, run the following command:

`python main.py`

Supported commands:

- SET key value: Set a key-value pair in the database.
- GET key: Retrieve the value associated with a key from the database.
- DELETE key: Delete a key-value pair from the database.
- COUNT value: Get the count of occurrences of a value in the database.
- BEGIN: Start a transaction in the database.
- ROLLBACK: Rollback the current transaction in the database.
- COMMIT: Commit the current transaction in the database.

## Sample Test Cases

Taken from: https://github.com/csvaldellon/engineer-python/blob/master/EXAM.md

**Example 1: Basic Commands**

1. `GET a`
>>> NULL
2. `SET a foo`
3. `SET b foo`
4. `COUNT foo`
>>> 2
5. `COUNT bar`
>>> 0
6. `DELETE a`
7. `COUNT foo`
>>> 1
8. `SET b baz`
9. `COUNT foo`
>>> 0
10. `GET b`
>>> baz
11. `GET B`
>>> NULL
12. END

**Example 2: Multiple Transactions**

1. `SET a foo`
2. `SET a foo`
3. `COUNT foo`
>>> 1
4. `GET a`
>>> foo
5. `DELETE a`
6. `GET a`
>>> NULL
7. `COUNT foo`
>>> 0
8. END

**Example 3: Nested Transactions**

1. `BEGIN`
2. `SET a foo`
3. `GET a`
>>> foo
4. `BEGIN`
5. `SET a bar`
6. `GET a`
>>> bar
7. `SET a baz`
8. `ROLLBACK`
9. `GET a`
>>> foo
10. `ROLLBACK`
11. `GET a`
>>> NULL
12. END

**Example 4: Nested Transactions with COMMIT**

1. `SET a foo`
2. `SET b baz`
3. `BEGIN`
4. `GET a`
>>> foo
5. `SET a bar`
6. `COUNT bar`
>>> 1
7. `BEGIN`
8. `COUNT bar`
>>> 1
9. `DELETE a`
10. `GET a`
>>> NULL
11. `COUNT bar`
>>> 0
12. `ROLLBACK`
13. `GET a`
>>> bar
14. `COUNT bar`
>>> 1
15. `COMMIT`
16. `GET a`
>>> bar
17. `GET b`
>>> baz
18. END
