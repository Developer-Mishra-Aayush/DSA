# DSA

A curated collection of Data Structures and Algorithms problems implemented in Python.
The repository is organized by topic to make it easy to browse, practice, and run
individual solutions.

## Repository Structure

```
DSA/
  Arrays/                     # Array-based problems and matrix utilities
  char Arrays & Strings/      # String algorithms and character array problems
  LinkedList/                 # Singly/Doubly linked list implementations and problems
  Searching & Sorting/        # Classic search/sort problems and patterns
  Sorting Algorithms/         # Fundamental sorting algorithm implementations
  Recursion/                  # Recursive solutions and patterns
```

Each folder contains one-file-per-problem Python solutions, named after the problem.

## Prerequisites

- Python 3.8+ installed (`python3 --version`)

No external dependencies are required; all solutions use the Python standard library.

## How to Run

Most files are self-contained scripts. You can run any problem directly with Python:

```bash
python3 Arrays/two_sum.py
```

Some scripts expect input provided within the file (sample inputs in variables or a
`if __name__ == "__main__":` block). If a script defines only functions, you can:

- Add a quick test in a `__main__` block, or
- Import and invoke the function from an interactive session or another file.

Example (interactive Python shell):

```python
from Arrays.two_sum import two_sum
print(two_sum([2,7,11,15], 9))  # -> [0, 1] (example)
```

## Topics Overview (folders)

- Arrays: prefix sums, two-pointer techniques, hashing, matrix traversal, etc.
- char Arrays & Strings: anagrams, palindrome checks, sliding window, string transforms.
- LinkedList: construction, reversal, cycle detection, partitioning, k-group reversal.
- Searching & Sorting: binary search patterns, allocation/partition problems, rotated arrays.
- Sorting Algorithms: bubble, insertion, selection, merge, and quick sort implementations.

## Suggested Workflow

1. Pick a topic folder.
2. Open a file to review the approach and implementation.
3. Run the script or import its main function(s) to test with custom inputs.

## Contributing

Contributions are welcome. Please follow these guidelines:

- Keep one problem per file and name it descriptively (e.g., `two_sum.py`).
- Include a small `__main__` demo or simple tests where helpful.
- Prefer clear, readable code and meaningful names.
- Add brief docstrings or comments for non-trivial logic.

## Author

- Name: Aayush Mishra
- GitHub: https://github.com/Developer-Mishra-Aayush/DSA
- Email: ayush28014@gmail.com

## License

This repository is provided for educational purposes. Use freely.
