import random, time, heapq,math
hlut = {}
class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
   def __init__(self):
      #self.queue = ["dummy"]
      self.queue = [(math.inf, math.inf,"dummy",["dummy"])]  # we do not use index 0 for easy index calulation
      #self.current = 1
      self.current = 0        # to make this object iterable

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
      #self.heapDown(1,len(self.queue)-1)
      heapq.heapify(self.queue)
   
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

def inversion_count(new_state, width = 4, N = 4):
   ''' 
   Depends on the size(width, N) of the puzzle, 
   we can decide if the puzzle is solvable or not by counting inversions.
   If N is odd, then puzzle instance is solvable if number of inversions is even in the input state.
   If N is even, puzzle instance is solvable if
      the blank is on an even row counting from the bottom (second-last, fourth-last, etc.) and number of inversions is even.
      the blank is on an odd row counting from the bottom (last, third-last, fifth-last, etc.) and number of inversions is odd.
   ''' 
   # Your code goes here
   state = list(new_state)
   index = state.index('_')
   count = 0
   for x in range(len(state)):
       for y in range(x+1,len(state)):
          if state[x] == '_' or state[y] == '_':
             count += 0
          elif state[x] > state[y]:
                count += 1
            
   if N%2 == 1:
       if count%2 == 0:
           return True
   else:
       if (index >= 0 and index < 4) or (index >= 8 and index < 12):
            if count % 2 == 0:
                return True
       if (index >= 4 and index < 8) or (index >= 12 and index < 16):
            if count % 2 == 1:
                return True
   return False
   '''
   _42
   135
   678

   4123
   C98B
   DA78
   5_EF
   '''

def check_inversion():
   t1 = inversion_count("_42135678", 3, 3)  # N=3
   f1 = inversion_count("21345678_", 3, 3)
   t2 = inversion_count("4123C98BDA765_EF", 4) # N is default, N=4
   f2 = inversion_count("4123C98BDA765_FE", 4)
   return t1 and t2 and not (f1 or f2)


def getInitialState(sample, size):
   sample_list = list(sample)
   random.shuffle(sample_list)
   new_state = ''.join(sample_list)
   while not inversion_count(new_state, size, size): 
      random.shuffle(sample_list)
      new_state = ''.join(sample_list)
   return new_state
   
def swap(n, i, j):
   # Your code goes here
   nums = list(n[1])
   nums[i],nums[j] = nums[j],nums[i]
   state = "".join(nums)
   return state
      
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state, size=4):
   children = []
   blank = state[1].find('_')
   '''your code goes here'''
   if blank - 4 >= 0:
      x = swap(state,blank,blank-4)
      children.append((len(state[2])+dist_heuristic(x),x,state[2]+[x]))
      #children.append((len(state[2])-1+dist_heuristic(x),x,state[2]))

   if (blank - 1)%size < 3:
      x = swap(state,blank,blank-1)
      children.append((len(state[2])+dist_heuristic(x),x,state[2]+[x]))
      #children.append((len(state[2])-1+dist_heuristic(x),x,state[2]))
   
   if blank + 4 < len(state[1]):
      x = swap(state,blank,blank+4)
      children.append((len(state[2])+dist_heuristic(x),x,state[2]+[x]))
      #children.append((len(state[2])-1+dist_heuristic(x),x,state[2]))

   if (blank + 1)%size > 0:
      x = swap(state,blank,blank+1)
      children.append((len(state[2])+dist_heuristic(x),x,state[2]+[x]))
      #children.append((len(state[2])-1+dist_heuristic(x),x,state[2]))

   return children

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

