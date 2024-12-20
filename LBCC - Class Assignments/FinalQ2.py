#OPENING FILE AND STRIPPING AT ONCE
with open('q2_input.txt') as file:
    directions = file.read().strip()
#TESTING
#print(directions) = BOOBS... BOOBS EVERYWHERE

#CONTROLS =
up = "(" 
down = ")"

#START
floor = 0

for direction in directions:
    if direction == up:
        floor += 1 #up 1
    if direction == down:
        floor -= 1 #down 1
    #TESTING
    #print(floor) 

print(f"Part 1 Answer: {up}{floor}{down}") #Nice touch with my Up and Down variables! I must say!

print(r"""\                  \  |  /         ___________
    ____________  \ \_# /         |  ___      |       _________
   |            |  \  #/          | |   |     |      | = = = = |
   | |   |   |  |   \\#           | |`v'|     |      |         |
   |            |    \#  //       |  --- ___  |      | |  || | |
   | |   |   |  |     #_//        |     |   | |      |         |
   |            |  \\ #_/_______  |     |74 | |      | |  || | |
   | |   |   |  |   \\# /_____/ \ |      ---  |      |         |
   |            |    \# |+ ++|  | |  |^^^^^^| |      | |  || | |
   |            |    \# |+ ++|  | |  |^^^^^^| |      | |  || | |
^^^|    (^^^^^) |^^^^^#^| H  |_ |^|  | |||| | |^^^^^^|         |
   |    ( ||| ) |     # ^^^^^^    |  | |||| | |      | ||||||| |
   ^^^^^^^^^^^^^________/  /_____ |  | |||| | |      | ||||||| |""")