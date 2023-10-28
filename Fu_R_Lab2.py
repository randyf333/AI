#https://academics.tjhsst.edu/compsci/ai/words.txt
import math


def main():
    word_dict = {}
    words = set(open("words.txt").read().split("\n"))
    for word in words:
        word_dict[word] = generate_adjacents(word,words)
    s = input("Input First Word: ")
    e = input("Input Second Word: ")
    path = BFS(s,e,word_dict)
    print(path)
    print('The number of steps: ' + str(len(path)))
    l = input("Type the limit (1-20): ")
    s = input("Type the starting word: ")
    e = input("Type the goal word: ")
    path = DLS(s,e,word_dict,int(l))
    print('Path: ' + str(path))
    print('Steps within '+ l + ' limit: ' + str(len(path)))
    shortest_Path = DDFS(s,e,word_dict,int(l))
    print('Shortest Path: '+str(shortest_Path))
    print('Steps: ' + str(len(shortest_Path)))

def generate_adjacents(current,word_list):
    adj_list = set()
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for num in range(len(current)):
        for let in alpha:
            letters = list(current)
            letters[num] = let
            s = "".join(letters)
            if s in word_list and s != current:
                adj_list.add(s)
    return adj_list

def BFS(start,end,word_dict): 
    explored = {start:""} #key is child value is parent
    frontier = [start]
    while len(frontier) > 0:
      current = frontier.pop(0)
      #del frontier[0]
      if current == end:
         #print(explored)
        #with open("explored.txt",'w') as f:
            #for key, value in explored.items():
               #f.write('%s:%s\n' % (key,value))
        path = []
        while explored[current] != "":
            path.append(current)
            current = explored[current]
        path.append(current)
        #print(path[::-1])
        
        #print("The number of steps " + str(len(path)))
        return path[::-1]
      kids = generate_adjacents(current,word_dict)
      for x in kids:
        if x not in explored.keys():
            frontier.append(x)
            explored[x] = current
    return(["No solution"],0)

def recur(start,end,word_dict,explored,limit):
    explored = explored
    frontier = [start]
   # while len(frontier) > 0:
    current = frontier.pop()
    if current == end:
        path = []
        while explored[current] != "":
                path.append(current)
                current = explored[current]
        path.append(current)
        return(path[::-1])
    elif limit <= 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        kids = generate_adjacents(current,word_dict)
        for x in kids:
            if x not in explored:
                explored[x] = current
            new_explored = {key : explored[key] for key in explored}
            result = recur(x,end,word_dict,new_explored,limit-1)
            if result == 'cutoff': 
                cutoff_occurred = True
            elif result != None and result != 'cutoff': 
                return result
            elif cutoff_occurred: 
                return 'cutoff'
    return None
def DLS(start,end,word_dict,limit):
    explored = {start:""}
    return recur(start,end,word_dict,explored,limit-1)
def DDFS(start, end, word_dict,limit):
    for depth in range(limit):
        result = DLS(start,end,word_dict,depth)
        if result != 'cutoff' and result != None:
            return result
    return None
if __name__ == '__main__':
   main()

