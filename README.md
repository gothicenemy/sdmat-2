# Lab Work: List Implementation and Refactoring

## Application Description

This project demonstrates the implementation of a character list interface (strings of length 1) in two ways:

1.  **Initial Implementation:** Using Python's built-in `list` type (`ArrayList`).
2.  **Second Implementation (Post-Refactoring):** A custom implementation of a doubly linked list (`DoublyLinkedList`) using `Node` objects.

The application includes unit tests to verify the correctness of both implementations and is configured with CI (GitHub Actions) for automatic test execution.

## Assignment Variant

* **Initial list implementation:** List based on built-in arrays/lists (used Python `list`).
* **Second list implementation:** Doubly linked list.

## Build and Test Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gothicenemy/sdmat-2
    cd sdmat-2
    ```

2.  **Install dependencies:**
    `pytest` is required for running tests.
    ```bash
    # Ensure pip is available for your python interpreter
    py -m ensurepip --upgrade
    # Install pytest
    py -m pip install pytest
    ```
    *Note: If using a virtual environment (recommended), activate it before installation.*

3.  **Run Unit Tests:**
    ```bash
    py -m pytest
    ```
    All tests should pass (except for the specific commit demonstrating a failure).

4.  **Run the Demonstration Script:**
    ```bash
    python main.py
    ```
    The script will demonstrate the methods of the `DoublyLinkedList` class.

## Link to Commit with CI Failure

To demonstrate the CI workflow and the ability of tests to catch errors, a test was intentionally broken in the following commit:

[Link to your commit with the failure](https://github.com/gothicenemy/sdmat-2/commit/b47b5f78d28644b132a03a4ea4a0681b7f0e4746)

The subsequent commit contains the fix for this error.

## Conclusions on Unit Tests
*Writing tests initially for the `ArrayList` felt somewhat redundant as it mostly wrapped built-in Python functions. However, having this test suite ready was invaluable when refactoring to `DoublyLinkedList`. It saved significant effort by allowing quick verification of the complex linked list logic against the established requirements. Overall, the time spent on tests was well justified.*
**)**
