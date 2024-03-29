from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board))

ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

for turn in range(4):
  print("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  #while guess_row != int(range(0,100)):
    #guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  #while guess_col != int(range(0,100)):
    #guess_col = int(input("Guess Col: "))
#add correct input loop
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    board[guess_row - 1][guess_col - 1] = "W"
    print_board(board)
    break
  else:
    if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row - 1][guess_col - 1] == "X"):
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row - 1][guess_col - 1] = "X"
    #print "Turn", turn + 1
    print_board(board)
  if turn == 3:
    print("Game Over!")
    board[ship_row - 1][ship_col - 1] = "W"
    print_board(board)
