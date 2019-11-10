from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
import sys, os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

class fileprotection():
    def __init__(self): # initialization
        self.root = Tk()
        self.root.withdraw()

    def init_target(self):
        self.target = self.tf1.get().replace('\\','/')
        self.path = '/'.join(self.target.split('/')[0:-1])
        self.input_filename = self.target.split('/')[-1]
        self.output_filename = '.'.join((self.target.split('/')[-1]).split('.')[0:-1])+'_output.'+(self.target.split('/')[-1]).split('.')[-1]
        self.key = self.generate_key(self.tf2.get().encode())

    def generate_key(self, password):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password)
        return base64.urlsafe_b64encode(digest.finalize())

    def protect(self):
        try:
            self.init_target()
            fernet = Fernet(self.key)
            temp = fernet.encrypt(self.read_from_file())
            self.write_to_file(temp)
            messagebox.showinfo('Notice','Done')
        except:
            messagebox.showerror('Notice','Failed')

    def unprotect(self):
        try:
            self.init_target()
            fernet = Fernet(self.key)
            temp = fernet.decrypt(self.read_from_file())
            self.write_to_file(temp)
            messagebox.showinfo('Notice','Done')
        except:
            messagebox.showerror('Notice','Failed')

    def read_from_file(self):
        with open(self.path+'/'+self.input_filename, 'r+b') as file:
            return file.read()

    def write_to_file(self, filedata):
        with open(self.path+'/'+self.output_filename, 'w+b') as file:
            file.write(filedata)

    def open_file(self):
        self.target = askopenfilename(initialdir=os.getcwd(),title = "Choose a file.")
        self.tf1.delete(0,END)
        self.tf1.insert(0,self.target)

    def show_main_window(self):
        self.window = Toplevel()
        self.window.geometry('400x150')
        self.window.title('project - file-protection')
        self.window.configure(background='#ababab')
        self.lbl1 = Label(self.window, text='File', background='#ababab')
        self.lbl1.place(height=20, width=80, x=40, y=20)
        self.tf1 = Entry(self.window)
        self.tf1.place(height=20, width=180, x=110,y=20)
        self.btn1 = Button(self.window, text = 'select', command=lambda: self.open_file())
        self.btn1.place(height=20, width=50, x=290, y=20)
        self.lbl2 = Label(self.window, text='Password', background='#ababab')
        self.lbl2.place(height=20, width=80, x=40, y=50)
        self.tf2 = Entry(self.window)
        self.tf2.place(height=20, width=230, x=110,y=50)
        self.btn2 = Button(self.window, text = 'Protect', command=lambda: self.protect())
        self.btn2.place(height=30, width=80, x=50, y=100)
        self.btn3 = Button(self.window, text = 'Unrotect', command=lambda: self.unprotect())
        self.btn3.place(height=30, width=80, x=260, y=100)
        self.window.mainloop()

if '__main__' == __name__:
    fp = fileprotection()
    fp.show_main_window()
