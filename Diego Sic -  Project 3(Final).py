#Diego Sic
#This will be the project 3 of CSC 175
#This will simulate a burn of trees

import graphics 
from graphics import *
import random

HEIGHT_WINDOW = 380
WIDTH_WINDOW = 1000

class Button(graphics.Polygon):

    def __init__(self, text, height):
        absolute_point = Point(WIDTH_WINDOW*0.6, HEIGHT_WINDOW*0.4 + height)
        absolute_point1 = Point(WIDTH_WINDOW*0.6 + 300, HEIGHT_WINDOW*0.4 + height + 40)
        rec = Rectangle(absolute_point, absolute_point1)
        rec.setFill("pink")
        centerPoint = rec.getCenter()
        text = Text(centerPoint , text)
        self.text = text
        self.rectangle = rec
    
    def is_click_on(self, mouse_position):
        p1 = (self.rectangle).getP1()
        p2 = (self.rectangle).getP2()
        x_range = range(int(p1.getX()), int(p2.getX()))
        y_range = range(int(p1.getY()), int(p2.getY()))
        if mouse_position.getX() in x_range and mouse_position.getY() in y_range:
            return True
        return False

class Trees:
    images_names = ["0_tree.png", "1_little_burn.png", "2_lot_burn.png", "3_charcoal.png"]

    def __init__(self, Point) -> None:
        self.Point = Point
        self.state = 0
        self.img_name = self.images_names[self.state]
        self.img_obj = Image(Point,self.img_name)
    
    def draw(self, win):
        self.img_obj.draw(win)
    
    def undraw(self):
        self.img_obj.undraw()

    def burn_more(self, win):
        if self.state == 3:
            return
        self.state += 1
        self.state = self.state
        self.img_obj.undraw()
        self.img_name = self.images_names[self.state]
        self.img_obj = Image(self.Point,self.img_name)
        self.img_obj.draw(win)

    def is_on_fire(self):
        if self.state > 0 and self.state < 3:
            return True

    def reborn(self, win):
        self.img_obj.undraw()
        self.state = 0
        self.img_name = self.images_names[self.state]
        self.img_obj = Image(self.Point,self.img_name)
        self.img_obj.draw(win)

    def __str__(self) -> str:
        return f"{self.img}"
    
    def __repr__(self) -> str:
        return f"Trees({self.Point})"

class Forest:

    def __init__(self, width_grid, height_grid) -> None:
        height_img = 29
        width_img = 29
        forest = []
        bool_forest = []
        for i in range(height_grid):
            temp_row = []
            temp_row2 = []
            for j in range(width_grid):
                point = Point(50+(j*height_img),(50+(i*width_img)))
                temp_tree = Trees(point)
                temp_row.append(temp_tree)
                temp_row2.append(False)
            bool_forest.append(temp_row2)
            forest.append(temp_row)
        
        self.forest = forest
        self.bool_forest = bool_forest
        self.width = width_grid
        self.height = height_grid

    def forest_on_fire(self):
        fire = False
        for i in range(self.height):
            for j in range(self.width):
                if self.forest[i][j].is_on_fire():
                    fire = True
        return fire

    #This function will work only once to draw the forest 
    def drawing_forest(self, win):
        height_grid = self.height
        width_grid = self.width
        self.win =  win
        for i in range(height_grid):
            for j in range(width_grid):
                 (self.forest[i][j]).draw(win)

    #This metod will update the image of every tree
    def set_on_fire(self,win):
        for i in range(self.height):
            for j in range(self.width):
                if self.bool_forest[i][j]:
                    self.forest[i][j].burn_more(win)
                            
    def check_probabilities(self,probability):
        for i in range(self.height):
            for j in range(self.width):
                if not self.bool_forest[i][j]:
                    self.check_trees_close(i,j,probability)

    def check_trees_close(self,i,j,probability):
        for a in range(-1,2):
            for b in range(-1,2):
                if (i+a) in range(0,self.height) and (j+b) in range(0,self.width):
                    if self.bool_forest[i+a][j+b]:
                        self.bool_forest[i][j] = fire_probability(probability)
                    
    def reforest(self,win):
        bool_forest = []
        for i in range(self.height):
            temp_row = []
            for j in range(self.width):
                temp_row.append(False)
                self.forest[i][j].reborn(win)  
            bool_forest.append(temp_row)
        self.bool_forest = bool_forest 
    
def check_mouse(mouse_position):
        absolute_width = int(WIDTH_WINDOW * 0.6)
        absolute_height = int(HEIGHT_WINDOW * 0.4)
        if mouse_position.getX() in range(absolute_width, absolute_width + 300):

            if mouse_position.getY() in range(absolute_height, absolute_height + 40):
                return 1
            elif mouse_position.getY() in range(absolute_height + 40, absolute_height + 90):
                return 2
            elif mouse_position.getY() in range(absolute_height + 90, absolute_height + 140):
                return 3
        return False

