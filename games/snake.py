import sys
import time
import random
import keyboard
sys.path.append('../') 
from resoprint import Screen
from resoprint import Model
from resoprint import Object

# Defining important variables
start_length = 3
rows = 20
columns = 40
columns = 40
coordinate_x = int(columns/2)
coordinate_y = int(rows/2)
coordinates = []
snake_symbol = "●"
apple_symbol = "●"
direction = "right"
apple_coordinate_x = 0
apple_coordinate_y = 0
apple_type = "red"
points = 20
delete_last = 0
death_check = False


# Making default snake
for i in range(start_length):
    coordinates.append([coordinate_y, coordinate_x+i])
coordinate_x += start_length-1

# Function for generating apple in random places
def generate_apple():
    global apple_coordinate_x 
    global apple_coordinate_y
    apple_coordinate_y = random.randint(2,rows-2)
    apple_coordinate_x = random.randint(3,columns-3)
    if [apple_coordinate_y, apple_coordinate_x] in coordinates:
        generate_apple()

# Function for adding apple to screen
def update_apple():
    global apple_coordinate_x 
    global apple_coordinate_y
    global apple_type
    screen.changeSymbol(apple_coordinate_y, apple_coordinate_x,apple_symbol, apple_type)

# Function for checking if snake died or not
def check_death():
    global death_check
    if coordinate_x <= 2:
        death_check = True
    elif coordinate_x >= columns-1:
        death_check = True
    elif coordinate_y <= 1:
        death_check = True
    elif coordinate_y >= rows:
        death_check = True

# Function for moving snake by direction
def move_direction(direction):
    global coordinate_x
    global coordinate_y
    global delete_last
    global death_check
    if direction == "right":
        coordinate_x += 1
    elif direction == "left" :
        coordinate_x -= 1
    if direction == "up":
        coordinate_y -= 1
    if direction == "down":
        coordinate_y += 1
    
    if delete_last == 0:
        coordinates.pop(0)    
    else:
        delete_last -= 1
    
   
    if [coordinate_y, coordinate_x] in coordinates:
        death_check = True

    coordinates.append([coordinate_y,  coordinate_x])

def check_apple_touch():
    global points
    global delete_last
    global apple_type
    if coordinate_y == apple_coordinate_y and coordinate_x == apple_coordinate_x:
        points += 1
        a = random.randint(1,10)
        generate_apple()
        apple_type = "red"
        delete_last = 1

# Defining screen object
screen = Screen(rows=rows, columns=columns, main_symbol=" ", main_color="cyan")

generate_apple()
update_apple()

while True:
    if keyboard.is_pressed('w') or keyboard.is_pressed('up') and direction != "down":
            direction = "up"
    elif keyboard.is_pressed('s') or keyboard.is_pressed('down') and direction != "up":
            direction = "down"
    elif keyboard.is_pressed('a') or keyboard.is_pressed('left') and direction != "right":
            direction = "left"
    elif keyboard.is_pressed('d') or keyboard.is_pressed('right') and direction != "left":
            direction = "right"
    move_direction(direction)
    if check_apple_touch():
        sf
    check_death()
    if (death_check):
        break
    screen.resetScreen()
    screen.changeBorder(border_left = 2, border_right = 2, border_top = 1, border_bottom = 1, symbol = "█", color = "")
    screen.changeSymbols(coordinates, snake_symbol)
    screen.changeSymbolsColors(coordinates, "green")
    update_apple()
    screen.update()
    print(delete_last)
    time.sleep(0.1)
