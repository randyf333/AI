# Name:
# Date:
import time
def check_complete(assignment, csp_table):
   if assignment.count('.') == 0:
      return True
   return False
   
def select_unassigned_var(assignment, variables, csp_table):
   # index = random.randint(0,80)
   # while assignment[index] != '.':
   #    index = random.randint(0,80)
   for i in range(len(assignment)):
      if assignment[i] == '.':
         return i

def isValid(value, var_index, assignment, variables, csp_table):
   for part in csp_table:
      if var_index in part:
         for index in part:
            if assignment[index] == str(value):
               return False 
   return True

def ordered_domain(var_index, assignment, variables, csp_table):
   return []

def update_variables(value, var_index, assignment, variables, csp_table):
   if len(variables[var_index]) <= 1:
      del variables[var_index]
   else:
      variables[var_index].remove(value)
   return variables

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   assign = list(assignment)
   if check_complete(assignment,csp_table):
      return assignment
   var = select_unassigned_var(assignment,variables,csp_table)
   values = variables[var]
   for x in values:
      if isValid(x,var,assignment,variables,csp_table):
         assign[var] = str(x)
         newassignment = ''.join(assign)
         newvariables = {k:vals[:] for k, vals in variables.items()}
         newvariables = update_variables(x,var,newassignment,newvariables,csp_table)
         result = recursive_backtracking(newassignment,newvariables,csp_table)
         if result != None:
            return result
         assign[var] = '.'
   return None

def display(solution):
   # for i in range(0,81,9):
   #    line = solution[i:i+3] + " " + solution[i+4:i+7] + " " + solution[i+8:i+11] + "\n"
   #    print(line)
   puzzle = ""
   for x in range(9):
      s = solution[x*9:(x+1)*9]
      for y in range(3):
         p = s[y*3:(y+1)*3]
         for part in p:
            puzzle = puzzle+part+' '
         puzzle = puzzle+'\t'
      puzzle = puzzle + '\n'
      if x%3 == 2:
         puzzle = puzzle+'\n'
   return puzzle

def sudoku_csp():
   #rows index 0-8
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

def initial_variables(puzzle, csp_table):
   variables = {}
   for x in range(len(puzzle)):
      if puzzle[x] == '.':
         values = [1,2,3,4,5,6,7,8,9]
         for z in csp_table:
            if x in z:
               for y in range(1,10):
                  for a in z:
                     if puzzle[a] == str(y) and y in values:
                        values.remove(y)
         variables[x] = values

   return variables
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   starttime = time.time()
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   print ("Duration:", (time.time() - starttime))
   
if __name__ == '__main__': main()
