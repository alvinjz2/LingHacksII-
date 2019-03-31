import speech_recognition as sr
import os


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
    r = sr.Recognizer()
    flu =0
    pinkI=0
    mono=0
    illnesses=[]
    agg_symptom=[]
    #Checks if the symptom has already been added to the list
    def sympAdded(sym):
        for i in range(len(agg_symptom)):
            if agg_symptom[i] == sym:
                return True
        return False
    #creates list of illnesses
    def createIllList():
        
        flu = Illness("flu", ["fever", "chills", "muscle", "cough", "congestion", "runny", "headache", "fatigue"], "rest and drink fluids")
        pinkI = Illness("pink eye", ["redness", "itchy", "eye"], "avoid touching your eyes")
        mono = Illness("Mononucleosis", ["fatigue", "throat", "fever", "appetite", "muscle"], "rest and eat and drink healthy")
        headache = Illness("headache", ["dull, ache", "sensitive, tension"], "go to a quiet place. Massage the head or neck region. Remain calm and control your breath")
        pneumonia = Illness("pneumonia", ["chest", "fatigue", "fever", "sweat", "shake" "chill", "nausea", "vomit", "diarrhea", "breath"], "use antibiotics for some forms of pneumonia.")
        depression = ("depression", ["hate", "confidence", "interest", "fatigue", "sleep", "schedule", "suicide"], "contact mental health hotlines or a therapist and take prescribed antidepressants")
        strep_throat = Illness("strep throat", ["throat", "swallow", "tonsilwh", "neck", "fever", "headache", "rash", "nausea", "vomiting", "body", "swollen"], "Oral antibiotics will help with the recovery, and if necessary, painkillers will help with the pain and fever")
        disease5 = Illness("fifth disease", ["fever", "rash", "headache", "sore" "throat", "joint"], "just take pain relievers")
        sinusitis = Illness("bacterial sinusitis", ["congestion", "discharge", "throat", "cough", "mucus", "headache", "tenderness", "earache", "toothache", "breath", "smell", "taste", "fever", "fatigue"], "use nasal decongestants and nasal saline rinses")
        pertussis = Illness("whooping cough", ["runny", "congestion", "sneeze"], "use antibiotics to treat the whooping cough.")
        arthritis = Illness("Arthritis", ["pain", "swell", "motion", "weak", "walk", "stiff", "tenderness", "fatigue", "malaise", "flare", "red", "stiff", "inflammation", "joint"], "use medication, attend physical therapy, or get surgery to reduce symptoms")
        chlamydia = Illness("chlamydia", ["genital", "discharge"], "Antibiotic therapy will be helpful towards the treatment.")
        
        illnesses = [flu, pinkI, mono, headache, pneumonia, depression, strep_throat, disease5, sinusitis, pertussis, arthritis, chlamydia]
        agg_symptom = []
        
        for i in range(len(illnesses)):
            for j in range(len(illnesses[i].agg_symptom)):
                if not sympAdded():
                    agg_symptom.append(illnesses[i].agg_symptom[j]);


    #The bot says something out loud and prints it
    def speak(words):
        if words[:5] == "JAN: ":
            words = words[5:]
        os.system("say 'i should be talking'")
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
            speak("JAN: Hey there, " + user + "! My name is JAN.")
            speak("JAN: What are your symptoms?")
        except sr.UnknownValueError:
            speak("JAN: Can you repeat that?")
    #transcribes an audio file from  beg seconds in to beg+len seconds
    def AudioFileBegLen(FileDotWav, beg, len):
        test = sr.AudioFile(FileDotWav)
        with test as source:
            audio = r.record(source, offset = beg, duration = len)
            speech = r.recognize_(audio)
            print("File: " + speech + "")
        Filespeak(speech)
    #Transcribes an audio file from beginning to len seconds
    def AudioFileLen(FileDotWav, len):
        AudioFileBegLen(FileDotWav, 0, len)
    #transcribes an entire audio file
    def AudioFile(FileDotWav):
        AudioFileLen(FileDotWav, sr.AudioFile(FileDotWav).Duration)
    #finds mentions of symptoms in user input
    def findKeywords(speech):
        split = speech.split()
        list = []
        for i in range(len(split)):
            for j in range(len(agg_symptom)):
                if(split[i] == agg_symptom[j]):
                    list.append(agg_symptom[j])
        return list 
    #Adds to count of symptoms for all illnesses
    def increment(all_sym):
        for i in range(len(illnesses)):
            for j in range(len(all_sym)):    
                if illnesses[i].contains(all_sym[j]):
                    illnesses[i].sympFound();
    #the bot responds to the user's comment
    def respond(speech):
        userSyms = findKeywords(speech)
        increment(userSyms)
        speak("Do you have a " + agg_symptom[question-1] + "?")
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
    
        endPhrase = ["good bye", "quit", "exit", "stop"]
        getName(True)
        while(True):
            speech = getMic()
            if(speech != (endphrase[i] for i in range(len(endPhrase)))):
                if(question <= len(agg_symptoms)):
                    question+=1
                    respond(speech)
                else:
                    ill = highSick()
                    speak("JAN: I think you might have " + ill.name + ".")
                    speak("JAN: " + ill.count + " symptoms of " + ill.name + " match your condition.")
                    speak("JAN: To get better, you should " + ill.treatment + ".")
                    speak("JAN: Get well soon, " + user + "!")
            else: 
                return

start()



    