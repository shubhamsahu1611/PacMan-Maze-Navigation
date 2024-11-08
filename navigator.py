import copy
from maze import *
from exception import *
from stack import *
from typing import List, Tuple
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation

    def solveWithoutRecursion(self, end : Tuple[int, int] , start: Tuple[int , int] , visited:List[List[bool]] , ans: Stack ,m ,n)-> bool:
        if self.navigator_maze[start[0]][start[1]]==1 :
            return False
        stack=Stack()
        if self.navigator_maze[end[0]][end[1]]==1 :
            return False
        index=start
        path=[]
        path.append(index)
        stack.push((index, path))
        while not stack.is_empty():
            index, path=stack.top()
            stack.pop()
            x=index[0]
            y=index[1]
            visited[x][y]=True
            if self.navigator_maze[x][y]==1 : continue
            #checking that we are at end or not, if yes than path found
            if index==end:
                for x in path:
                    ans.push(x)
                return True
            #flag=False
            
            #going to left side
            if y>0 and not visited[x][y-1] :
                new_path = copy.copy(path)
                new_path.append((x, y-1))
                stack.push(((x, y-1), new_path))
            
            #going to up side
            if (x>0) and (not visited[x-1][y]) :
                new_path = copy.copy(path)
                new_path.append((x-1, y))
                stack.push(((x-1, y), new_path))
            
            #going to down side
            if x<(m-1) and not visited[x+1][y] :
                new_path = copy.copy(path)
                new_path.append((x+1,y))
                stack.push(((x+1, y), new_path))
            
                
            #going to right side
            if y<(n-1) and not visited[x][y+1] :
                new_path = copy.copy(path)
                new_path.append((x, y+1))
                stack.push(((x, y+1), new_path))
            
        return False
        
        
    def find_path(self, start : Tuple[int, int], end : Tuple[int, int]) -> List[Tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        visited=[]
        ans=Stack()
        m=len(self.navigator_maze)
        n=len(self.navigator_maze[0])
        for row in range(m):
            grid=[]
            for column in range(n):
                grid.append(False)
            visited.append(grid)
        if self.solveWithoutRecursion( end, start , visited, ans, m, n) :
            return ans.items()
        else:
            raise PathNotFoundException
