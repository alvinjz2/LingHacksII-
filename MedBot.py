import speech_recognition as sr
import os
import nltk



class Illness:
    def __init__(self, name, sym, treat):
        self.name = name;
        self.symptom = sym
        self.treatment = treat
        self.count = 0
        
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
    b = False
    r = sr.Recognizer()
    illnesses=[]
    agg_symptom = []
    user = "User"
    #Checks if the symptom has already been added to the list
    def sympAdded(sym):
        for i in range(len(Medibot.agg_symptom)):
            if Medibot.agg_symptom[i] == sym:
                return True
        return False
    #creates list of illnesses and list of all symptoms
    def createIllList():
        
        flu = Illness("flu", ["fever", "chills", "muscle", "cough", "congestion", "runny", "headache", "fatigue"], "rest and drink fluids")
        pinkI = Illness("pink eye", ["redness", "itchy", "eye"], "avoid touching your eyes")
        mono = Illness("Mononucleosis", ["fatigue", "throat", "fever", "appetite", "muscle"], "rest and eat and drink healthy")
        headache = Illness("headache", ["dull", "ache", "sensitive", "tension"], "go to a quiet place. Massage the head or neck region. Remain calm and control your breath")
        pneumonia = Illness("pneumonia", ["chest", "fatigue", "fever", "sweat", "shake" "chill", "nausea", "vomit", "diarrhea", "breath"], "use antibiotics for some forms of pneumonia.")
        depression = Illness("depression", ["hate", "confidence", "interest", "fatigue", "sleep", "schedule", "suicide"], "contact mental health hotlines or a therapist and take prescribed antidepressants")
        strep_throat = Illness("strep throat", ["throat", "swallow", "tonsil", "neck", "fever", "headache", "rash", "nausea", "vomiting", "body", "swollen"], "Oral antibiotics will help with the recovery, and if necessary, painkillers will help with the pain and fever")
        disease5 = Illness("fifth disease", ["fever", "rash", "headache", "sore" "throat", "joint"], "just take pain relievers")
        sinusitis = Illness("bacterial sinusitis", ["congestion", "discharge", "throat", "cough", "mucus", "headache", "tenderness", "earache", "toothache", "breath", "smell", "taste", "fever", "fatigue"], "use nasal decongestants and nasal saline rinses")
        pertussis = Illness("whooping cough", ["runny", "congestion", "sneeze"], "use antibiotics to treat the whooping cough.")
        arthritis = Illness("Arthritis", ["pain", "swell", "motion", "weak", "walk", "stiff", "tenderness", "fatigue", "malaise", "flare", "red", "stiff", "inflammation", "joint"], "use medication, attend physical therapy, or get surgery to reduce symptoms")
        chlamydia = Illness("chlamydia", ["genital", "discharge"], "Antibiotic therapy will be helpful towards the treatment.")
        
        Medibot.illnesses = [flu, pinkI, mono, headache, pneumonia, depression, strep_throat, disease5, sinusitis, pertussis, arthritis, chlamydia]
        Medibot.agg_symptom = []
        
        for i in range(len(Medibot.illnesses)):
            for j in range(len(Medibot.illnesses[i].symptom)):
                if not Medibot.sympAdded(Medibot.illnesses[i].symptom[j]):
                    Medibot.agg_symptom.append(Medibot.illnesses[i].symptom[j]);
        
        """
        for i in range(len(Medibot.illnesses)):
            for j in range(len(Medibot.illnesses[i].symptom)):
                for b in range(len(Medibot.agg_symptom)):
                    if Medibot.agg_symptom[b] == Medibot.illnesses[i].symptom[j]:
                        break
                Medibot.agg_symptom.append(Medibot.illnesses[i].symptom[j]);
        """
        

    #The bot says something out loud and prints it
    def speak(words):
        if words[:5] != "JAN: ":
            words = "JAN: " + words
        print(words)
        words = words[5:]
        os.system("say '" + words + "'")
    #speaks the words transcribed from an audio file
    def Filespeak(words):
        os.system("say '" + words + "'")
    #Gets the name of the user
    def getName(first):
        if first == True:
            Medibot.speak("JAN: Hello! What's your name?")
            first = False
        mic = sr.Microphone()
        with mic as source:
            audio = Medibot.r.listen(source)
        try:
            user = Medibot.r.recognize_google(audio)
            Medibot.speak("JAN: Hey there, " + user + "! My name is JAN.")
            Medibot.speak("JAN: What are your symptoms?")
        except sr.UnknownValueError:
            Medibot.speak("JAN: Can you repeat that?")
    #transcribes an audio file from  beg seconds in to beg+len seconds
    def AudioFileBegLen(FileDotWav, beg, len):
        test = sr.AudioFile(FileDotWav)
        with test as source:
            audio = Medibot.r.record(source, offset = beg, duration = len)
            speech = Medibot.r.recognize_(audio)
            print("File: " + speech + "")
        Medibot.Filespeak(speech)
    #Transcribes an audio file from beginning to len seconds
    def AudioFileLen(FileDotWav, len):
        Medibot.AudioFileBegLen(FileDotWav, 0, len)
    #transcribes an entire audio file
    def AudioFile(FileDotWav):
        Medibot.AudioFileLen(FileDotWav, sr.AudioFile(FileDotWav).Duration)
    
    #finds mentions of symptoms in user input
    def findKeywords(speech):
        split = speech.split()
        lem = nltk.stem.WordNetLemmatizer()
        for s in split:
            lem.lemmatize(s)
        list = []
        for i in range(len(split)):
            for j in range(len(Medibot.agg_symptom)):
                if(split[i] == "hi" or split[i] == "hello" or split[i] == "hey"):
                    Medibot.speak("JAN: Hello, " + Medibot.user+"!")
                    Medibot.speak("JAN: Tell me about your symptoms.")
                    return
                elif(split[i] == Medibot.agg_symptom[j]):
                    list.append(Medibot.agg_symptom[j])
                    Medibot.agg_symptom[j].pop()
                    j-=1
        return list 
    #Adds to count of symptoms for all illnesses
    def increment(all_sym):
        for i in range(len(Medibot.illnesses)):
            for j in range(len(all_sym)):    
                if Medibot.illnesses[i].contains(all_sym[j]):
                    Medibot.illnesses[i].sympFound();
    #the bot responds to the user's comment
    def respond(speech):
        userSyms = Medibot.findKeywords(speech)
        if len(userSyms) <1:
            return
        Medibot.increment(userSyms)
        s = Medibot.agg_symptom[Medibot.question-1]
        if s[:len(s)-1] == "s" and s[:len(s)-3] == "ion":
            Medibot.speak("Do you have " + s + "?")
        elif s=="muscle" or s=="throat" or s=="eye" or s=="joint" or s=="chest":
            Medibot.speak("Does your " + s+" hurt?")
        elif s=="runny":
            Medibot.speak("Do you have a runny nose?")
        elif s=="fatigue" or s=="sleep":
            Medibot.speak("Are you feeling sleepy?")
        else:
            Medibot.speak("Do you have a " + s + "?")
        
    #gets user input
    def getMic():
        mic = sr.Microphone()
        with mic as source:
            audio = Medibot.r.listen(source)
        try:
            speech = Medibot.r.recognize_google(audio)
            print(Medibot.user + ": " + speech)
            return speech
        except sr.UnknownValueError:
            Medibot.speak("JAN: Can you repeat that?")
            Medibot.getMic()
    def highStick():
        index = 0
        for i in range(len(Medibot.illnesses)):
            if Medibot.illnesses[i].likely() > Medibot.illnesses[index].likely():
                index = i
        return Medibot.illnesses[index]
    #runs the program
    def start():
        Medibot.createIllList()
        endPhrase = ["good bye", "quit", "exit", "stop"]
        Medibot.getName(True)
        while(True):
            speech = Medibot.getMic()
            if(speech != (endPhrase[i] for i in range(len(endPhrase)))):
                if(Medibot.question <= len(Medibot.agg_symptom)):
                    Medibot.question+=1
                    Medibot.respond(speech)
                else:
                    ill = Medibot.highSick()
                    Medibot.speak("JAN: I think you might have " + ill.name + ".")
                    Medibot.speak("JAN: " + ill.count + " symptoms of " + ill.name + " match your condition.")
                    Medibot.speak("JAN: To get better, you should " + ill.treatment + ".")
                    Medibot.speak("JAN: Get well soon, " + Medibot.user + "!")
            else: 
                return

Medibot.start()