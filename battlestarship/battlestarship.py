import os

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
#This is the one I shall continue to work on.

#don't get rid of that.\/ I really need those letters.
letters = "abcdefghij"

class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10   |"""

    bottom = "_________________________________________________________"

    def __init__(self, name):
        self.fleet = []
        self.miss = []
        self.name = name
    def display(self, enemy_board=False, letter=letters):
        enemy = enemy_board
        row_headers = ["| A", "| B", "| C", "| D", "| E", "| F", "| G", "| H", "| I", "| J"]
        if enemy == False:
            print(self.top)
            index = 0
            count = 1
            for header in row_headers:
                row = header
                for column in range(0, 10):
                    ship_located_here = False
                    for ships in self.fleet:
                        if [letter[index], count] in ships.location:
                            row += "  o  "
                            ship_located_here = True
                            break
                        if [letter[index], count] in ships.hit:
                            row += "  X  "
                            ship_located_here = True
                            break
                    if [letter[index], count] in self.miss:
                        row += "  *  "
                        ship_located_here = True
                    if ship_located_here == False:
                        row += "  .  "
                    count += 1
                index += 1
                count = 1
                row += "  |"
                print(row)   
            print(self.bottom)
        else:
            print(self.top)
            index = 0
            count = 1
            for header in row_headers:
                row = header
                for column in range(0, 10):
                    something_found = False
                    for ships in self.fleet:
                        if [letter[index], count] in ships.hit:
                            row += "  X  "
                            something_found = True
                            break
                    if [letter[index], count] in self.miss:
                        row += "  *  "
                        something_found = True
                    if something_found == False:
                        row += "  .  "
                    count += 1
                index += 1
                count = 1
                row += "  |"
                print(row)
            print(self.bottom)

    def check_for_defeat(self):
        defeated = False
        dead_ships = 0
        for ship in self.fleet:
            if ship.alive == False:
                dead_ships += 1
        if dead_ships >= 5:
            defeated = True
        return defeated

    def attack(self, r, c, board_being_attacked, letters=letters):
        target_hit = False
        for ship in board_being_attacked.fleet:
            if [r, c] in ship.location:
                target_hit = True
                ship.location.remove([r, c])
                ship.hit.append([r, c])
                print("You Hit!!")
                if len(ship.location) == 0:
                    ship.alive = False
                break
        if target_hit == False:
            board_being_attacked.miss.append([r, c])
            print("You missed...")
            
            




class Ship:
    
    
    def __init__(self, size, rank = "(A)"):
        self.alive = True
        self.location = []
        self.hit = []
        self.size = size
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank
#when setting up the fleets, each player gets 5 ships. x2 fighter jets and 1 of each of the others.
#be sure to label the two fighter jets, (A) and (B)
    def assign_ship(self, letter, number, board, verticle = True, up = False, left = False, list=letters):
        board.fleet.append(self)
        size_sub = self.size - 1
        self.verticle = verticle
        starting_letter_index = letters.index(letter)
        if self.verticle == True and up == False:
            
            if starting_letter_index + size_sub > 10:
                print(starting_letter_index + size_sub)
                print("------------------Failed to assign----------------------")
                print("location invalid for {ship}: {row}{num} going down takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index += 1
        if self.verticle == True and up == True:
            if starting_letter_index- size_sub < 0:
                print(starting_letter_index- size_sub)
                print("------------------Failed to assign----------------------")
                print("location invalid for {ship}: {row}{num} going up takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                return False
            else:
                index = starting_letter_index
                for location in range(0, self.size):
                    self.location.append([letters[index], number])
                    index -= 1

        if self.verticle == False:
            if left == True:
                if int(number) - size_sub <= 0:
                    print("------------------Failed to assign----------------------")
                    print("location invalid for {ship}: {row}{num} going left takes the ship off the board.".format(ship=self.name, row=letter, num = number))
                    return False
                else:
                    num = number
                    for location in range(0, self.size):
                        self.location.append([letter, num])
                        num -= 1
            else:
                if int(number) + size_sub > 10:
                    print("------------------Failed to assign----------------------")
                    print("location invalid for {ship}: {row}{num} going right takes the ship off the board.".format(ship=self.name))
                    return False
                else:
                    num = number
                    for location in range(0, self.size):
                        self.location.append([letter, num])
                        num += 1

    def __repr__(self):
        stats = """Ship Name: {name}
         Ship Location: {location} """.format(name=self.name, location=self.location)

        return stats


section = "-----------------------------------------------------------------------------------------------------------------"


print(""" 
    ________             __       __      __ _                _______     _                ___    _             
    (    _   \           (   )__ (    )_ (_    )              (    __ \(   )_             (  _  \( )    _       
    |  (__)   ) _ _ _____|    __)       _)|   |     ____       |  (__(_)    _)  _ _ _ __  | (__(_) |__ (_) __ __  
    |    _  (  /   __    )   |   |    |   |   |   /  ____ \     \__  \ |   |  / _  )  __)  \___ \|  _  \ |   __  \ 
    |  (__)  )|   (__|  |    |__ |    |__ |   |__(  ______/   ( )__)  ||   |_( (_| | |    ( )__) | | | | |  (__)  )
    (_______/  \__ ______)\_____)\_______)_______)\_______)    \______)\__  _)\__ _)_)     \_____)_) (_)_)     __/ 
                                                                                                        |  |    
                                                                                                        (___)
    -----------------------------------------------------------------------------------------------------------------""")
print("Welcome to the squad commander. This is a two player game where one person has access to this screen and passes to the other player when prompted.")
print("Let's get started!")
print(section)

p1_name = input("Player One, what is your name? ex. Lauren          ")
p1_board = Board(p1_name)
p2_name = input("Player Two, what is your name? ex. Mark            ")
p2_board = Board(p2_name)
print("""
                ----Players set----
            phase one: player identification
                        COMPLETE
        
        
        Begin phase two: fleet assignments""")
swap = input("""{p1} prepare to assign your ships. {p2} do not look.
                press enter when ready""".format(p1=p1_name, p2=p2_name))
clear()    


p1_scout = Ship(2)
p1_fighter_a = Ship(3)
p1_fighter_b = Ship(3, "(B)")
p1_cargo = Ship(4)
p1_mother = Ship(5)
p1_ships = [p1_scout, p1_fighter_a, p1_fighter_b, p1_cargo, p1_mother]

p2_scout = Ship(2)
p2_fighter_a = Ship(3)
p2_fighter_b = Ship(3, "(B)")
p2_cargo = Ship(4)
p2_mother = Ship(5)
p2_ships = [p2_scout, p2_fighter_a, p2_fighter_b, p2_cargo, p2_mother]

#Here are two fake players so that I can skip the assignment stage when testing the fighting stage.
t1_board = Board("Tester 1")
t1_scout = Ship(2)
t1_scout.assign_ship("a", 1, t1_board, False, False, False)
t1_fighter_a = Ship(3)
t1_fighter_a.assign_ship("b", 1, t1_board, False, False, False)
t1_fighter_b = Ship(3, "(B)")
t1_fighter_b.assign_ship("c", 1, t1_board, False, False, False) 
t1_cargo = Ship(4)
t1_cargo.assign_ship("d", 1, t1_board, False, False, False)
t1_mother = Ship(5)
t1_mother.assign_ship("e", 1, t1_board, False, False, False)

t2_board = Board("Tester 2")
t2_scout = Ship(2)
t2_scout.assign_ship("a", 1, t2_board, False, False, False)
t2_fighter_a = Ship(3)
t2_fighter_a.assign_ship("b", 1, t2_board, False, False, False)
t2_fighter_b = Ship(3, "(B)")
t2_fighter_b.assign_ship("c", 1, t2_board, False, False, False) 
t2_cargo = Ship(4)
t2_cargo.assign_ship("d", 1, t2_board, False, False, False)
t2_mother = Ship(5)
t2_mother.assign_ship("e", 1, t2_board, False, False, False)

def ship_assignments(player, ships_list):
    for ship in ships_list:
        placed_ship = False
        while placed_ship == False:
            print("""                   ---{p}---
            Assign the {type} which takes up {size} spaces on the map.
                """.format(p=player.name, type=ship.name, size=ship.size))
            player.display()
            row = input("choose a starting point. choose a row (the letter must be lower case. ex. b )     ")
            column = int(input("now a column.     "))
            v_q = input("Will the ship be verticle? yes or no.      ")
            verticle = True
            up = False
            left = False
            if v_q == "yes" or v_q == "Yes" or v_q == "y":
                verticle = True
            if v_q == "no" or v_q == "No" or v_q == "n":
                verticle = False
            
            if verticle == True:
                up_q = input("Do you want the ship going up from the starting point or down?     ")
                if up_q == "up":
                    up = True
                if up_q == "down" or up_q == "d":
                    up = False
            else:
                left_q = input("Do you want the ship going left or right from the starting point?    ")
                if left_q == "left" or left_q == "l":
                    left = True
                if left_q == "right" or left_q == "r":
                    left = False
            if ship.assign_ship(row, column, player, verticle, up, left) != False:
                placed_ship = True 
            
        player.display()
        pause = input("press enter to continue")
    clear()
    


ship_assignments(p1_board, p1_ships)
print("Fleet as been deployed!")
pause = input("Pass the controls to {p} and press enter to continue".format(p=p2_board.name))
ship_assignments(p2_board, p2_ships)
print("Fleet as been deployed!")
print("Both Fleets are ready for battle! Pass controls over to {p1} to start us off.".format(p1= p1_board.name))
pause= input("press enter to continue")
clear()

def user_attack(player_board, enemy_board):
    print("------------{p}-------------".format(p=player_board.name))
    print("Your Fleet")
    player_board.display()
    engage = input("Press enter to activate targetting system")
    clear()
    print("------------{p}-------------".format(p=player_board.name))
    print("targetting system active. Select Location.")
    enemy_board.display(True)
    row = str(input("Select a row. ex. d            "))
    column = int(input("Selct a column. ex 8            "))
    clear()
    player_board.attack(row, column, enemy_board)
    enemy_board.display(True)

def changeplayers(pl_board, en_board):
    print("it is now {p}'s turn.".format(p=en_board.name))
    passed = input("Pass controls to them and hit enter when ready.")
    clear()

# t2_mother.alive = False
# t2_fighter_a.alive = False
# t2_fighter_b.alive = False
# t2_cargo.alive = False
# #t2_scout.alive = False
# run_game = True
# while run_game == True:
#     user_attack(t1_board, t2_board)
#     print(t2_board.check_for_defeat())
#     if t2_board.check_for_defeat() is True:
#         print("{p1} has won!! All of {p2}'s ships have been destroyed.".format(p1=t1_board.name, p2=t2_board.name))
#         run_game = False
#         break
    
#     changeplayers(t1_board, t2_board)
#     user_attack(t2_board, t1_board)
#     print(t1_board.check_for_defeat())
#     if t1_board.check_for_defeat() is True:
#         print("{p1} has won!! All of {p2}'s ships have been destroyed.".format(p2=t1_board.name, p1=t2_board.name))
#         run_game = False
#         break
#     changeplayers(t2_board, t1_board)



run_game = True
while run_game == True:
    user_attack(p1_board, p2_board)
    #print(p2_board.check_for_defeat())
    if p2_board.check_for_defeat() is True:
        print("{p1} has won!! All of {p2}'s ships have been destroyed.".format(p1=p1_board.name, p2=p2_board.name))
        run_game = False
        break
    
    changeplayers(p1_board, p2_board)
    user_attack(p2_board, p1_board)
    #print(p1_board.check_for_defeat())
    if p1_board.check_for_defeat() is True:
        print("{p1} has won!! All of {p2}'s ships have been destroyed.".format(p2=p1_board.name, p1=p2_board.name))
        run_game = False
        break
    changeplayers(p2_board, p1_board)