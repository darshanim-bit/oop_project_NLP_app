import google.generativeai as genai
import os

from src.signin_login import Login
import src.nlp_modules as nlp



if __name__=="__main__":
    
    log_cred =  Login()
    print(log_cred)
    