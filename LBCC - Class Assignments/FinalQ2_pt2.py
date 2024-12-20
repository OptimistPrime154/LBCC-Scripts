#Part 2 Answer: 1795
#OPENING FILE AND STRIPPING AT ONCE
with open('q2_input.txt') as file:
    directions = file.read().strip()

#CONTROLS =
up = "(" 
down = ")"

#LEVEL LAYOUT =
floor = 0
basement = -1 #Santa needs to start at
santa_position = 1 #where Santa really starts

for direction in directions:
    if direction == up:
        floor += 1
    if direction == down:
        floor -= 1
    if floor == basement: #Santa reaches desired floor
        break
    santa_position += 1 # position for Santa to start at 

print(f"Part 2 Answer: {santa_position}")

print(r"""\       _____________,--,
      | | | | | | |/ .-.\   HANG IN THERE
      |_|_|_|_|_|_/ /   `.      SANTA
       |_|__|__|_; |      \
       |___|__|_/| |     .'`}
       |_|__|__/ | |   .'.'`\
       |__|__|/  ; ;  / /    \.-"-.
       ||__|_;   \ \  ||    /`___. \
       |_|___/\  /;.`,\\   {_'___.;{}
       |__|_/ `;`__|`-.;|  |C` e e`\
       |___`L  \__|__|__|  | `'-o-' }
       ||___|\__)___|__||__|\   ^  /`\
       |__|__|__|__|__|_{___}'.__.`\_.'}
       ||___|__|__|__|__;\_)-'`\   {_.-;
       |__|__|__|__|__|/` (`\__/     '-'
       |_|___|__|__/`      |
-jgs---|__|___|__/`         \-------------------
-.__.-.|___|___;`            |.__.-.__.-.__.-.__
  |     |     ||             |  |     |     |
-' '---' '---' \             /-' '---' '---' '--
     |     |    '.        .' |     |     |     |
'---' '---' '---' `-===-'`--' '---' '---' '---'
  |     |     |     |     |     |     |     |
-' '---' '---' '---' '---' '---' '---' '---' '--
     |     |     |     |     |     |     |     |
'---' '---' '---' '---' '---' '---' '---' '---'""")