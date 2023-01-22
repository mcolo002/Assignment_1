import random
from collections import defaultdict
import numpy as np

class Graph:
    
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def actions(self, u:list):
        coordinates = find_empty_space(u)
        x = coordinates[0]
        y = coordinates[1]
        
        if x == 0 and y == 0:
            self.addEdge(u[0][0],u[0][1])
            self.addEdge(u[0][0],u[1][0])
        elif x == 0 and y == 1:
            self.addEdge(u[0][1],u[0][0])
            self.addEdge(u[0][1],u[1][1])
            self.addEdge(u[0][1],u[0][2])
        elif x == 0 and y == 2:
            self.addEdge(u[0][2],u[0][1])
            self.addEdge(u[0][2],u[1][2])
            self.addEdge(u[0][2],u[0][3])
        elif x == 0 and y == 3:
            self.addEdge(u[0][3],u[0][2])
            self.addEdge(u[0][3],u[1][3])
        elif x == 1 and y == 0:
            self.addEdge(u[1][0],u[0][0])
            self.addEdge(u[1][0],u[1][1])
            self.addEdge(u[1][0],u[0][2])
        elif x == 1 and y == 1:
            self.addEdge(u[1][1],u[0][1])
            self.addEdge(u[1][1],u[1][2])
            self.addEdge(u[1][1],u[2][1])
            self.addEdge(u[1][1],u[1][0])
        elif x == 1 and y == 2:
            self.addEdge(u[1][2],u[1][1])
            self.addEdge(u[1][2],u[0][2])
            self.addEdge(u[1][2],u[2][2])
            self.addEdge(u[1][2],u[1][3])
        elif x == 1 and y == 3:
            self.addEdge(u[1][3],u[1][2])
            self.addEdge(u[1][3],u[0][3])
            self.addEdge(u[1][3],u[2][3])
        elif x == 2 and y == 0:
            self.addEdge(u[2][0],u[1][0])
            self.addEdge(u[2][0],u[2][1])
            self.addEdge(u[2][0],u[3][0])
        elif x == 2 and y == 1:
            self.addEdge(u[2][1],u[2][0])
            self.addEdge(u[2][1],u[1][1])
            self.addEdge(u[2][1],u[2][2])
            self.addEdge(u[2][1],u[3][1])
        elif x == 2 and y == 2:
            self.addEdge(u[2][2],u[2][1])
            self.addEdge(u[2][2],u[1][2])
            self.addEdge(u[2][2],u[2][3])
            self.addEdge(u[2][2],u[3][1])
        elif x == 2 and y == 3:
            self.addEdge(u[2][3],u[2][2])
            self.addEdge(u[2][3],u[1][3])
            self.addEdge(u[2][3],u[3][3])
        elif x == 3 and y == 0:
            self.addEdge(u[1][1],u[0][1])
            self.addEdge(u[1][1],u[1][2])
            self.addEdge(u[1][1],u[2][1])
            self.addEdge(u[1][1],u[1][0])
        elif x == 3 and y == 1:
            self.addEdge(u[1][1],u[0][1])
            self.addEdge(u[1][1],u[1][2])
            self.addEdge(u[1][1],u[2][1])
            self.addEdge(u[1][1],u[1][0])       
        elif x == 3 and y == 2:
            self.addEdge(u[1][1],u[0][1])
            self.addEdge(u[1][1],u[1][2])
            self.addEdge(u[1][1],u[2][1])
            self.addEdge(u[1][1],u[1][0])
        elif x == 3 and y == 3:
            self.addEdge(u[1][1],u[0][1])
            self.addEdge(u[1][1],u[1][2])
            self.addEdge(u[1][1],u[2][1])
            self.addEdge(u[1][1],u[1][0])
            
    def dispay(self):
        print(self.graph)
    
    def BFS(self, s):
        
        visited = [False] * (max(self.graph)+1)
        
        queue = []
        queue.append(s)
        visited[s] = True
        
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

class Game_Board:
    gb = []
        
    def create_board(self, nums:list)->list:
        x:int=0
        y:int=0
        i:int=0
        
        for x in range(4):
            for y in range(4):
                self.gb.append((x,y,nums[i]))
                i+=1
                    
        return self.gb
    
    def move_tile(self, x, y):
        pass
    
    def get_tile_number(self, x_value, y_value)->int:
        pass
    
    def display(self):
        print(self.gb)

def arbitrary_nums_list()->list:
    """_summary_
    Puzzle nums is a list of numbers from 0-16. 
    0 represents the empty space in the puzzle board.
    """
    puzzle_nums = [0, 1, 2, 3, 4, 5, 6, 7,
                   8, 9, 10, 11, 12, 13, 14, 15]
    
    random.shuffle(puzzle_nums)
    print("Number Order: ",puzzle_nums)
    return puzzle_nums

def create_puzzle_board(numbers):
    puzzle_board =[]
    rows, cols = 4,4
    k=0
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(numbers[k])
            k+=1
        puzzle_board.append(col)
    return puzzle_board

def find_empty_space(board:list):
    for x in range(4):
        for y in range(4):
            if board[x][y] == 0:
                return (x,y)

def main():
    numbers = arbitrary_nums_list()
    puzzle_board = create_puzzle_board(numbers)

    for i in puzzle_board:
        print('\t'.join(map(str, i)))
        
    graph = Graph()
    graph.actions(puzzle_board)
    graph.dispay()
    
if __name__ == "__main__":
    main()
    

