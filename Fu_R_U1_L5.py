# Name:          Date:
import heapq
from os import X_OK
import time
import math

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()   
   # TODO 1: adjacents
   # Your code goes here
   alpha = list("abcdefghijklmnopqrstuvwxyz")
   for num in range(len(current)):
        for let in alpha:
            letters = list(current)
            letters[num] = let
            s = "".join(letters)
            if s in words_set and s != current:
                adj_set.add(s)
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   st_frontier = [start] 
   g_frontier = [goal]
   st_explored = {start:""}
   g_explored = {goal:""}
   path = []
 #key is child value is parent
   while len(st_frontier) > 0 and len(g_frontier) > 0: #len(st_frontier) > 0 and :
      stcur = st_frontier.pop(0)  
      kids = generate_adjacents(stcur,words_set)
      for x in kids:
        if x not in st_explored.keys():
            st_frontier.append(x)
            st_explored[x] = stcur
            if x in g_explored.keys():
               #path.append(x)
               temp = x
               while st_explored[x] != "":
                  path.append(x)
                  x = st_explored[x]
               path.append(x)
               path = path[::-1]
               path.pop()
               while g_explored[temp] != "":
                  path.append(temp)
                  temp = g_explored[temp]
               path.append(temp)
               return path
      gcur = g_frontier.pop(0)
      gkids = generate_adjacents(gcur,words_set)
      for y in gkids:
         if y not in g_explored.keys():
            g_frontier.append(y)
            g_explored[y] = gcur
            if y in st_explored.keys():
               temp = y
               while st_explored[y] != "":
                  path.append(y)
                  y = st_explored[y]
               path.append(y)
               path = path[::-1]
               #path.append(y)
               path.pop()
               while g_explored[temp] != "":
                  path.append(temp)
                  temp = g_explored[temp]
               path.append(temp)
               return path
   return None


class HeapPriorityQueue():
   def __init__(self):
      #self.queue = ["dummy"]
      self.queue = [[math.inf,"dummy",[]]]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self

   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]
   
     # helper method for push
   def heapUp(self, k):
      while k > 0:
         parent = k//2
         if parent > 0 and self.queue[k][0] < self.queue[parent][0]:
            self.swap(k,parent)
         k = parent

               

   # Add a value to the heap_pq
   def push(self, value):
      #self.queue.append(value)
      # write more code here to keep the min-heap property
      #self.heapUp(len(self.queue)-1)
      heapq.heappush(self.queue,value)
        
  
   # helper method for reheap and pop
   def heapDown(self, k, size):
      while k < size:
         smallest = k
         l = k*2
         r = k*2+1
         if l < size and self.queue[l][0] < self.queue[smallest][0]:
            smallest = l
         if r < size and self.queue[r][0] < self.queue[smallest][0]:
            smallest = r
         if smallest != k:
            self.swap(smallest,k)
         k = l
   
   # make the queue as a min-heap            
   def reheap(self):
      #for x in range(1,len(self.queue)):
      self.heapDown(1,len(self.queue)-1)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      #value = self.queue.pop(1)
      #self.reheap()
      #return value # change this
      return heapq.heappop(self.queue)
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      self.swap(index,len(self.queue)-1)
      num = self.pop(index)
      self.heapDown(index,len(self.queue))
      #self.swap(self.queue[len(self.queue)-1], self.queue[index])
      return num    

def dist_heuristic(current, goal):
   count = 0
   for c in range(len(current)):
      if current[c] != goal[c]:
         count += 1
   return count

def a_star(start,goal,words_set):
   frontier = HeapPriorityQueue()
   length = 0 #path length
   x = [dist_heuristic(start,goal),start,length,[start]]
   explored = {}
   while x[1] != goal:
      explored[x[1]] = x[0]
      kids = generate_adjacents(x[1],words_set)
      for k in kids:
         cost = x[2]+1
         y = dist_heuristic(k,goal)+cost
         if k not in explored:
            frontier.push([y,k,cost,x[3]+[k]])
         else:
            if y < explored[k]:
               frontier.push([y,k,cost,x[3]+[k]])
               explored[k] = y
      if frontier.isEmpty():
         return None
      else:
         x = frontier.pop()
   return x[3]

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   #path = (bi_bfs(initial, goal, words_set))
   path = (a_star(initial,goal,words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''


'''
frontier = [[start],[goal]]
explored = [{start:""},{}]
while _________:
   k = 1-k        0->1
                  1->0


'''