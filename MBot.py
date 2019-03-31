import speech_recognition as sr
import os
import random
import nltk
nltk.download('wordnet')



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
    b = True
    r = sr.Recognizer()
    illnesses=[]
    agg_symptom = []
    user = "User"
    endPhrase = ["bye", "quit", "exit", "stop"]
    nextPhase = ["diagnose", "done"]
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
        
        
        

    #The bot says something out loud and prints it
    def speak(words):
        print("JAN: " + str(words))
        os.system("say '" + str(words) + "'")
    #speaks the words transcribed from an audio file
    def Filespeak(words):
        os.system("say '" + str(words) + "'")
    #Gets the name of the user
    def getName(first):
        if first == True:
            Medibot.speak("Hello! What's your name?")
            first = False
        
        mic = sr.Microphone()
        with mic as source:
            audio = Medibot.r.listen(source)
        
        try:
            Medibot.user = Medibot.r.recognize_google(audio)
            Medibot.speak("Hey there, " + Medibot.user + "! My name is JAN.")
            Medibot.speak("What are your symptoms?")
        except sr.UnknownValueError:
            Medibot.speak("Can you repeat that?")
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
        if speech is not None:
            split = speech.split()
            lem = nltk.stem.WordNetLemmatizer()
            for s in split:
                lem.lemmatize(s)
            list = []
            numList = []
            
            for i in range(len(split)):
                for k in range(len(Medibot.endPhrase)):
                    if split[i] == Medibot.endPhrase[k]:
                        Medibot.b = False
                        return
                for h in range(len(Medibot.nextPhase)):
                    if split[i] == Medibot.nextPhase[h]:
                        Medibot.b = False
                        return
                for j in range(len(Medibot.agg_symptom)):
                    #print(split[i])
                    #print(str(j) +", "+str(len(Medibot.agg_symptom)))
                    if(split[i] == Medibot.agg_symptom[j]):
                        list.append(Medibot.agg_symptom[j])
                        numList.append(j)
                    elif(split[i] == "hi" or split[i] == "hello" or split[i] == "hey"):
                        Medibot.speak("Hello, " + Medibot.user+"!")
                        Medibot.speak("Tell me about your symptoms.")
                        return
            for i in range(len(numList)-1, 0, -1):
                Medibot.agg_symptom.pop(i)
            return list
        else:
            Medibot.b = False
            return []
            
    #Adds to count of symptoms for all illnesses
    def increment(all_sym):
        for i in range(len(Medibot.illnesses)):
            for j in range(len(all_sym)):    
                if Medibot.illnesses[i].contains(all_sym[j]):
                    Medibot.illnesses[i].sympFound();
    #the bot responds to the user's comment
    def respond(speech):
        if speech is not None:
            split = speech.split()
            for i in range(len(split)):
                for j in range (len(Medibot.endPhrase)):
                    if split[i] == Medibot.endPhrase[j]:
                        return
                for k in range(len(Medibot.nextPhase)):
                    if split[i] == Medibot.nextPhase[k]:
                        return
            
            userSyms = Medibot.findKeywords(speech)
            if len(userSyms) >1:
                Medibot.increment(userSyms)  
        """
        if speech.bool():
            for i in range(len(Medibot.illnesses)):
                for j in range(Medibot.illnesses[i].symptom):    
                    if Medibot.sickn == Medibot.illnesses[i].symptom[j]:
                        Medibot.illnesses[i].sympFound();
        else:
        """
        """ff
        s = Medibot.agg_symptom[random.randint(0, len(Medibot.agg_symptoms))]
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
        return s;
        
        """
        if Medibot.b:
            asking = ["What other symptoms do you have?", "Tell me more about your symptoms.", "Can you think of any other symptoms you might have?", "Do you have any other symptoms?"]
            x = random.randint(0, len(asking)-1)
            Medibot.speak(asking[x])
    #gets user input
    def getMic():
        mic = sr.Microphone()
        with mic as source:
            audio = Medibot.r.listen(source)
        try:
            speech = Medibot.r.recognize_google(audio)
            print(Medibot.user + ": " + speech)
            if len(speech.split()) == 1:
                if (speech.split())[0] == "yes" or (speech.split())[0] == "yeah":
                    return True
                elif speech.split()[0] == "no":
                    return False
            else:
                return speech
        except sr.UnknownValueError:
            Medibot.speak("Can you repeat that?")
            Medibot.getMic()
    def highSick():
        index = 0
        for i in range(len(Medibot.illnesses)):
            if Medibot.illnesses[i].likely() > Medibot.illnesses[index].likely():
                index = i
        return Medibot.illnesses[index]
    #runs the program
    def start():
        Medibot.createIllList()
        Medibot.getName(True)
        b = 0
        while(b<12):
            speech = Medibot.getMic()
            
            print("End phrase")
            for i in range(len(Medibot.endPhrase)):
                print(str(i))
                if(speech is not None):
                    split = speech.split()
                    for j in range(len(split)):
                        if(split[j] == (Medibot.endPhrase[i])):
                            return
            print("Next phrase")
            for j in range(len(Medibot.nextPhase)):
                print(str(j))
                if speech is not None:
                    split = speech.split()
                    for i in range(len(split)):
                        if(split[i] == (Medibot.nextPhase[j])):
                            ill = Medibot.highSick()
                            Medibot.speak("I think you might have " + ill.name + ".")
                            Medibot.speak("" + ill.count + " symptoms of " + ill.name + " match your condition.")
                            Medibot.speak("To get better, you should " + ill.treatment + ".")
                            Medibot.speak("Get well soon, " + Medibot.user + "!")
                            return
            Medibot.question+=1
            Medibot.respond(speech)
            b+=1


