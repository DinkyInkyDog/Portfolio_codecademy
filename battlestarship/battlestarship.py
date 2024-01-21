

#don't get rid of that.\/ I really need those letters.
letters = "abcdefghi"
#there will be two boards. One for the player and one for the enemy that print seperate and hold their own info
class Board:
    top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    bottom = "_________________________________________________________"
    user_rows = [row_a, row_b, row_c, row_d, row_e, row_f, row_g, row_h, row_i]
    #I need a seperate board for each of the different versions that will happen.
    #so this next one will be the enemy board view
    e_top = """_________________________________________________________
|    1    2    3    4    5    6    7    8    9    10    |"""
    e_row_a = [ "| A", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_b = [ "| B", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_c = [ "| C", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_d = [ "| D", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_e = [ "| E", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_f = [ "| F", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_g = [ "| G", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_h = [ "| H", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_row_i = [ "| I", "  .  ", "  .  ", "  .  ","  .  ", "  .  ", "  .  ", "  .  ", "  .  ","  .  ", "   .  ", "  |"]
    e_bottom = "_________________________________________________________"
    enemy_rows = [e_row_a, e_row_b, e_row_c, e_row_d, e_row_e, e_row_f, e_row_g, e_row_h, e_row_i]
    def __init__(self, enemy = False):
        self.fleet = {}
        self.enemy = enemy

    def display(self):
        if self.enemy == False:
            print(self.top)
            for row in self.user_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.bottom)
        #tested and it work!! ^ 
        #for now I have the enemy one displaying the same but that won't be the case moving forward.
        if self.enemy == True:
            print(self.e_top)
            for row in self.enemy_rows:
                full = ''
                for part in row:
                    full += str(part)
                print(full)
            print(self.e_bottom) 

    def mark_board(self, ship, list=letters):
        if ship.verticle == True:
            self.fleet[ship.name] = [str(ship.location.items())]
            index = 0
            row_letter = " "
            
            for letter in letters:
                if letters[index] in ship.location.keys():
                    row_letter = letters[index]
                    break
                else:
                    index += 1
            
            numbers_list = [value for sublist in ship.location.values() for value in sublist]
            
            if self.enemy == False:
                i = letters.find(row_letter)
                row = self.user_rows[i]
                index_3 = 0
                for number in range(0, len(numbers_list)):
                    row.pop(numbers_list[index_3])
                    row.insert(numbers_list[index_3], "  o  ")
                    print(row)
                    index_3 += 1
                print(self.user_rows[i])
            self.display()
                
                
        else:
            self.fleet[ship.name] = [str(ship.location.items())]
            index = 0
            row_letters = []
            for letter in letters:
                if letters[index] in ship.location.keys():
                    row_letters.append(letters[index])
                    index += 1
                else:
                    index += 1
            column_number = 0
            for num in ship.location.values():
                    column_number = num
           
            if self.enemy == False:
                index_2 = 0
                for row in range(0, len(row_letters)):
                    i = letters.find(row_letters[index_2])
                    row = self.user_rows[i]
                    row.pop(column_number)
                    row.insert(column_number, "  o  ")
                    index_2 += 1
            self.display()

    #         


       
       
player = Board()
enemy = Board(enemy=True)

def find_index(letter, list=letters):
    index = list.index(letter)
    return index

class Ship:
    verticle = True
    location = {}
    def __init__(self, size, rank = "(A)", status=True):
        self.size = size
        #The initialized ship is friendly by default, so when making the enemy ships change to false.
        self.friendly = status
        ship_names = ["0", "1", "Scout", "Fighter Jet", "Cargo Ship", "Mothership"]
        self.name = ship_names[size] + rank
    def flip(self):
        if self.verticle == True:
            self.verticle = False
        else:
            self.verticle = True

    def assign_ship(self, letter, number, list=letters):
        if self.verticle == True:
            add = 0
            for mark in range(0, self.size):
                if letter not in self.location:
                    self.location[letter] = [number]
                    add += 1
                    continue
                self.location[letter].append(number + add)
                add += 1
        else:
            index = find_index(letter)
            for mark in range(0, self.size):
                self.location[letters[index]] = number
                index += 1

#player.display()
#enemy.display()

testship_1 = Ship(3)
#testship_1.flip()

testship_1.assign_ship("a", 4)



player.mark_board(testship_1)