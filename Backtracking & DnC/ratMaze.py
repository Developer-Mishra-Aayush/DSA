def isSafe(maze,visited,i,j,currentPath,ans):
    if i>=0 and i<len(maze) and j>=0 and j<len(maze) and  maze[i][j]==1 and visited[i][j] == 0:
        return True
    return False



def solve(maze,visited,i,j,currentPath,ans):
    if i==len(maze)-1  and j==len(maze)-1:
        ans.append(currentPath)
        return 
    
    # Down Case -> i+1,j
    if isSafe(maze,visited,i+1,j,currentPath,ans):
        visited[i+1][j] = 1
        solve(maze,visited,i+1,j,currentPath+'D',ans)
        # Now Backtract the above step
        visited[i+1][j] = 0
    # Up Case -> i-1,j
    if isSafe(maze,visited,i-1,j,currentPath,ans):
        visited[i-1][j] = 1
        solve(maze,visited,i-1,j,currentPath+'U',ans)
        # Now Backtract the above step
        visited[i-1][j] = 0
    # Right Case -> i,j+1
    if isSafe(maze,visited,i,j+1,currentPath,ans):
        visited[i][j+1] = 1
        solve(maze,visited,i,j+1,currentPath+'R',ans)
        # Now Backtract the above step
        visited[i][j+1] = 0
    # Left Case -> i,j-1
    if isSafe(maze,visited,i,j-1,currentPath,ans):
        visited[i][j-1] = 1
        solve(maze,visited,i,j-1,currentPath+'L',ans)
        # Now Backtract the above step
        visited[i][j-1] = 0
    




def ratMaze(maze,visited):
    i = 0
    j = 0
    currentPath = ""
    ans = []
    solve(maze,visited,i,j,currentPath,ans)
    print(ans)
    return ans



maze = [[1,0,0],
        [1,1,0],
        [1,1,1,]]
visited = [[0,0,0],
            [0,0,0],
            [0,0,0]]
visited[0][0] = 1
ratMaze(maze,visited)