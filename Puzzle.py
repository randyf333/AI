# Name:Marvin Fu          Date:
import heapq
import random, time, math

class PriorityQueue():
   """Implementation of a priority queue 
   to store nodes during search."""
   # TODO 1 : finish this class
   
   # HINT look up/use the module heapq.

   def __init__(self):
      self.queue = []
      self.dic = {}
      self.current = 0    

   def next(self):
      if self.current >=len(self.queue):
         self.current
         raise StopIteration
   
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def pop(self):
      # Your code goes here
      item = heapq.heappop(self.queue)
      if item[1] not in self.dic:
          while True:
            item = heapq.heappop(self.queue)
            if item[1] in self.dic:
                break
      
      self.dic.pop(item[1])
      return item #pops lowest node
   
       
   def remove(self, nodeId):
     # Your code goes here
     item = self.dic.pop(nodeId)
     self.queue.remove(item)

     """ for l in self.queue:
         if l[1]==nodeId:#check if ID matches
             self.queue.remove(l)#removes node
     return self.queue """

   def __iter__(self):
      return self

   def __str__(self):
      return 'PQ:[%s]'%(', '.join([str(i) for i in self.queue]))

   def append(self, node):
      if node[1] in self.dic:
          item = self.dic[node[1]]
          if (node[0] < item[0]):
              self.dic[node[1]] = node
            #   self.queue.remove(item)
              heapq.heappush(self.queue,node)
      else:
          self.dic[node[1]] = node
          heapq.heappush(self.queue,node)#adds node to PQ, making sure to preserve the heap
      return self.queue
  
   def __contains__(self, key):
      self.current = 0
      return key in [n for v,n in self.queue]

   def __eq__(self, other):
      return self == other

   def size(self):
      return len(self.queue)
   
   def clear(self):
      self.queue = []
       
   def top(self):
      return self.queue[0]

   __next__ = next



def check_pq():
   ''' check_pq is checking if your PriorityQueue
   is completed or not'''
   pq = PriorityQueue()
   temp_list = []

   for i in range(10):
      a = random.randint(0,10000)
      pq.append((a,'a'+str(i)))
      temp_list.append(a)

   temp_list = sorted(temp_list)   
   
   for i in temp_list:
      j = pq.pop()
      if not i == j[0]:
         return False

   return True

# Extension #1
def inversion_count(new_state, size):
   ''' Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is odd.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is even.
   ''' 
   # Your code goes here
   count=0
   for p in range(1,len(new_state)):
           if new_state[p]=='_':
               continue
           for c in range(p):
               if ord(new_state[p])>ord(new_state[c]):
                   count+=1
   if size%2==0:
       i=new_state.index('_')
       if i//size%2==0:
           if count%2==1:
               return True
   else:
       if count%2==0:
           return True
   return False

def getInitialState(sample):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   if(inversion_count(new_state, 4)): return new_state
   else: return None
   
def switch(x, y, z):
    a=min(y,z)
    b=max(y,z)
    r=x[:a]+x[b]+x[a+1:b]+x[a]+x[b+1:]
    return r

def canRight(i,size):
    return i%size<size-1
def canLeft(i,size):
    return i%size>0
def canUp(i,size):
    return i>=size
def canDown(i,size):
    return i<size*(size-1)
def generateChild(n, size):
   # Your code goes here
    r=[]
    i=n.index('_')
    if canRight(i,size):
        r.append(switch(n,i,i+1))
    if canLeft(i,size):
        r.append(switch(n,i,i-1))
    if canUp(i,size):
        r.append(switch(n,i,i-size))
    if canDown(i,size):
        r.append(switch(n,i,i+size))
    return r

def display_path(path_list, size):
   for n in range(size):
      for i in range(len(path_list)):
         print (path_list[i][n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""


def dist_heuristic(start, goal, size):
   # Your code goes here
   count=0
   for c in start:
       si=start.index(c)
       gi=goal.index(c)
       if si==gi:
           continue
       else:
           sci=si%size
           gci=gi%size
           count+=abs(sci-gci)
           sri=si//size
           gri=gi//size
           count+=abs(sri-gri)           
   return count

def a_star2(start, goal="_123456789ABCDEF", heuristic=dist_heuristic):
   frontier = PriorityQueue()
   if start == goal: return []
   size = 4
   # Your code goes here
   s=[start]
   x=[heuristic(start, goal,size)+1,start,s]
   explored={}
   while not x[1]==goal:
       explored[x[1]]=x[0]
       z=generateChild(x[1],size)
       for p in z:
           t=list(x[2])
           t.append(p)
           y=heuristic(p,goal,size) +len(t)
           if p not in explored:
               frontier.append([y,p,t])
           else:
               if y<explored[p]:
                    frontier.append([y,p,t])
                    explored[p]=y
       if frontier.size() == 0:
           x=None
           break
       x=frontier.pop()
   if x==None:
       return "No Solution"  
   return x[2]

def main():
   # check PriorityQueue
   if check_pq(): print ("PriorityQueue is good to go.")
   else: print ("PriorityQueue is not ready.")

   # A star
   
   #initial_state = getInitialState("_123456789ABCDEF")
   #while initial_state == None:
   #   initial_state = getInitialState("_123456789ABCDEF")
   print(inversion_count("152349678_ABCDEF",4))
   initial_state = input("Type initial state: ")
   cur_time = time.time()
   path = (a_star2(initial_state))
   if path != None: display_path(path, 4)
   else: print ("No Path Found.")
   print ("Duration: ", (time.time() - cur_time))

if __name__ == '__main__':
   main()

''' Sample output 1
PriorityQueue is good to go.

Initial State: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0

Sample output 2
PriorityQueue is good to go.

Initial State: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005984306335449219

Sample output 3
PriorityQueue is good to go.

Initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.34381628036499023
'''