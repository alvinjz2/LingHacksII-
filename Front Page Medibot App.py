from tkinter import Tk, Label, Button, StringVar, Text
from tkinter import *
import speech_recognition as sr
import os
import time
from MBot import Medibot

sr.__version__
r = sr.Recognizer()

x = '2'

class FrontEnd:
    LABEL_TEXT = ["MedicBot v1.0."]
    bot = Medibot()
   
    
    

    def __init__(self, master):
        self.master = master
        master.title("MedicBot")
        canvas = Canvas(width=40, height=15, bg = "red")
        canvas.pack(expand=YES, fill=BOTH)      
        quote = "**Please check the diagnosis with a verified doctor**" 
        text = Text(master, width = 40, height = 4.5)
        text.insert('1.0', '            MedicBot v1.0. \n    **Please Check the Diagnoses \n    with a Verified Doctor**')
        text.pack()
        """
        self.greet_button = Button(master, text="Start Diagnosing", command=self.Listen)
        self.greet_button.pack()
        """
        self.greet_button = Button(master, text="Start", command=self.start)
        self.greet_button.pack()
        self.greet_button = Button(master, text="Help", command=self.Help)  
        self.greet_button.pack()
        
    """  
    def Response(self):
        print("Make sure the file is in \"database\" folder!")
        os.system("say 'Welcome to Audio to Text feature, make sure the format of the file is in .wav'") 
        time.sleep(1)
        os.system("say 'what is the name of the audio file?'") 
        mic = sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            answer = r.recognize_google(audio)  
        except sr.UnknownValueError:
            os.system("say 'Sorry, I did not understand that'")
            
        z = answer + ".wav"
        print(z)
        
        harvard = sr.AudioFile(z)        
        with harvard as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)
        type(audio)    
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=4, width=60)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = "\"" + r.recognize_google(audio) + ".\""
        T.insert(END, quote) 
        os.system("say 'I think the passage is:'")
        mainloop() 
    """

        
    def Help(self):
        os.system("say 'Here are the instructions on how to navigate the application'")
        root = Tk()
        S = Scrollbar(root)
        T = Text(root, height=4, width=60)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        navigation = "It is self-explanatory; to use this app, all you need to do is speak into your microphone and tell your symptoms to Jan. It will gather all your symptoms and diagnosis you. Then,  Jan will give advice about treatment that can help with the illness. *WARNING* This is an app made by high-school       students and it will not always be the best idea to follow  our advice." 
        '''navigationtwo = "                                                 For the audiofile to text converter, make sure 1) the audio file is in .wav format AND 2) the audio file is in the      \"database\" directory."'''
        T.insert(END, navigation) 
        T.insert(END, navigationtwo)
        mainloop() 
        

    def start(self):
        FrontEnd.bot.start
        
        
root = Tk()
Front = FrontEnd(root)
root.mainloop()
















        