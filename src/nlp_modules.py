import google.generativeai as genai
import os
import time
class NLPModels:
    with open(r'D:\git_Repositories\oop_project_NLP_app\src\google_gemini_api_key.txt','r') as f:
        
        gemini_api_key = f.readline().strip()
    
    def __init__(self) -> None:
        
        print('this is NLP Module class')
      
    def __Connect_gemini(self,module= 'gemini-pro'):
            genai.configure(api_key=NLPModels.gemini_api_key)
            model = genai.GenerativeModel(model_name=module)
            return model
    
    def centimental_analysis(self):
        text = input('Enter text to centimental analysis\n')
        string = f'Give me centimental analysis : "{text}"'
        model = self.__Connect_gemini()
        responce =  model.generate_content(string,)
        time.sleep(5)
        try:
            return responce.text
        except:
            return None
        
     
    def translator(self):
        text = input('Enter text to translate\n')
        converting_lang = input('\nEnter language name to convert\n')
        string = f'translate the text to {converting_lang} : "{text}"'
        model = self.__Connect_gemini()
        responce = model.generate_content(string)
        try:
            return responce.text
        except:
            return None
 
    def language_detection(self):
        text = input('Enter text to detecte the language\n')
        string = f'detecte the language : "{text}"'
        model = self.__Connect_gemini()
        responce = model.generate_content(string)
        try:
            return responce.text
        except:
            return None
    
    
    

if __name__=="__main__":
    p1 = NLPModels()
    s = 'i love you'
    res = p1.centimental_analysis()
    print(res)
    res1 = p1.language_detection()
    print(res1)
    res2 = p1.translator()
    print(res2)
    
