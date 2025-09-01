"""
Title: Word Search
Approach: Use backtracking with DFS to search for word in 2D grid by trying all directions
Time: O(m*n*4^L) where m*n is grid size and L is word length
Space: O(L) for recursion stack
"""

from typing import List

class Solution:
    def solve(self, board, word, row, col, index, visited) -> bool:
        # base case
        if index == len(word):
            return True

        # bounds + visited + mismatch check
        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            visited[row][col] or 
            board[row][col] != word[index]):
            return False

        # mark visited
        visited[row][col] = True

        # explore 4 directions
        found = (self.solve(board, word, row+1, col, index+1, visited) or
                 self.solve(board, word, row-1, col, index+1, visited) or
                 self.solve(board, word, row, col+1, index+1, visited) or
                 self.solve(board, word, row, col-1, index+1, visited))

        # backtrack
        visited[row][col] = False
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if self.solve(board, word, i, j, 0, visited):
                    return True
        return False