def fire_probability(probability):
    return random.random() < probability

def final_label(steps,win):
    point1 = Point(WIDTH_WINDOW*0.2, HEIGHT_WINDOW*0.4)
    point2 = Point(WIDTH_WINDOW*0.8, HEIGHT_WINDOW*0.6)
    rec = Rectangle(point1, point2)
    rec.setFill("Yellow")
    centerPoint = rec.getCenter()
    text = Text(centerPoint , 
            f"The fire subsided after {steps} steps, click anywhere to continue")
    label = [rec,text]
    label[0].draw(win)
    label[1].draw(win)
    win.getMouse()
    label[0].undraw()
    label[1].undraw()
    
def error_label(win):
    point1 = Point(WIDTH_WINDOW*0.2, HEIGHT_WINDOW*0.4)
    point2 = Point(WIDTH_WINDOW*0.8, HEIGHT_WINDOW*0.6)
    rec = Rectangle(point1, point2)
    rec.setFill("Yellow")
    centerPoint = rec.getCenter()
    text = Text(centerPoint , 
            f"Invalid input, try with a new one (click anywhere to continue)")
    label = [rec,text]
    label[0].draw(win)
    label[1].draw(win)
    win.getMouse()
    label[0].undraw()
    label[1].undraw() 


def what_tree(mouse_position, forest):
    width = forest.width
    height = forest.height
    x_position = mouse_position.getX()
    y_position = mouse_position.getY()
    if (x_position in range(50, 29 * width + 29) 
        and y_position in range(50, 29 * height + 29)):
        tree_position_y = int(y_position/29) - 1
        tree_position_x = int(x_position/29) - 1
        tree_positions = [tree_position_y, tree_position_x]
        return tree_positions
    return False
                                      
def main():
    #Determining The initial dimensions
    height_grid = 10
    width_grid = 15
    win = GraphWin('Graphics', WIDTH_WINDOW , HEIGHT_WINDOW)
    #Draw the text of probability
    title = Text(Point(WIDTH_WINDOW*0.75, HEIGHT_WINDOW*0.22), "Burn Probability:")
    title.setSize(18)
    title.setStyle("bold")
    title.draw(win)
    #Draw the input box
    inputBox = Entry(Point(WIDTH_WINDOW*0.75, HEIGHT_WINDOW*0.32), 20)
    inputBox.setSize(20)
    inputBox.draw(win)
    #Draw the first buttons
    button1 = Button("Run (Random Start)", 0)
    button1.rectangle.draw(win)
    button1.text.draw(win)

    button2 = Button("Run (Click to start)",50)
    button2.rectangle.draw(win)
    button2.text.draw(win)

    button3 = Button("Reset Simulation",100)
    button3.rectangle.draw(win)
    button3.text.draw(win)

    button4 = Button("Close button",150)
    button4.rectangle.draw(win)
    button4.text.draw(win)


    #Creating the forest with the dimensions
    forest = Forest(width_grid,height_grid)
    forest.drawing_forest(win)
    mouse_position = win.getMouse()

    while not button4.is_click_on(mouse_position) :
        #This is to get the number
        what_to_do = check_mouse(mouse_position)
        while True:
            try:
                inputStr = float(inputBox.getText())
                break
            except ValueError:
                inputBox.setText("0")
                error_label(win)           
                what_to_do = False

        if what_to_do == 1:
        #This function will print the forest in every iteration
            random1 = random.randint(0,9)
            random2 = random.randint(0,14)
            (forest.forest[random1][random2]).burn_more(win)
            forest.bool_forest[random1][random2] = True
            steps = 0

            while forest.forest_on_fire():
                forest.check_probabilities(inputStr)
                forest.set_on_fire(win)
                steps += 1
            forest.set_on_fire(win)
            final_label(steps,win)


        elif what_to_do ==  2:
            while True:
                mouse_position = win.getMouse()
                tree_pos = what_tree(mouse_position, forest)
                if tree_pos != False:
                    break
            
            (forest.forest[tree_pos[0]][tree_pos[1]]).burn_more(win)
            forest.bool_forest[tree_pos[0]][tree_pos[1]] = True
            steps = 0
            while forest.forest_on_fire():
                forest.check_probabilities(inputStr)
                forest.set_on_fire(win)
                steps += 1
                
            forest.set_on_fire(win)
            final_label(steps,win)
       
        elif what_to_do == 3:
            forest.reforest(win)
        mouse_position = win.getMouse()

if __name__ == "__main__":
    main()