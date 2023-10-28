# import sys; args = sys.argv[1:]
# puzzles = open(args[0], "r").read().splitlines()
import time

puzzles = open('puzzles.txt','r').read().splitlines()
# global count
# count = 0
# optional helper function
def select_unassigned_var(assignment, variables, neighbors):
   #for i in range(len(assignment)):
   #   if assignment[i] == '.':
   #      return i
   if '.' not in assignment:
      return
   index = 0
   options = 9
   for i in variables:
      length = len(variables[i])
      # if length == 1 and assignment[i] == '.':
      #    return i
      if length < options and assignment[i] == '.':
            index = i
            options = length
   return index


def isValid(value, var_index, assignment, variables, neighbors):
   if len(variables[var_index]) != 1:
      for x in neighbors[var_index]:
         if assignment[x] == str(value):
            return False
   # for part in csp_table:
   #    if var_index in part:
   #       for index in part:
   #          if assignment[index] == str(value):
   #             return False 
   return True

# optional helper function
def ordered_domain(var_index, variables, q_table):
   newdomain = []
   # for x in q_table:
   #     if x in variables[var_index]:
   
   if var_index in variables:
      #return sorted(variables[var_index], key=q_table.get)
      sortedq = sorted(q_table.items(),key = lambda item: item[1], reverse=True)
      for x in sortedq:
         if x[0] in variables[var_index]:
            newdomain.append(x[0])
      return newdomain
   return None
# optional helper function
def update_variables(value, var_index, variables, neighbors, assignment, q_table):
   assign = list(assignment)
   copy = {k:vals[:] for k, vals in variables.items() if k!=var_index}
   #del copy[var_index]
   # if len(copy[var_index]) <= 1:
   #    del copy[var_index]
   # else:
   #    copy[var_index].remove(value)
   for neighbor in neighbors[var_index]:
      if neighbor in copy:
         if value in copy[neighbor]:
            copy[neighbor].remove(value)
        #  if len(copy[neighbor]) == 1:
        #        assign[neighbor] = str(copy[neighbor][0])
        #        del copy[neighbor]
         if neighbor in copy:
            for y in copy[neighbor]:
               if isValid(y,neighbor,assignment,variables,neighbors) == False:
                  copy[neighbor].remove(y)
   newassignment = ''.join(assign)
   # placed = []
   # for y in copy:
   #    if len(copy[y]) == 1:
   #       assignment[y] = str(copy[y][0])
   #       placed.append(y)
   # for z in placed:
   #    del copy[z]
   # newassignment = ''.join(assignment)
   return copy, newassignment
      
def solve(puzzle, neighbors):
   # initialize_ds function is optional helper function. You can change this part. 
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  # q_table is quantity table {'1': number of value '1' occurred, ...}
   return recursive_backtracking(puzzle, variables, neighbors, q_table)

# assignment[:var_index] + str(var_index) + assignment[var_index + 1:]
# optional helper function: you are allowed to change it
def recursive_backtracking(assignment, variables, neighbors, q_table):
   ''' Your code goes here'''
   if assignment.find('.') == -1: return assignment
   assign = list(assignment)
   var = select_unassigned_var(assignment,variables,neighbors)
   values = variables[var]
   for x in values:
      if isValid(x,var,assignment,variables,neighbors):
         #assign = assignment[:var] + str(x) + assignment[var + 1:]
         assign[var] = str(x)
         newassignment = ''.join(assign)
         q_table[x]+=1
         for y in neighbors[var]:
            newdomain = ordered_domain(y, variables, q_table)
            if newdomain != None:
               variables[y] = newdomain
         newvariables, newassignment = update_variables(x,var,variables,neighbors,newassignment,q_table)#,assign) # added assignment
         # global count
         # count += 1
         result = recursive_backtracking(newassignment,newvariables,neighbors,q_table)
         if result != None:
            return result
         #assign = assign[:var] + '.' + assign[var + 1:]
         assign[var] = '.'
   return None

def sudoku_csp(n=9):
   ''' Your code goes here '''
   table = []
   for k in range(0,81,9):
      rowlist = []
      for i in range(k,k+9):
         rowlist.append(i)
      table.append(rowlist)
   #col index 9-17
   for a in range(9):
      collist = []
      for b in range(a,81,9):
         collist.append(b)
      table.append(collist)
   #squares index 18-26
   table = table+[[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26]
   ,[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53]
   ,[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
   return table

def sudoku_neighbors(csp_table): # {0:[0, 1, 2, 3, 4, ...., 8, 9, 18, 27, 10, 11, 19, 20], 1:
   ''' Your code goes here '''
   neighbors = {}
   for a in range(81):
      neighborlist = []
      for x in csp_table:
         if a in x:
            for y in x:
               if y not in neighborlist:
                  neighborlist.append(y)
      neighbors[a] = neighborlist
   return neighbors

# Optional helper function
def initialize_ds(puzzle, neighbors):
   ''' Your code goes here '''
   #print (vars, puzzle, q_table) 
   variables = {}
   quantity = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
   for x in range(len(puzzle)):
      if puzzle[x] == '.':
         values = [1,2,3,4,5,6,7,8,9]
         for a in neighbors[x]:
               for y in range(1,10):
                     if puzzle[a] == str(y) and y in values:
                        values.remove(y)
         variables[x] = values
   for z in puzzle:
      if z != '.':
         if int(z) in quantity:
            quantity[int(z)] += 1
   return variables, puzzle, quantity


# sum of all ascii code of each char - (length of the solution * ascii code of min char)
def checksum(solution):
   ''' write your code here'''
   sum = 0
   for x in solution:
      sum += ord(x)
   return sum -(len(solution)*ord(min(solution)))

def main():
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   
   # for line, puzzle in enumerate(puzzles):
   #   line, puzzle = line+1, puzzle.rstrip()
   #   print ("{}: {}".format(line, puzzle)) 
   #   solution = solve(puzzle, neighbors)
   #   if solution == None:print ("No solution found."); break
   #   print ("{}{} {}".format(" "*(len(str(line))+2), solution, checksum(solution)))
   # print ("Duration:", (time.time() - start_time))


   puzzle = input("Type a 81-char string: ")
   solution = solve(puzzle, neighbors)
   if solution == None:print('No solution')
   print(solution)
   print ("Duration:", (time.time() - start_time))
   print(checksum(solution))
  # print(count)

if __name__ == '__main__': main()
# Required comment: Your name, Period #, 2022
# Check the example below. You must change the line below before submission.
# Randy Fu, Period 5, 2022
