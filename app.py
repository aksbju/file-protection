from cryptography.fernet import Fernet
import sys
import easygui

class fileprotection():
    def __init__(self, target, key):
        self.target = target.replace('\\','/')
        self.path = '/'.join(self.target.split('/')[0:-1])
        self.input_filename = self.target.split('/')[-1]
        self.output_filename = '.'.join((self.target.split('/')[-1]).split('.')[0:-1])+'_output.'+(self.target.split('/')[-1]).split('.')[-1]
        self.key = key.encode() # string keys to byte keys

    def protect(self):
        fernet = Fernet(self.key)
        return fernet.encrypt(self.import())

    def unprotect(self):
        fernet = Fernet(self.key)
        return fernet.decrypt(self.import())

    def import(self):
        with open(self.input_filename, 'r+b') as file:
            return file.read()

    def export(self):
        with open(self.output_filename, 'w+b') as file:
            file.write()
