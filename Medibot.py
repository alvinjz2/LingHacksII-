import speech_recognition as sr
import os

r = sr.Recognizer()

#Gets the name of the user
def getName(first):
    if(first == True):
        speak("Hello! What's your name?")
        first = False
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    try:
        user = r.recognize_google(audio)
        print("JAN: Hey there, " + user + "! My name is JAN. \nJAN: Tell me something about yourself")
    except sr.UnknownValueError:
        print("JAN: Can you repeat that?")

#Transcribes an audio file from beginning to len seconds
def AudioFileLen(FileDotWav, len):
    test = sr.AudioFile(FileDotWav)
    with test as source:
        audio = r.record(source, duration = len)
        speech = r.recognize_google(audio)
        print("File: " + speech + "")
    Filespeak(speech)
#transcribes an audio file from  beg seconds in to beg+len seconds
def AudioFileBegLen(FileDotWav, beg, len):
    test = sr.AudioFile(FileDotWav)
    with test as source:
        audio = r.record(source, offset = beg, duration = len)
        speech = r.recognize_google(audio)
        print("File: " + speech + "")
    Filespeak(speech)

#transcribes an entire audio file
def AudioFile(FileDotWav):
    test = sr.AudioFile(FileDotWav)
    with test as source:
        audio = r.record(source)
        speech = r.recognize_google(audio)
        print("File: " + speech + "")
    Filespeak(speech)
#The bot says something out loud and prints it
def speak(words):
    os.system("say '" + words + "'")
    print("JAN: " + words)
#the bot responds to the user's comment
def respond(speech):
    #What should it say
    speak("Why I am alive?")
#gets user input
def getMic():
    print("JAN: I command you to speak!")
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
    try:
        speech = r.recognize_google(audio)
        print(user + ": " + speech)
        return speech
    except sr.UnknownValueError:
        print("JAN: Can you repeat that?")
        getMic()
#speaks the words transcribed from an audio file
def Filespeak(words):
    os.system("say '" + words + "'")
    
#runs the program
def start():
    getName(True)
    while():
        speech = getMic()
        if(speech != "quit"): 
            respond(speech)
        else: 
            return
            
            
start()


    