import google.generativeai as genai
import os

class nlp_module:
    with open(os.path.abspath(r'src\google_gemini_api_key.txt'),'r') as f:
        
        gemini_api_key = f.readline().strip()
    
    def __init__(self) -> None:
        self.__model = self.__ConnectGemini__() 
        print('this is NLP Module class')
    
    def __ConnectGemini__(self, module= 'gemini-pro'):
        genai.configure(api_key=nlp_module.gemini_api_key)
        model = genai.GenerativeModel(model_name=module)
        return model
    
    def gemini_formatter(func):
        def wrapper(self, *args, **kwargs):
            model = self.__model
            prompt = func(self, *args, **kwargs)
            response = model.generate_content(prompt)
            try:
                print(response.text)
                return response.text
            except:
                return None
        return wrapper
      
    @gemini_formatter  
    def centimental_analysis(self,text=None):
        string = f'Give me centimental analysis : "{text}"'
        return string
    @gemini_formatter  
    def translator(self,text=None,converting_lang = 'english'):
        string = f'translate the text to {converting_lang} : "{text}"'
        return string
    @gemini_formatter  
    def language_detection(self,text=None):
        string = f'detecte the language : "{text}"'
        return string
    
    
    

if __name__=="__main__":
    p1 = nlp_module()
    s = 'i love you'
    p1.centimental_analysis(text=s)
    p1.language_detection(s)
    p1.translator(s,converting_lang='hindi')
    
