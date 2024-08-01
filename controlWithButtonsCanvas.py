from tkinter import *
def next_turn():
    global x1, y1, x2, y2,rectangle,direction,canvas
    if direction == 'left':
        x1, x2 = x1-10, x2-10 
    elif direction == 'right':
        x1, x2 = x1+10, x2+10 
    elif direction == 'up':
        y1, y2 = y1-10, y2-10
    elif direction == 'down':
        y1,y2 = y1+10, y2+10
    canvas.delete(rectangle)
    rectangle = canvas.create_rectangle(x1,y1,x2,y2, fill="red")
    canvas.after(100,next_turn)
def change_direction(new_direction):
    global direction
    direction = new_direction
    
window = Tk()
direction = 'down'
x1,y1 = 0,0
x2, y2 = x1+30, y1+30
canvas = Canvas(window)
canvas.pack()
rectangle = canvas.create_rectangle(x1,y1,x2,y2,fill="red", tag="rectangle")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

next_turn()
window.mainloop()