from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class GiveFeedback:
      def __init__(self , master):
          master.title('Pyton feedback ')
          master.configure(background = '#e1d8b9')
          master.resizable(False,False)
          self.style = ttk.Style()
          self.style.configure('TFrame' , background = '#e1d8b9')
          self.style.configure('TButton', background = '#e1d8b9')
          self.style.configure('TLabel' , background = '#e1d8b9', font=('Arial',11))
          self.style.configure('Header.TLabel' , background = '#e1d8b9', font=('Arial',18,'bold'))

          self.Frame_Header = ttk.Frame(master)
          self.Frame_Header.pack()
          self.My_logo = PhotoImage(file = 'python_logo.gif').subsample(2,2)
          ttk.Label(self.Frame_Header , image = self.My_logo).grid(row = 0, column =0 , rowspan = 2)
          ttk.Label(self.Frame_Header , text = ' Thank you for choosing python ', style = 'Header.TLabel').grid(row = 0 , column = 1)
          ttk.Label(self.Frame_Header , wraplength = 300 , text = ' We are glad you choose python as a programming language. Using Tkinter for the Gui side is pretty awesome and fairly easy to learn. Please tell us what you think about it').grid(row =1 , column =1)
          self.Frame_content = ttk.Frame(master)
          self.Frame_content.pack()

          ttk.Label(self.Frame_content , text ='Name:').grid(row =0 ,column =0, padx=5, sticky = 'sw')
          ttk.Label(self.Frame_content , text ='Email').grid(row =0 , column =1, padx=5, sticky = 'sw')
          ttk.Label(self.Frame_content , text ='Comments').grid(row =2 , column=0, padx=5, sticky = 'sw')

          self.Entry_name = ttk.Entry(self.Frame_content , width = 24, font=('Arial',11))
          self.Entry_mail = ttk.Entry(self.Frame_content , width = 24,font=('Arial',11))
          self.Entry_comments =Text(self.Frame_content , width = 50 ,height = 10,font=('Arial',12))
          self.Entry_name.grid(row =1, column =0)
          self.Entry_mail.grid(row = 1 , column =1)
          self.Entry_comments.grid(row = 3 , column = 0 , columnspan =2, padx = 5)
         
          ttk.Button(self.Frame_content , text = 'Submit',command = self.submit).grid(row = 4,column =0, padx=5, sticky = 'e')
          ttk.Button(self.Frame_content , text = 'Clear', command = self.clear).grid(row = 4, column =1, padx=5, sticky = 'w')

      def submit(self):
            print('Name: {}'.format(self.Entry_name.get()))
            print('Email: {}'.format(self.Entry_mail.get()))
            print('Comments: {}'.format(self.Entry_comments.get(1.0,'end')))
            self.clear()
            messagebox.showinfo(title = ' Learning Python feedback' ,message=' Message Submitted')
      def clear(self):
            self.Entry_name.delete(0,'end')
            self.Entry_mail.delete(0,'end')
            self.Entry_comments.delete(1.0, 'end')
def main():
    root = Tk()
    feedback = GiveFeedback(root)
    root.mainloop()

if __name__ =="__main__":main()
