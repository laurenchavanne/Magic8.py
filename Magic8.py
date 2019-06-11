"""
Program: Magic8.py
Author: Lauren Chavanne
Date: 4/1/19

GUI Magic 8 ball program where the user types in a yes or no question and the program responds with a random answer.
"""

from breezypythongui import EasyFrame
from random import *
from tkinter import *

# Output list 
ResponseList = ["As I see it , yes", "Ask again later", "Better not tell you now",
               "Cannot predict now","Don't count on it","It is certain","Most likely","My sources say no","Outlook is good","Outlook not so good","Reply hazy, try again","Signs point to yes","Very doubtful","Without a doubt","Yes"]

userInput = ""
N = len(ResponseList)

""" Sets up window and widgets."""
class Magic8(EasyFrame):
  
    def __init__(self, root):
        EasyFrame.__init__(self, title = "Magic 8 Ball !")   
         
        self.initUI(root)
        
    def initUI(self, root):
        self.userString = StringVar()
        self.answerString = StringVar()
     
        self.label1 = Label(self, text = "Magic 8 Ball !", width = 24)
        self.label1.grid(row = 0, column = 1 ) # Creates first label and inner title for the window frame

        self.label2 = Label(self, text = "Question: ", width = 10)
        self.label2.grid(row = 1, column = 0, sticky = W) # Sets up second label for user to enter a question 

        self.Entry2 = Entry(self)
        self.Entry2.grid(row = 1, column = 1,columnspan = 6, sticky = W+E) # Allows for user to input a qustion 

        self.label3 = Label(self, text = "Answer: ", width = 10)
        self.label3.grid(row = 2, column = 0, sticky = W) # Sets up third label where the program generates a random answer to the user's question 
        
        self.label4 = Label(self, text ='', width = 10)
        self.label4.grid(row = 2, column = 1, columnspan = 6, sticky = W+E) # Fourth label for text to be entered 
              
        self.button1= Button(self, text = "Ask",command = self.get_answer, foreground = "White", background = "Firebrick")
        self.button1.grid(row = 3, column = 0) # Creates Ask button for user to click on as many times as they like 

        self.button1 = Button(self, text = "Clear", command = self.clear_question, foreground ="White", background = "Firebrick") # Clear button resets input field for user to type a question
        self.button1.grid(row = 3, column = 1)

        self.button1= Button(self, text = "Exit", command = root.destroy, foreground = "White", background = "Firebrick") # Exit button kills program and closes out the window 
        self.button1.grid(row = 3, column = 2)

    def get_answer(self):
        self.label4['text'] = ResponseList[randrange(0, N)] # Allows user to see the output of their question  

    def clear_question(self):
        self.Entry2.delete(0, 'end') # Allows user to enter another question after they click the clear button

    def close_window (root): 
        root.destroy() # Allows user to click the x button when they are finished with the program which then kills the program  
        
def main():
		root = Tk() # Initializes tkinter to create a widget and a window with a title bar 
		root.geometry("340x128+330+330") # Height and width for the window frame 
		app = Magic8(root) # Sets application to run 
		root.mainloop()  

if __name__ == '__main__':
    main()  

