from math import perm
import queue
import random
import collections
def getInitialState():
   x = "_12345678"
   l = list(x)
   random.shuffle(l)
   y = ''.join(l)
   return y
   
'''precondition: i<j
   swap characters at position i and j and return the new state'''
def swap(state, i, j):
   '''your code goes here'''
   temp = list(state)
   temp[i],temp[j] = temp[j],temp[i]
   return ''.join(temp)
   
'''Generate a list which hold all children of the current state
   and return the list'''
def generate_children(state):
   '''your code goes here'''
   children = []
   if state.index('_') - 3 >= 0:
      children.append(swap(state,state.index('_'),state.index('_')-3))

   if (state.index('_') - 1)%3 < 2:
      children.append(swap(state,state.index('_'),state.index('_')-1))
   
   if state.index('_') + 3 < len(state):
      children.append(swap(state,state.index('_'),state.index('_')+3))

   if (state.index('_') + 1)%3 > 0:
      children.append(swap(state,state.index('_'),state.index('_')+1))

   return children
   
def display_path(n, explored): #key: current, value: parent
   l = []
   while explored[n] != "s": #"s" is initial's parent
      l.append(n)
      n = explored[n]
   print ()
   l = l[::-1]
   for i in l:
      print (i[0:3], end = "   ")
   print ()
   for j in l:
      print (j[3:6], end = "   ")
   print()
   for k in l:
      print (k[6:9], end = "   ")
   print ("\n\nThe shortest path length is :", len(l))
   return ""

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def BFS(initial_state):

   explored = {initial_state:'s'}
   '''Your code goes here'''
   frontier = [initial_state]
   while len(frontier) > 0:
      current = frontier.pop(0)
      #del frontier[0]
      if current == "_12345678":
         display_path('_12345678',explored)
         return ""
      kids = generate_children(current)
      for x in kids:
         #if x not in frontier and x not in explored.keys():
         if x not in explored.keys():
            frontier.append(x)
            explored[x] = current
   return ("No solution")
    
   

'''Find the shortest path to the goal state "_12345678" and
   returns the path by calling display_path() function to print all steps.
   You can make other helper methods, but you must use dictionary for explored.'''
def DFS(initial):
   explored = {initial:'s'}
   '''Your code goes here'''
   frontier = [initial]
   while len(frontier) > 0:
      current = frontier.pop()
      if current == "_12345678":
         display_path('_12345678',explored)
         return ""
      kids = generate_children(current)
      for x in kids:
         #if x not in frontier and x not in explored.keys():
         if x not in explored.keys():
            frontier.append(x)
            explored[x] = current
   return ("No solution")


def main():
   #initial = getInitialState()
   #initial = "1234567_8"
   #initial = "84765231_"
   initial = "14725836_"
   print ("BFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   print (BFS(initial))
   #print ("DFS start with:\n", initial[0:3], "\n", initial[3:6], "\n", initial[6:], "\n")
   #print (DFS(initial))

if __name__ == '__main__':
   main()
