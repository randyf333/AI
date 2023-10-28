# Name:
# Date:

import copy
import random
import math
from re import search



class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      allmoves = self.find_moves(board,color)
      best_move = random.choice(list(allmoves))
      return (best_move//len(board),best_move%len(board)), 0

   def stones_left(self, board):
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               count+=1
    # returns number of stones that can still be placed (empty spots)
      return count

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                  moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found
      

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
         return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                  break
            if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
    # returns best move
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      best_move = self.minimax(board,color,6)
      return (best_move//len(board),best_move%len(board)),0

   def minimax(self, board, color, search_depth):
    # returns best "value"
      best_value = self.alphabeta(board,color,search_depth,-math.inf, math.inf)
      return best_value

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
   
   # def value(self,board,color,search_depth, alpha,beta):
   #    return -self.alphabeta(board,self.opposite_color[color],search_depth-1,-alpha,-beta)

   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      best = 0
      best = self.max_value(board,color,search_depth,alpha,beta)
      # possible_moves = self.find_moves(board,color)
      # if search_depth <= 0:
      #    return self.evaluate(board,color,possible_moves)
      # for move in possible_moves:
      #    if alpha > beta:
      #       break
      #    val = self.value(board,color,search_depth,alpha,beta)
      #    if val > alpha:
      #       alpha = val
      #       best = move
      
      # best = 0
      # possible_moves = self.find_moves(board,color)
      # if search_depth <= 0:
      #    utility = self.evaluate(board,color,possible_moves)
      #    return utility
      # for moves in possible_moves:
      #    newboard = copy.deepcopy(board)
      #    flipped = self.find_flipped(newboard,moves//len(board),moves%len(board),color)
      #    alpha = -self.alphabeta(self.make_move(board,color,moves,flipped),self.opposite_color[color],search_depth-1,-alpha,-beta)
      #    if beta <= alpha:
      #       return alpha
      #    if alpha > best:
      #       board = self.make_move(board,color,moves,flipped)
      #       best = alpha
      # return best
      return best


   def max_value(self, board, color, search_depth, alpha, beta):
      possible_moves = self.find_moves(board,color)
      if search_depth <= 0:
         utility = self.evaluate(board,color,possible_moves)
         #return self.evaluate(board,color,possible_moves)
         return utility
      nextmove = -9999
      for moves in possible_moves.keys():
         newboard = copy.deepcopy(board)
         value = max(nextmove,self.min_value(self.make_move(newboard,color,moves,possible_moves[moves]),self.opposite_color[color],search_depth-1,alpha,beta))
         if value >= beta:
            return moves
         if alpha < value:
            nextmove = moves
            alpha = nextmove
      return nextmove

   def min_value(self,board,color,search_depth, alpha, beta):
      possible_moves = self.find_moves(board,color)
      if search_depth <= 0: 
         utility = self.evaluate(board,color,possible_moves)
         return utility
         #return self.evaluate(board,color,possible_moves)
      nextmove = 9999
      for moves in possible_moves.keys():
         newboard = copy.deepcopy(board)
         value = min(nextmove,self.max_value(self.make_move(newboard,color,moves,possible_moves[moves]),self.opposite_color[color],search_depth-1,alpha,beta))
         if value <= alpha:
            return moves
         if beta > value:
            beta = value
            nextmove = moves
      return nextmove


   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, board):
    # returns number of stones that can still be placed
      count = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == '.':
               count+=1
      # returns number of stones that can still be placed (empty spots)
      return count

   def make_move(self, board, color, move, flipped):
    # returns board that has been updated
      board[move//len(board)][move%len(board)] = color
      for x in flipped:
         board[x[0]][x[1]] = color
      return board

   def evaluate(self, board, color, possible_moves):
    # returns the utility value
      x = len(possible_moves)
      # return self.mobility(board,color,possible_moves) + self.tokenvalues(board,color,possible_moves)
      if x <= 3:
         return 3*self.mobility(board,color,possible_moves)+2*self.tokenvalues(board,color,possible_moves)#+4*self.corners(board,color,possible_moves)
      if x > 3 and x < 9: 
         return self.mobility(board,color,possible_moves)+3*self.tokenvalues(board,color,possible_moves)#+self.corners(board,color,possible_moves)
      if x >= 9:
         return self.mobility(board,color,possible_moves)+5*self.tokenvalues(board,color,possible_moves)#+10*self.corners(board,color,possible_moves)


   def mobility(self, board,color,possible_moves): #mobility
      omoves = self.find_moves(board,self.opposite_color[color])
      #movesum = 0
      #osum = 0
      # for moves in possible_moves.keys():
      #    movesum += self.valueboard[moves//len(board)][moves%len(board)]
      # for other in omoves.keys():
      #    osum += self.valueboard[moves//len(board)][moves%len(board)]
      # return movesum - osum
      if len(possible_moves) + len(omoves) != 0:
         return 100*(len(possible_moves)-len(omoves))/(len(possible_moves)+len(omoves))
      else:
         return 0

   def tokenvalues(self,board,color,possible_moves): #stability
      m_value = 0
      o_value = 0
      # tsum=0
      # osum=0
      valueboard = [
         [100,-3,2,2,2,2,-3,100],
         [-3,-10,-1,-1,-1,-1,-10,-3],
         [2,-1,1,0,0,1,-1,2],
         [2,-1,0,1,1,0,-1,2],
         [2,-1,0,1,1,0,-1,2],
         [2,-1,1,0,0,1,-1,2],
         [-3,-10,-1,-1,-1,-1,-10,-3],
         [100,-3,2,2,2,2,-3,100]
      ]
      # moves = len(self.find_moves(board, self.opposite_color[color]))
      # return len(possible_moves)-moves
      # omoves = self.find_moves(board,self.opposite_color[color])
      # m_value = 0
      # o_value = 0
      for a in range(len(board)):
         for b in range(len(board[a])):
            if board[a][b] == color:
               m_value += valueboard[a][b]
            if board[a][b] == self.opposite_color[color]:
               o_value += valueboard[a][b]
      # # for x in possible_moves.keys():
      # #    m_value += valueboard[x//len(board)][x%len(board)]
      # # for y in omoves.keys():
      # #    o_value += valueboard[y//len(board)][y%len(board)]
      # # return m_value-o_value
      if m_value + o_value != 0:
         return 100*(m_value-o_value)/(m_value+o_value)
      else:
         return 0
      #staticweights=[4,-3,2,2,2,2,-3,4,-3,-4,-1,-1,-1,-1,-4,-3,2,-1,1,0,0,1,-1,2,2,-1,0,1,1,0,-1,2,2,-1,0,1,1,0,-1,2,2,-1,1,0,0,1,-1,2,-3,-4,-1,-1,-1,-1,-4,-3,4,-3,2,2,2,2,-3,4]
      # b=[i for i in board if i!='.']
      # for x in range(len(b)):
      #    if b[x]==color:
      #          tsum+=staticweights[x]
      #    if b[x]==self.opposite_color[color]:
      #          osum+=staticweights[x]
      # if (tsum+osum)!=0:
      #    return 100*(tsum-osum)/(tsum+osum)
      # else:
      #    return 0

   # def corners(self,board,color,possible_moves):
   #    colorcount = 0
   #    ocount = 0
   #    corners = [[0,len(board)-1],[0,0],[len(board)-1,0],[len(board)-1,len(board[0])-1]]
   #    for x in corners:
   #       if board[x[0]][x[1]] == color:
   #          colorcount += 1
   #       elif board[x[0]][x[1]] == self.opposite_color[color]:
   #          ocount += 1
   #    if colorcount + ocount != 0:
   #       return 100*(colorcount-ocount)/(colorcount+ocount)
   #    else:
   #       return 0

   def score(self, board, color):
    # returns the score of the board 
      points = 0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == color:
               points+=1
      return points

   def find_moves(self, board, color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(board)):
         for j in range(len(board[i])):
            flipped_stones = self.find_flipped(board, i, j, color)
            if len(flipped_stones) > 0:
                  moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found

   def find_flipped(self, board, x, y, color):
    # finds which chips would be flipped given a move and color
      if board[x][y] != ".":
         return []
      if color == self.black:
         color = "@"
      else:
         color = "O"
      flipped_stones = []
      for incr in self.directions:
         temp_flip = []
         x_pos = x + incr[0]
         y_pos = y + incr[1]
         while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if board[x_pos][y_pos] == ".":
                  break
            if board[x_pos][y_pos] == color:
                  flipped_stones += temp_flip
                  break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones
   
   # def heuristic(board,turn):
   #  x=len(moves(board,turn))
   #  if x<=3:
   #      return 3*mobilityheuristic(board,turn)+2*stabilityheuristic(board,turn)
   #  if x>3 and x<9:
   #      return mobilityheuristic(board,turn)+3*stabilityheuristic(board,turn)
   #  if x>=9:
   #      return 1*mobilityheuristic(board,turn)+5*stabilityheuristic(board,turn)

   # def mobilityheuristic(board,turn):
   #    if turn=='X':
   #       oturn='O'
   #    else:
   #       oturn='X'
   #    if (len(moves(board,turn))+len(moves(board,oturn)))!=0:
   #       return 100*(len(moves(board,turn))-len(moves(board,oturn)))/(len(moves(board,turn))+len(moves(board,oturn)))
   #    else:
   #       return 0
   # def stabilityheuristic(board,turn):
   #    if turn=='X':
   #       oturn='O'
   #    else:
   #       oturn='X'
   #    tsum=0
   #    osum=0
   #    staticweights=[4,-3,2,2,2,2,-3,4,-3,-4,-1,-1,-1,-1,-4,-3,2,-1,1,0,0,1,-1,2,2,-1,0,1,1,0,-1,2,2,-1,0,1,1,0,-1,2,2,-1,1,0,0,1,-1,2,-3,-4,-1,-1,-1,-1,-4,-3,4,-3,2,2,2,2,-3,4]
   #    b=[i for i in board if i!='#']
   #    for x in range(len(b)):
   #       if b[x]=='X':
   #             tsum+=staticweights[x]
   #       if b[x]=='O':
   #             osum+=staticweights[x]
   #    if (tsum+osum)!=0:
   #       return 100*(tsum-osum)/(tsum+osum)
   #    else:
   #       return 0


