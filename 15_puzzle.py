import random
from collections import defaultdict

class Graph:
    
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
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
    

def main():
    numbers = arbitrary_nums_list()
    game_board = Game_Board()
    game_board.create_board(numbers)
    game_board.display()
    
if __name__ == "__main__":
    main()
    

