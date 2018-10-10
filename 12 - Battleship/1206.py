#%%
letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)

#%%
board = []

for i in range(0, 5):
  board.append(["O"] * 5)
  
def print_board(board_in):
  for row in board_in:
  	print " ".join(row)
    
print_board(board)
