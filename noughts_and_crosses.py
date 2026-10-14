
# spaces are empty
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def print_board(board):
    i = 0
    for row in board:               
        print(row[0] + '|' + row[1] + '|' + row[2])
        if i < 2:
            print( "-|-|-")
        i += 1 

def valid_move(x : int, y : int):
  return board[y][x] == ' '

def set_piece(piece : str, x : int, y : int):
  board[y][x] = piece

def get_input_player(player : str):
  while True:
    x = int(input(f"Player {player} Enter Column: "))
    y = int(input(f"Player {player} Enter Row: "))
    if valid_move(x, y):
      return x, y
    else:
      print("The move was invalid! Please retry")

def check_row(piece : str, board):
  if board[0][0] == board[0][1] == board[0][2] == piece:
    return True
  elif board[1][0] == board[1][1] == board[1][2] == piece:
    return True
  elif board[2][0] == board[2][1] == board[2][2] == piece:
    return True
  return False

def check_column(piece : str, board):
  if board[0][0] == board[1][0] == board[2][0] == piece:
    return True
  elif board[0][1] == board[1][1] == board[2][1] == piece:
    return True
  elif board[0][2] == board[1][2] == board[2][2] == piece:
    return True
  return False

def check_diagnal(piece : str, board):
  if board[0][0] == board[1][1] == board[2][2] == piece:
    return True
  elif board[0][2] == board[1][1] == board[2][0] == piece:
    return True  
  return False

def check_who_won(piece : str, board):
  return check_column(piece,board) or check_row(piece,board) or check_diagnal(piece,board)

def is_board_full(board):
  for part in board:
    for letter in part:
      if letter == ' ':
        return False
  return True

def check_logic(board):
    if check_who_won('x', board):
        print( f"x won!" )
        return True
    elif check_who_won('o', board):
        print( f"o won!")
        return True
    elif is_board_full(board):
        print( f"nobody won")
        return True
    return False

while not check_who_won('x', board) and not check_who_won('o', board):
    x, y = get_input_player("One")
    set_piece( 'x', x, y)
    print_board(board)
    if check_logic(board):
      break
    x, y = get_input_player("Two")  
    set_piece( 'o', x, y)
    print_board(board)
    if check_logic(board):
      break
    

