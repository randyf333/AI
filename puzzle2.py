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
      #self.dic = {}
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
      #if item[1] not in self.dic:
      #    while True:
      #      item = heapq.heappop(self.queue)
      #      if item[1] in self.dic:
      #          break
      
      #self.dic.pop(item[1])
      return item #pops lowest node
   
       
   #def remove(self, nodeId):
   #  # Your code goes here
   #  item = self.dic.pop(nodeId)
   #  self.queue.remove(item)

   #  """ for l in self.queue:
   #      if l[1]==nodeId:#check if ID matches
   #          self.queue.remove(l)#removes node
   #  return self.queue """

   def __iter__(self):
      return self

   def __str__(self):
      return 'PQ:[%s]'%(', '.join([str(i) for i in self.queue]))

   def append(self, node):
      #if node[1] in self.dic:
      #    item = self.dic[node[1]]
      #    if (node[0] < item[0]):
      #        self.dic[node[1]] = node
      #        self.queue.remove(item)
      #        heapq.heappush(self.queue,node)
      #else:
      #    self.dic[node[1]] = node
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
    #r=x[:a]+x[b]+x[a+1:b]+x[a]+x[b+1:]
    r=f'{x[:a]}{x[b]}{x[a+1:b]}{x[a]}{x[b+1:]}'
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
   listlen= len(path_list)
   start =0
   setLen = 14
   leftLen = listlen
   while leftLen >0:
       if (leftLen > setLen):
          end = start + setLen
       else:
          end= start + leftLen
       for n in range(size):
          for i in range(start,end):
             print(path_list[i][n*size:(n+1)*size], end = " "*size)
          print()
       print()
       leftLen -=setLen
       start = end
       
   print ("\nThe shortest path length is :", len(path_list))
   return ""

def dist_heuristic1(start, goal, size):
   # Your code goes here
   count=0
   for c in start:
       i=start.index(c)
       o=goal.index(c)
       if i==o:
           continue
       else:
           while i%size>o%size:
               i-=1
               count+=1
           while i%size<o%size:
               i+=1
               count+=1
           while i//size>o//size:
               i-=size
               count+=1
           while i//size<o//size:
               i+=size
               count+=1
   return count

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
#    x=[heuristic(start, goal,size),start,s]
   history ={}
   history[x[1]]=x[0]
   explored={}
   while not x[1]==goal:
       explored[x[1]]=x[0]
       z=generateChild(x[1],size)
       for p in z:
           t=list(x[2])
           t.append(p)
           y=heuristic(p,goal,size) +len(t)
           if p not in history:
               node = [y,p,t]
               history[p] =y 
               frontier.append(node)
           else:
               if y<history[p]:
                    frontier.append([y,p,t])
                    history[p]=y
                    if p in explored:
                        explored[p] =y
       if frontier.size() == 0:
           x=None
           break
       x=frontier.pop()
       while x[1] in explored:
           if x[0] >= explored[x[1]]:
               if frontier.size() == 0:
                    x=None
                    break
               x=frontier.pop()
   if x==None:
       return "No Solution"  
   
   print("explored count = " + str(len(explored)))
   inputlist =[]
   linea ='8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123'
   outlist=linea.split()
   inputlist.append('C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567')
   inputlist.append('A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB')
   inputlist.append('DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF')
   for item in inputlist:
        lineB = item.split()
        for i in range(len(lineB)):
            outlist[i] = outlist[i] + lineB[i]
   i = 0
   for word in outlist:
        i = i +1
        if word in history:
            cost = history[word]
            y = heuristic(word,goal,size)
            print (f'{i} {y} {word} {cost} {i+y}')
        else:
            print (f'missing word {word}')
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
   #initial_state = '8936C_24A71FDB5E'
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

