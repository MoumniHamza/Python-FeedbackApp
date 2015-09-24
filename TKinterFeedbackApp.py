from tkinter import *
from tkinter import ttk

class GiveFeedback:
      def __init__(self , master):
          self.Frame_Header = ttk.Frame(master)
          self.Frame_Header.pack()
          self.My_logo = PhotoImage(file = 'python_logo.gif').subsample(3,3)
          ttk.Label(self.Frame_Header , image = self.My_logo).grid(row = 0, column =0 , rowspan = 2)
          ttk.Label(self.Frame_Header , text = ' Thank you for choosing python ').grid(row = 0 , column = 1)
          ttk.Label(self.Frame_Header , wraplength = 300 , text = ' We are glad you choose python as a programming language. Using Tkinter for the Gui side is pretty awesome and fairly easy to learn. Please tell us what you think about it').grid(row =1 , column =1)
          self.Frame_content = ttk.Frame(master)
          self.Frame_content.pack()

          ttk.Label(self.Frame_content , text ='Name:').grid(row =0 ,column =0, padx=5, sticky = 'sw')
          ttk.Label(self.Frame_content , text ='Email').grid(row =0 , column =1, padx=5, sticky = 'sw')
          ttk.Label(self.Frame_content , text ='Comments').grid(row =2 , column=0, padx=5, sticky = 'sw')

          self.Entry_name = ttk.Entry(self.Frame_content , width = 24)
          self.Entry_mail = ttk.Entry(self.Frame_content , width = 24)
          self.Entry_comments =Text(self.Frame_content , width = 50 ,height = 10)
          self.Entry_name.grid(row =1, column =0)
          self.Entry_mail.grid(row = 1 , column =1)
          self.Entry_comments.grid(row = 3 , column = 0 , columnspan =2, padx = 5)
         
          ttk.Button(self.Frame_content , text = 'Submit').grid(row = 4,column =0, padx=5, sticky = 'e')
          ttk.Button(self.Frame_content , text = 'Clear').grid(row = 4, column =1, padx=5, sticky = 'w')


def main():
    root = Tk()
    feedback = GiveFeedback(root)
    root.mainloop()

if __name__ =="__main__":main()