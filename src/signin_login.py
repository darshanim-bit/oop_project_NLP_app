
import google.generativeai as genai
import os
from src.nlp_modules import nlp_module

global database 
database = {}

class Login(nlp_module):
    def __init__(self) -> None:
        self.__database = database
        self.manu()
     
     
       
    
        
        
    def __register(self):
        
        name = input('Enter your name\n')
        
        email_id = input('Enter your email Id\n')
        if email_id.lower() in ['login']:
                self.__login()
                
        elif email_id in self.__database :
            print('This mail Id already have an account')
            print('''Try again with different mail id else want to EXIT type "EXIT"
                  1. Want to EXIT type EXIT
                  2. want to Login with the existing account type "login"''')
            self.__register()
                             
        elif email_id.lower() in ['exit'] :
            exit()
        
        password = input('Enter password')
        
        self.__database[email_id] = (name,password)
        print('Successfully registered')
        nextstep = input('\n you can procceed further By Loging In \n 1. want to login type "login"\n 2. want to exit type "Exit"')
        if nextstep.lower() in ['login'] :
            self.__login()
        else:
            exit()
        
    
    
    def __login(self):
    
        
        email_id = input('Enter your email Id\n')
        if email_id.lower() in ['register']:
                self.__register()
        elif email_id not in self.__database :
            print('This mail Id Not have an account')
            print('''Try again with different mail id else want to EXIT type "EXIT"
                  1. Want to EXIT type EXIT
                  2. want to Register with the existing account type "register"''')
            self.__login()
            
            
        elif email_id in self.__database :
            
            password = input('Enter password')
            if password != self.__database[email_id][1] :
                print('Wrong password')
                print('Try again with different password else want to EXIT type EXIT')
                self.__login()
            elif password == self.__database[email_id][1] :
                print('Login Successfull')
                nlp_module()
                return True
            elif email_id.lower() in ['exit'] :
                exit()
           
        elif email_id.lower() in ['exit'] :
            exit()
            
        return False
        
        
        
    
    
    def manu(self):
        responce = input("""
              Please Enter the Number to procceed
              
              1. Already have an account? Login
              2. New User or You don't have an Account? Create account
              3. Exit
              """)
        
        if responce == str(1):
            self.__login()
        elif responce == str(2):
            self.__register()
        else:
            exit()
        
        



if __name__ == "__main__":
    
    p1 = Login()
    
    