'''
8936    8936    8936    8936    8936    8936    8936    8936    8936    8_36    _836    1836    1836    1_36    13_6    1376    1376    1376    1376    1376    1376    1376    1376    1376    1376            137_    13_7    1_37    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    123_    12_3    1_23    _123
C_24    C724    C724    C7_4    C_74    C174    C174    _174    1_74    1974    1974    _974    9_74    9874    9874    98_4    9824    9824    9824    9824    9824    _824    8_24    82_4    824_            8246    8246    8246    8_46    84_6    8456    8456    8456    8456    8456    8456    8456    _456    4_56    45_6    456_    4567    4567    4567    4567
A71F    A_1F    A1_F    A12F    A12F    A_2F    _A2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA_F    CA5F    CA5F    CA5F    _A5F    9A5F    9A5F    9A5F    9A5F            9A5F    9A5F    9A5F    9A5F    9A5F    9A_F    9ABF    9ABF    9AB_    9A_B    9_AB    _9AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB_E    D_BE    _DBE    CDBE    CDBE    CDBE    CDBE    CDBE            CDBE    CDBE    CDBE    CDBE    CDBE    CDBE    CD_E    CDE_    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF
'''
'''
Type initial state: 8936C_24A71FDB5E
explored count = 2497113
1 32 8936C_24A71FDB5E 33 33
2 34 8936C2_4A71FDB5E 36 36
3 34 8936C24_A71FDB5E 37 37
4 32 893_C246A71FDB5E 36 36
5 30 89_3C246A71FDB5E 35 35
6 32 8943C2_6A71FDB5E 38 38
7 30 8943C_26A71FDB5E 37 37
8 28 8_43C926A71FDB5E 36 36
9 28 84_3C926A71FDB5E 37 37
10 28 8423C9_6A71FDB5E 38 38
11 28 8423C916A7_FDB5E 39 39
12 26 8423C916A_7FDB5E 38 38
13 26 8423C916AB7FD_5E 39 39
14 26 8423C916AB7FD5_E 40 40
15 26 8423C916AB7FD5E_ 41 41
16 24 8423C916AB7_D5EF 40 40
17 22 8423C916AB_7D5EF 39 39
18 20 8423C916A_B7D5EF 38 38
19 18 8423C916_AB7D5EF 37 37
20 16 8423_916CAB7D5EF 36 36
21 18 84239_16CAB7D5EF 39 39
22 18 842391_6CAB7D5EF 40 40
23 18 8423916_CAB7D5EF 41 41
24 18 84239167CAB_D5EF 42 42
25 16 84239167CA_BD5EF 41 41
26 14 84239167C_ABD5EF 40 40
27 14 84239167C5ABD_EF 41 41
28 12 84239167C5AB_DEF 40 40
29 10 84239167_5ABCDEF 39 39
30 8 8423_16795ABCDEF 38 38
31 6 _423816795ABCDEF 47 37
32 6 4_23816795ABCDEF 46 38
33 6 41238_6795ABCDEF 45 39
34 6 412385679_ABCDEF 46 40
35 4 41238567_9ABCDEF 45 39
36 2 4123_56789ABCDEF 44 38
37 0 _123456789ABCDEF 45 37
8936    8936    8936    8936    8936    8936    8936    8936    8936    8_36    _836    1836    1836    1_36
C_24    C724    C724    C7_4    C_74    C174    C174    _174    1_74    1974    1974    _974    9_74    9874
A71F    A_1F    A1_F    A12F    A12F    A_2F    _A2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F    CA2F
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E

13_6    1376    1376    1376    1376    1376    1376    1376    1376    1376    1376    137_    13_7    1_37
9874    98_4    9824    9824    9824    9824    9824    _824    8_24    82_4    824_    8246    8246    8246
CA2F    CA2F    CA_F    CA5F    CA5F    CA5F    _A5F    9A5F    9A5F    9A5F    9A5F    9A5F    9A5F    9A5F
DB5E    DB5E    DB5E    DB_E    D_BE    _DBE    CDBE    CDBE    CDBE    CDBE    CDBE    CDBE    CDBE    CDBE

1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    1237    123_
8_46    84_6    8456    8456    8456    8456    8456    8456    8456    _456    4_56    45_6    456_    4567
9A5F    9A5F    9A_F    9ABF    9ABF    9AB_    9A_B    9_AB    _9AB    89AB    89AB    89AB    89AB    89AB
CDBE    CDBE    CDBE    CD_E    CDE_    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF

12_3    1_23    _123
4567    4567    4567
89AB    89AB    89AB
CDEF    CDEF    CDEF


The shortest path length is : 45
Duration:  141.69265723228455
'''