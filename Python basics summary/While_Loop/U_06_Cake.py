x = int(input())
y = int(input())
total_number_pieces = x * y
pieces_taken = 0
while True:
    pieces = input()
    if pieces != "STOP":
        pieces = int(pieces)
        pieces_taken += pieces
        if pieces_taken > total_number_pieces:
            print(f"No more cake left! You need {pieces_taken - total_number_pieces} pieces more.")
            break
    else:
        print(f"{total_number_pieces - pieces_taken} pieces are left.")
        break