''' You can make multiple heuristic functions '''
def setlookup(goal,size = 4):
   global hlut
   s=size*size
   for c in range(len(goal)):
      for place in range(s):
         hlut[(goal[c],place)]=abs(place%size-c%size)+abs(place//size-c//size)

def dist_heuristic(state, goal = "_123456789ABCDEF", size=4): #big manhatten
   #dist = 0
   ##board = list(goal)
   ##st = list(state)

   #for x in goal:
   #   if x != '_':
   #      i = state.find(x)
   #      j = goal.find(x)
   #      dist += abs(i % size - j % size) + abs(i//size - j//size)
   #return dist
    dist = 0
    global hlut
    i = 0
    for x in state:
        dist += hlut[x,i]
        i += 1
    return dist
   # Your code goes here


   

def incrimentman(state, prev, heuristic_value, goal = "_123456789ABCDEF", size = 4): #prev is previous node
   cur = state.find("_")
   before = prev.find("_")
   goal_index = 0
   dist = abs(cur%size - before%size) + abs(cur//size - before//size)
   otherdist = abs(cur%size) + abs(cur//size)
   finaldist = abs(dist-otherdist)
   #find which tile moved by comparing new index of _ with char at same index in old state
    
   return 
def check_heuristic():
   setlookup("_123456789ABCDEF")
   a = dist_heuristic("152349678_ABCDEF", "_123456789ABCDEF", 4)
   b = dist_heuristic("8936C_24A71FDB5E", "_123456789ABCDEF", 4)
   return (a < b) 

def a_star(start, goal="_123456789ABCDEF", heuristic=dist_heuristic, size = 4):
   '''frontier = HeapPriorityQueue()
   if start == goal: return []
   # Your code goes here
   pathlist = [start]
   frontier.push((heuristic(start),start,[start])) #tuple(f, state, path)
   while frontier == False:
      for y in frontier:
         if y[1] == goal:
            return y[2]
      current = frontier.pop()
      #if current[1] == goal:
         #return current[2]
      children = generate_children(current,size)
      for x in children:
         if x[1] not in pathlist:
            pathlist.append(x[1])
            frontier.push(x)'''
   #frontier = [(heuristic(start),start,[start])]
   frontier = HeapPriorityQueue()
   if start == goal: return []
   #pathlist = [start]
   pathlist = set()
   frontier.push((heuristic(start),start,[start]))
   #current = frontier.pop()
   while frontier.isEmpty() == False:
      '''for y in frontier:
         if goal in y:
            return y[2]'''
      current = frontier.pop()
      if current[1] == goal:
         return current[2]
      children = generate_children(current,size)
      for x in children:
         if x[1] not in pathlist:
            pathlist.add(x[1])
            frontier.push(x)
   return None
def aswap(n,i,j):
   nums = list(n)
   nums[i],nums[j] = nums[j],nums[i]
   state = "".join(nums)
   return state
def generate_adjacents(state, size=4):
   children = []
   blank = state.find('_')
   #blank = state[0].find("_")
   #g = state[2] + 1
   if blank - 4 >= 0:
      #x = aswap(state[0],blank,blank-4)
      #children.append((x,dist_heuristic(x),g))
      children.append(aswap(state,blank,blank-4))
   if (blank - 1)%size < 3:
      #x = aswap(state[0],blank,blank-1)
      #children.append((x,dist_heuristic(x),g))
      children.append(aswap(state,blank,blank-1))
   if blank + 4 < len(state):
     # x = aswap(state[0],blank,blank+4)
      #children.append((x,dist_heuristic(x),g))
      children.append(aswap(state,blank,blank+4))
   if (blank + 1)%size > 0:
      #x = aswap(state[0],blank,blank+1)
      #children.append((x,dist_heuristic(x),g))
      children.append(aswap(state,blank,blank+1))
   return children

def search(path, threshold, distance, goal = "_123456789ABCDEF", heuristic = dist_heuristic):
   node = list(path.keys())[-1]
   if node[0] == goal: return True
   cost = distance + heuristic(node[0],goal)
   if cost > threshold:
      return cost
   kids = generate_adjacents(node)
   minimun = math.inf
   for i in kids:
      if i not in path:
         path[i] = None
         temp = search(path, threshold, distance+1)
         if temp == True:
            return True
         if temp < minimun:
            minimun = temp
         path.popitem()
   return minimun

def getKids(state,size):
   matrix = ""
   matrix = matrix+"Total Cost: "+str(state[0])
   matrix += '\n'
   matrix = matrix+"Steps Cost: "+str(state[1])
   matrix += '\n'
   
   for n in range(size):
      matrix = matrix+str(state[2][n*size:(n+1)*size])+" "
      matrix = matrix+'\n'
   print( matrix)



def solve(start, goal = "_123456789ABCDEF",heuristic = dist_heuristic, size = 4):
    frontier = HeapPriorityQueue()
    bfrontier = [[goal,[]]]
    bpathlist = set()
    if start == goal: return []
    #pathlist = [start]
    pathlist = set()
    explored = {}
    bexplored = {goal:[]}
    state = (heuristic(start, goal),start,[start])
    #estate = (heuristic(goal,start),goal,[goal])
    frontier.push(state)
    #bfrontier.push(estate)
    way = 1
    #current = frontier.pop()

    while frontier.isEmpty() == False and len(bfrontier) > 0:
        st_current = frontier.pop()
        if st_current[1] in bexplored:
            return explored[st_current[1]][1] + bexplored[st_current][:-1][::-1]
        st_children = generate_adjacents(st_current)
        for child in st_children:
            h = heuristic(child)
            st_path = list(st_current[2])
            st_path.append(child)
            if child not in explored:
                frontier.push((h+len(path)-1,child,path))
                explored[kid] = [h,path]
            else:
                old_data = explored[child]
                if h < old_data[0]:
                    frontier.push((h+len(path)-1,child,path))
                    old_data[0] = h
        b_current = bfrontier.pop()
        if b_current in explored:
            return explored[b_current][1] + bexplored[b_current][:-1][::-1]
        b_kids = generate_adjacents(b_current)
        for kid in b_kids:
            if kid not in bexplored:
                bfrontier.append(kid)
                bexplored[kid] = b_current[1]+[kid]



    #while bstate[1] not in bexplored or estate not in explored or bstate[1] == goal or estate == start:
    #  '''for y in frontier:
    #     if goal in y:
    #        return y[2]'''
    #  children = generate_adjacents(bstate[1],size)
    #  for kid in children:
    #    h = heuristic(kid)
    #    path = list(bstate[2])
    #    path.append(kid)
    #    if kid not in explored:
    #       pathlist.add(bstate[1])
    #       frontier.push((h+len(path),kid,path))
    #       explored[kid] = [h,path]
    #    else:
    #       if h < explored[kid][0]:
    #           frontier.push((h+len(path),kid,path))
    #           explored[bstate[1]] = [h,path]
    #  bstate = frontier.pop()
    #  if bstate[1] in bexplored: way = 2
    #        #return explored[x[1]][::-1] + bexplored[x[1]][::-1]
    #  #bexplored[estate[1]] = [estate[0],estate[2]]
    #  bchildren = generate_adjacents(estate,size)
    #  for kids in bchildren:
    #      if kids not in bexplored:
    #          bfrontier.append(kids)
    #          bexplored[kids] = estate
    #  estate = bfrontier.pop()



    #  for y in bchildren:
    #    h = heuristic(y,start)
    #    bpath = list(estate[2])
    #    bpath.append(y)
    #    if y not in bexplored:
    #       bpathlist.add(y[1])
    #       bfrontier.push((h+len(bpath),y,bpath))
    #       bexplored[y] = [h,bpath]
    #    else:
    #       if h < bexplored[y][0]:
    #           bfrontier.push((h+len(bpath),y,bpath))
    #           bexplored[estate[1]] = [h,bpath]
    #  estate = bfrontier.pop()
    #        #1_23456789ABCDEF
    #if way == 1:
    #    return explored[bstate[1]][1] + bexplored[bstate[1]][1][:-1][::-1]
    #else:
    #    #trail = bexplored[estate[1]][1]
    #    #del trail[-1]
    #    return explored[estate[1]][1] + bexplored[estate[1]][1][:-1][::-1]

    
    '''path = []
    temp = y
    while explored[y[1]][2] != None:
        path.append(y[1])
        y = explored[y]
        path.append(y[1])
        path = path[::-1]
        path.pop()
        while bexplored[temp][2] != None:
           path.append(temp[1])
           temp = explored[temp]
           path.append(temp[1])
           return path'''
     


   ##threshold = heuristic(start,goal)
   ##x = (start, threshold, 0)
   ##explored = {x: None}
   ##while 1:
   ##   tmp = search(explored, threshold, 0, goal, heuristic)
   ##   if tmp == True:
   ##      return explored.keys()
   ##   elif tmp == math.inf:
   ##      return None
   ##   threshold = tmp
   #frontier = HeapPriorityQueue()
   #backfrontier = HeapPriorityQueue()
   #if start == goal: return []
   
   ##s = [start]
   #pathset = set() #open set
   #backset = set()
   
   ##s = (start,)
   ##x = (heuristic(start,goal)+1,start,s)
   #x = [heuristic(start,goal),0,start,None]
   #y = [0,0,goal,None]
   #frontier.push(x)
   #explored = {start: x}#closedset
   #backexplored = {goal: y}
   #backfrontier.push(y)
   ##explored = {x[0], start}
   ##setlookup(goal)
   #while frontier and backfrontier:
   #   #pop_time = time.time()
   #   current_data = frontier.pop()
   #   #pop_count+=1
   #   #print("Pop time: " , (time.time()-pop_time))
   #   f_current, g_current, current, parent_data = current_data

   #   #if current_data in backexplored:
   #   #   #print("Pop count"+str(pop_count))
   #   #   #print("Push count"+str(push_count))
   #   #   def path(data):
   #   #      while data:
   #   #         yield data[2]
   #   #         data = data[3]
   #   #   return list(path(current_data))[::-1]

   #   del explored[current]
   #   pathset.add(current)
   #   children = generate_adjacents(current)
   #  # hold = 0
   #   for kids in children:
   #       if kids in backexplored:
   #           path = []
   #           temp = kids
   #           while explored[kids] != None:
   #               path.append(kids)
   #               kids = explored[kids]
   #               path = path[::-1]
   #               path.pop()
   #           while backexplored[temp] != None:
   #               path.append(temp)
   #               temp = backexplored[temp]
   #           path.append(temp)
   #           return path
   #       if kids in pathset:
   #         continue

   #       g_kids = g_current+1
   #       f_kids = heuristic(kids,goal)+g_kids
   #       #kidsdata = [f_kids,g_kids, kids, current_data]
   #       kidsdata = [f_kids,g_kids,kids,current]
         
   #       if kids not in explored:
   #          explored[kids] = kidsdata
   #          #explored[f_kids] = kidsdata
   #          #add_time = time.time()
   #          frontier.push(kidsdata)
   #         #push_count+=1
   #         #print("Add Time: ", (time.time()-add_time))
   #       else:
   #          old_data = explored[kids]
   #          if kidsdata < old_data:
   #            #copy_time = time.time()

   #             old_data[:] = kidsdata #updates cost if new explored cost is less then old

   #            #print("Copy Time: ", (time.time()-copy_time))
   #            #frontier.reheap()
   #   back_data = backfrontier.pop()
   #   bf_current, bg_current, bcurrent, bparent_data = back_data
   #   del back_data[bcurrent]
   #   backset.add(bcurrent)
   #   bchildren = generate_adjacents(bcurrent)
   #   for bkids in bchildren:
   #       if bkids in explored:
   #           path = []
   #           temp = bkids
   #           while explored[bkids] != None:
   #               path.append(bkids)
   #               bkids = explored[



   #return None

'''explored = {}
   while x[1] != goal:
      #explored[x[1]] = x[0]
      #explored[x[0]] = x[2]
      kids = generate_adjacents(x[1],size)
      for k in kids:
         y = list(x[2])
         y.append(k)
         h = heuristic(k,goal,size)
         if k not in explored:
         #if k not in explored.values():
            frontier.push((h+len(y),k,y))
         else:
            if h < explored[k]:
               frontier.push((h+len(y),k,y))
               explored[x[1]] = h 
               #explored[x[0]] = x[1]
      if frontier.isEmpty():
         return None
      else:
         x = frontier.pop()
      while x[1] in explored:
      #while x[1] in explored.values():
         if x[0] < explored[x[1]]:
            break
         else:
            x = frontier.pop()
   return x[2]'''

def main():
    # A star
   print ("Inversion works?:", check_inversion())
   print ("Heuristic works?:", check_heuristic())
   initial_state = getInitialState("_123456789ABCDEF", 4)
   initial_state = input("Type initial state: ")
   if inversion_count(initial_state):
      cur_time = time.time()
      #path = (a_star(initial_state))
      path = (solve(initial_state))
      if path != None: display_path(path, 4)
      else: print ("No Path Found.")
      print ("Duration: ", (time.time() - cur_time))
   else: print ("{} did not pass inversion test.".format(initial_state))
   
if __name__ == '__main__':
   main()


''' Sample output 1

Inversion works?: True
Heuristic works?: True
Type initial state: 152349678_ABCDEF
1523    1523    1_23    _123    
4967    4_67    4567    4567    
8_AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 4
Duration:  0.0


Sample output 2

Inversion works?: True
Heuristic works?: True
Type initial state: 2_63514B897ACDEF
2_63    _263    5263    5263    5263    5263    5263    5263    5263    52_3    5_23    _523    1523    1523    1_23    _123    
514B    514B    _14B    1_4B    14_B    147B    147B    147_    14_7    1467    1467    1467    _467    4_67    4567    4567    
897A    897A    897A    897A    897A    89_A    89A_    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    89AB    
CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 16
Duration:  0.005014657974243164


Sample output 3

Inversion works?: True
Heuristic works?: True
Type initial state: 8936C_24A71FDB5E
8936    8936    8936    893_    89_3    8943    8943    8_43    84_3    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
C_24    C2_4    C24_    C246    C246    C2_6    C_26    C926    C926    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 37
Duration:  0.27825474739074707


Sample output 4

Inversion works?: True
Heuristic works?: True
Type initial state: 8293AC4671FEDB5_
8293    8293    8293    8293    8293    8293    8293    8293    82_3    8_23    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    8423    _423    4_23    4123    4123    4123    4123    _123    
AC46    AC46    AC46    AC46    AC46    _C46    C_46    C4_6    C496    C496    C_96    C9_6    C916    C916    C916    C916    C916    C916    C916    C916    C916    _916    9_16    91_6    916_    9167    9167    9167    9167    9167    9167    _167    8167    8167    8_67    8567    8567    _567    4567    
71FE    71F_    71_F    7_1F    _71F    A71F    A71F    A71F    A71F    A71F    A71F    A71F    A7_F    A_7F    AB7F    AB7F    AB7F    AB7_    AB_7    A_B7    _AB7    CAB7    CAB7    CAB7    CAB7    CAB_    CA_B    C_AB    C5AB    C5AB    _5AB    95AB    95AB    95AB    95AB    9_AB    _9AB    89AB    89AB    
DB5_    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    DB5E    D_5E    D5_E    D5E_    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D5EF    D_EF    _DEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    CDEF    

The shortest path length is : 39
Duration:  0.7709157466888428

'''




'''
Dictionary of lists

'''