# Name:
# Date:
import random
import copy


class RandomPlayer:
   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # Terminal test: when there's no more possible move
      #                return (-1, -1), 0
      # returns best move
      # (column num, row num), 0
      posmoves = self.find_moves(board,color)
      if len(posmoves) == 0:
         return (-1,-1), 0
      move = random.choice(list(posmoves))
      return (move//len(board),move%len(board[0])), 0
      
     
   def find_moves(self, board, color):
      # finds all possible moves
      # returns a set, e.g., {0, 1, 2, 3, ...., 24} 
      # 0 5 10 15 20
      # 1 6 11 16 21
      # 2 7 12 17 22
      # 3 8 13 18 23
      # 4 9 14 19 24
      # if 2 has 'X', board = [['.', '.', 'X', '.', '.'], [col 2], .... ]
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
               if self.first_turn and board[i][j] == '.': 
                  moves_found.add(i*self.y_max+j)
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                  for incr in self.directions:
                     x_pos = i + incr[0]
                     y_pos = j + incr[1]
                     stop = False
                     while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              moves_found.add(x_pos*self.y_max+y_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
      self.first_turn = False
      return moves_found

class CustomPlayer:

   def __init__(self):
      self.white = "#ffffff" #"O"
      self.black = "#000000" #"X"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 5
      self.y_max = 5
      self.first_turn = True
      self.colors = {self.white:'O', self.black:'X'}

   def best_strategy(self, board, color):
      # returns best move
      best_move, utility = self.minimax(board,color,2)
      return best_move, 0

   def minimax(self, board, color, search_depth):
      # search_depth: start from 2
      # returns best "value"

      # possible_moves = self.find_moves(board,color)
      # if len(possible_moves) == 0: return self.evaluate(board,color,possible_moves)
      # value = -99999
      # for move in possible_moves:
      #    best_move, val = self.minimax(board,self.opposite_color,search_depth+1)
      best_move = self.max_value(board,color,search_depth)
      return (best_move//len(board),best_move%len(board[0])), 1 

   def max_value(self, board, color, search_depth):
      possible_moves = self.find_moves(board,color)
      if search_depth <= 0:
         utility = self.evaluate(board,color,possible_moves)
         #return self.evaluate(board,color,possible_moves)
         return utility
      max_v = -9999
      nextmove = 0
      for moves in possible_moves:
         newboard = copy.deepcopy(board)
         value = self.min_value(self.make_move(newboard,color,moves),self.opposite_color[color],search_depth-1)
         if value > max_v:
            max_v = value
            nextmove = moves
      return nextmove

   def min_value(self,board,color,search_depth):
      possible_moves = self.find_moves(board,color)
      if search_depth <= 0: 
         utility = self.evaluate(board,color,possible_moves)
         return utility
         #return self.evaluate(board,color,possible_moves)
      min_v = 9999
      nextmove = 0
      for moves in possible_moves:
         newboard = copy.deepcopy(board)
         value = self.max_value(self.make_move(newboard,color,moves),self.opposite_color[color],search_depth-1)
         if value < min_v:
            min_v = value
            nextmove = moves
      return nextmove

   def negamax(self, board, color, search_depth):
      # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
      # returns best "value" while also pruning
      pass

   def make_move(self, board, color, move):
      # returns board that has been updated
      board[move//len(board)][move%len(board[0])] = self.colors[color]
      return board

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      # count possible_moves (len(possible_moves)) of my turn at current board
      # opponent's possible_moves: self.find_moves(board, self.opposite_color(color))
      omoves = len(self.find_moves(board, self.opposite_color[color]))
      return len(possible_moves) - omoves

   def find_moves(self, board, color):
      # finds all possible moves
      y_max = len(board)
      x_max = len(board[0])
      moves_found = set()
      for i in range(len(board)):
         for j in range(len(board[i])):
               if self.first_turn and board[i][j] == '.': 
                  moves_found.add(i*y_max+j)
               elif (color == self.black and board[i][j] == 'X') or (color == self.white and board[i][j] == 'O'):
                  for incr in self.directions:
                     x_pos = i + incr[0]
                     y_pos = j + incr[1]
                     stop = False
                     while 0 <= x_pos < x_max and 0 <= y_pos < y_max:
                           if board[x_pos][y_pos] != '.':
                              stop = True
                           if not stop:    
                              moves_found.add(x_pos*y_max+y_pos)
                           x_pos += incr[0]
                           y_pos += incr[1]
      self.first_turn = False
      return moves_found
      
      

