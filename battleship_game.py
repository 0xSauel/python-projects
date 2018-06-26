from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#Next 2 lines show where ship is hidden.
#print ship_row
#print ship_col

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row (0-4): "))
  guess_col = int(raw_input("Guess Col (0-4): "))

  if guess_row == ship_row and guess_col == ship_col:
    board[guess_row][guess_col] = "X"
    print_board(board)
    print "Congratulations! You sank my battleship!" 
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over. Ship was here!"
      board[ship_row][ship_col] = "$"
    print_board(board)
