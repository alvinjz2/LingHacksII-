import speech_recognition as sr
import os


class Illness:
    def __init__(self, name, sym, treat):
        self.name = name;
        self.symptom = sym
        self.treatment = treat
        count = 0
        
    def contains(self, sym):
        for i in range(len(self.symptom)):
            if(self.symptom[i] == sym): return True;
        return False;
    def sympFound(self):
        self.count+=1
    def likely(self):
        return self.count/(len(self.symptom))
    def getSymp(self):
        return self.symptom
        
    
    
class Medibot:
    question = 0
    r = sr.Recognizer()
    flu =0
    pinkI=0
    mono=0
    illnesses=[]
    agg_symptom=[]
    #Checks if the symptom has already been added to the list
    def sympAdded(sym):
        for i in range(len(agg_symptom)):
            if( agg_symptom[i] == sym):
                return True
        return False
    #creates list of illnesses
    def createIllList():
        flu = Illness("flu", ["fever", "chills", "muscle", "cough", "congestion", "runny nose", "headache", "fatigue"], "rest and drink fluids")
        pinkI = Illness("pink eye", ["redness", "itchy", "eye"], "avoid touching your eyes")
        mono = Illness("Mononucleosis", ["fatigue", "throat", "fever", "appetite", "muscle"], "rest and eat and drink healthy")
        illnesses = [flu, pinkI, mono]
        agg_symptom = []
        for i in range(len(illnesses)):
            for j in range(len(illnesses[i].agg_symptom)):
                if not sympAdded():
                    agg_symptom.append(illnesses[i].agg_symptom[j]);
    """
    #INITIALIZATION
    def __init__():
        createIllList()
    """

    #The bot says something out loud and prints it
    def speak(words):
        os.system("say '" + words + "'")
        print("JAN: " + words)
    #speaks the words transcribed from an audio file
    def Filespeak(words):
        os.system("say '" + words + "'")
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
            print("JAN: Hey there, " + user + "! My name is JAN. \nJAN: What are your symptoms?")
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
    #finds mentions of symptoms in user input
    def findKeywords(speech):
        split = speech.split()
        list = []
        for i in range(len(split)):
            #WORKING ON IT
            print()
        return list 
    #Adds to count of symptoms for all illnesses
    def increment(all_sym):
        for i in range(len(illnesses)):
            for j in range(len(all_sym)):    
                if illnesses[i].contains(all_sym[j]):
                    illnesses[i].sympFound();
    #the bot responds to the user's comment
    def respond(speech):
        #What should it say
        userSyms = findKeywords(speech)
        increment(userSyms)
        speed("Do you have a " + agg_symptom[question-1] + "?")
    #gets user input
    def getMic():
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source)
        try:
            speech = r.recognize_google(audio)
            print(user + ": " + speech)
            return speech
        except sr.UnknownValueError:
            speak("JAN: Can you repeat that?")
            getMic()
        
    #runs the program
    
    def start():
        createIllList()
        endPhrase = ["good bye", "quit", "exit", "stop"]
        getName(True)
        while(True):
            speech = getMic()
            if(speech != (endphrase[i] for i in range(len(endPhrase)))):
                question+=1
                respond(speech)
            else: 
                return

start()



    