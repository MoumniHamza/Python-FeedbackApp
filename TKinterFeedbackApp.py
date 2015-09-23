from tkinter import *
from tkinter import ttk

class GiveFeedback:
      def __init__(self , master):
          self.Frame_Header = ttk.Frame(master)
          self.My_logo = PhotoImage(file = 'python_logo.gif')
          ttk.Label(self.Frame_Header , image = self.My_logo).pack()
          ttk.Label(self.Frame_Header , text = ' Thank you for choosing python ')
          ttk.Label(self.Frame_Header , text = ' We are glad you choose python as a programming language. Using Tkinter for the Gui side is pretty awesome and fairly easy to learn. Please tell us what you think about it')
          self.Frame_content = ttk.Frame(master)
          self.Frame_content.pack()

          ttk.Label(self.Frame_content , text ='Name:')
          ttk.Label(self.Frame_content , text ='Email')
          ttk.Label(self.Frame_content , text ='Comments')




def main():
    root = Tk()
    feedback = GiveFeedback(root)
    root.mainloop()

if __name__ =="__main__":main()