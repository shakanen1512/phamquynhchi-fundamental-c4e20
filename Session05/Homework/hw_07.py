map = {
    "size_x" : 6,
    "size_y" : 6
}

player = {"x": 1, "y": 1}

boxes = [
    {"x": 0, "y": 2},
    {"x": 1, "y": 2},
    {"x": 2, "y": 2},
    {"x": 3, "y": 2},
]

destinations = [
    {"x": 0, "y": 3},
    {"x": 1, "y": 4},
    {"x": 0, "y": 5},
    {"x": 3, "y": 5}
]

obstacles = [
    {"x": 1, "y": 3},
    {"x": 4, "y": 5},
]

playing = True
while playing:

#print_map
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            if y == player["y"] and x == player["x"]:
                player_is_here = True
            
            box_is_here = False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True

            destination_is_here = False
            for destination in destinations:
                if y == destination["y"] and x == destination["x"]:
                    destination_is_here = True

            obstacle_is_here = False
            for obstacle in obstacles:
                if y == obstacle["y"] and x == obstacle["x"]:
                    obstacle_is_here = True

            if player_is_here:
                print("p ", end="")
            elif box_is_here:
                print("b ", end="")
            elif destination_is_here:
                print("d ", end="")
            elif obstacle_is_here:
                print("o ", end="")
            else:
                print("- ", end="")
        print()

#check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    if win:
        print("You win")
        break

#let's get moving
    move = input("Your move: ").upper()
    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False
    
    if 0 <= (player["x"] + dx) < map["size_x"] and \
       0 <= (player["y"] + dy) < map["size_y"]:
        player["y"] += dy
        player["x"] += dx

        for box in boxes:
            if box["x"] == player["x"] and \
               box["y"] == player["y"] and \
               0 <= (box["x"] + dx) < (map["size_x"]) and \
               0 <= (box["y"] + dy) < (map["size_y"]):
                box["x"] += dx
                box["y"] += dy

#copy/ clone/ deep clone