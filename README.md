# DSA

A curated collection of Data Structures and Algorithms problems implemented in Python.
The repository is organized by topic to make it easy to browse, practice, and run
individual solutions.

## Repository Structure

```
DSA/
  Arrays/                     # Array-based problems and matrix utilities
  char Arrays & Strings/      # String algorithms and character array problems
  Generic & Binary Trees/     # Binary tree operations, traversals, and tree-based algorithms
  LinkedList/                 # Singly/Doubly linked list implementations and problems
  Recursion/                  # Recursive solutions and patterns
  Backtracking & DnC/        # Backtracking algorithms and Divide & Conquer solutions
  Stacks/                     # Stack-based algorithms and data structure problems
  Searching & Sorting/        # Classic search/sort problems and patterns
  Sorting Algorithms/         # Fundamental sorting algorithm implementations
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

### Arrays
Array manipulation, prefix sums, two-pointer techniques, hashing, matrix traversal, and common array patterns.
- **Key Problems**: Two Sum, Three Sum, Missing Number, Remove Duplicates, Spiral Print, Wave Print
- **Matrix Operations**: Transpose, Row/Column Sum, Spiral Traversal
- **Techniques**: Sliding Window, Two Pointers, Hashing, Sorting

### Character Arrays & Strings
String algorithms, character manipulation, and advanced string processing techniques.
- **Key Problems**: Valid Anagram, Longest Common Prefix, Palindrome Check, String Compression
- **Advanced**: Wildcard Matching, Isomorphic Strings, Group Anagrams, Zigzag Conversion
- **Techniques**: Sliding Window, Two Pointers, Character Frequency Counting

### Generic & Binary Trees
Binary tree operations, traversals, and tree-based algorithms with comprehensive coverage.
- **Traversals**: Inorder, Preorder, Postorder, Level Order, Morris Traversal
- **Tree Properties**: Height, Diameter, Balanced Tree, Identical Trees, Path Sum
- **Advanced Operations**: Tree Construction, Flatten Tree, Boundary Traversal, Top/Bottom View
- **Tree Algorithms**: Lowest Common Ancestor, Duplicate Subtrees, Burning Tree, Sum Tree
- **Techniques**: DFS, BFS, Recursion, Tree Manipulation, Parent-Child Relationships

### LinkedList
Singly and doubly linked list implementations, operations, and problem-solving patterns.
- **Key Problems**: Reverse List, Detect Cycle, Merge Lists, Remove Nth Node
- **Advanced**: Copy List with Random Pointer, Partition List, Rotate List
- **Techniques**: Two Pointers (Fast/Slow), Recursion, Iterative Manipulation

### Recursion
Recursive solutions and patterns for various algorithmic problems.
- **Key Problems**: Fibonacci Series, Factorial, Binary Search, Palindrome Check
- **Advanced**: Coin Change, House Robber, Jump Game, Perfect Squares
- **Techniques**: Memoization, Backtracking, Divide & Conquer, Tree Traversal

### Backtracking & Divide & Conquer
Backtracking algorithms and divide-and-conquer solutions for complex problems.
- **Backtracking**: N-Queens, Rat in Maze, Word Search, Permutations, Combinations
- **Divide & Conquer**: Merge Sort, Quick Sort, Count Inversions, Max Subarray
- **Techniques**: State Space Search, Pruning, Recursive Backtracking

### Stacks
Stack-based algorithms and data structure problems with various applications.
- **Basic Operations**: Reverse Stack, Insert at Bottom, Check if Sorted, Find Middle Element
- **Advanced Problems**: Car Fleet, Celebrity Problem, Decode String, Largest Rectangle Area
- **Monotonic Stack**: Next/Previous Smaller Elements, Stock Span, Min Stack
- **String Processing**: Valid Parentheses, Bracket Reversal, Remove Duplicates, Simplify Path
- **Techniques**: Monotonic Stack, Recursive Stack Manipulation, State Tracking

### Searching & Sorting
Classic search and sort problems with advanced patterns and optimizations.
- **Searching**: Binary Search, Search in Rotated Array, Peak Finding
- **Allocation Problems**: Book Allocation, Painter Partition, Aggressive Cows
- **Techniques**: Binary Search on Answer, Two Pointers, Greedy Approaches

### Sorting Algorithms
Fundamental sorting algorithm implementations with analysis.
- **Algorithms**: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort
- **Analysis**: Time/Space Complexity, Stability, In-place vs Extra Space
- **Optimizations**: Early Termination, Pivot Selection, Merge Strategies

## Problem Documentation

Each problem file includes:
- **Title**: Clear description of the problem
- **Approach**: Brief explanation of the algorithm/strategy used
- **Time Complexity**: Analysis of time requirements
- **Space Complexity**: Analysis of memory requirements

## Suggested Workflow

1. **Start with Basics**: Begin with Arrays and Sorting Algorithms for fundamental concepts
2. **Progress to Intermediate**: Move to LinkedList and Recursion for more complex patterns
3. **Advanced Topics**: Explore Backtracking & DnC for sophisticated problem-solving techniques
4. **Practice**: Use Searching & Sorting for interview-style problems
5. **Review**: Revisit problems to understand different approaches and optimizations

## Learning Path

### Beginner Level
- Arrays: Two Sum, Missing Number, Remove Duplicates
- Sorting: Bubble Sort, Selection Sort, Insertion Sort
- Recursion: Factorial, Fibonacci, Print Array

### Intermediate Level
- LinkedList: Reverse, Detect Cycle, Merge Lists
- Strings: Valid Anagram, Palindrome, Longest Common Prefix
- Recursion: Binary Search, Coin Change, House Robber
- Stacks: Basic Operations, Valid Parentheses, Remove Duplicates
- Binary Trees: Tree Traversals, Height/Diameter, Balanced Tree, Path Sum

### Advanced Level
- Backtracking: N-Queens, Rat in Maze, Permutations
- Divide & Conquer: Merge Sort, Quick Sort, Count Inversions
- Stacks: Monotonic Stack, Car Fleet, Celebrity Problem, Largest Rectangle Area
- Binary Trees: Tree Construction, Flatten Tree, Boundary Traversal, LCA, Burning Tree
- Complex Problems: Wildcard Matching, Isomorphic Strings, Group Anagrams

## Contributing

Contributions are welcome. Please follow these guidelines:

- Keep one problem per file and name it descriptively (e.g., `two_sum.py`)
- Include a small `__main__` demo or simple tests where helpful
- Prefer clear, readable code and meaningful names
- Add brief docstrings or comments for non-trivial logic
- Follow the established format with Title, Approach, Time, and Space complexity

## Author

- Name: Aayush Mishra
- GitHub: https://github.com/Developer-Mishra-Aayush/DSA
- Email: ayush28014@gmail.com

## License

This repository is provided for educational purposes. Use freely.
