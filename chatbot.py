import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import wikipedia

def speak(input) :
    engine = pyttsx3.init()
    print(input)
    engine.say(input)
    engine.runAndWait()
    engine.getProperty("rate")
    engine.setProperty("rate", 150)
    
def listen():
    r = sr.Recognizer()
    while True :
        with sr.Microphone() as source:
            speak("listening")
            
            audio = r.listen(source)
        try:
            resp = r.recognize_google(audio, language="en-in")
            return resp
        except:
            speak("say that again")

def firstLine(text):
    for i in range(0, len(text)):
        if(text[i] == '.'):
            index = i
            break;
    return text[:index+1]

def printRules():
    speak("       ---->> RULES <<----")
    speak("There are 21 sticks in total.")
    speak("One can pick any number of sticks from 1-4.")
    speak("The player who picks the last stick, looses")
    speak("You get the opportunity to pick first")

one = ["1", "one", "won", 1]
two = ["tu", "two", "2", "who", "to", "too", 2]
three = ["three", "free", "tree", "3", 3]
four = ["four", "4", "for", "fork", 4, "pol", "Ford"]
hi = ["hello", "hi", "hey", "hola", "hai"]
bye = ["exit", "quit", "bye", "bye bye", "okay then bye", "tata", "goodbye", "okay bye", "ok bye"]
made = ["who made you", "who created you"]
ok = ["okay", "ok", "OK", "done"]
extra = ["yes", "no", "nothing", "shut up", "not much"]
sites = ["Google", "Yahoo", "Facebook", "Twitter", "Instagram", "Wikipedia", "Amazon", "Flipkart", "Linkedin", "Github"]
basic = ["how are you", "how you doing", "how's you"] 
ques = ["what", "when", "where", "how", "why", "if", "who", "whom", "whose"]
 
def playGame():
    sticks_left = 21
    while(sticks_left <= 21):
        if(sticks_left == 1):
            speak("You have to pick this last stick ...Sorry you lost")
            break
        speak("How many sticks do you want : 1-4 ")      
        text = listen()
        user_chosen = 0
        if(text in one) : user_chosen = 1
        elif(text in two) : user_chosen = 2
        elif(text in three) : user_chosen = 3
        elif(text in four) : user_chosen = 4
        else:
            speak("Please pick 1 to 4 sticks only")
            continue
        
        sticks_left = sticks_left - user_chosen
        speak("Sticks left : " + str(sticks_left))
        computer_chosen = 5- user_chosen
        speak("Computer picked " + str(computer_chosen) + " sticks")
        sticks_left = sticks_left - computer_chosen
        speak("Sticks left : " + str(sticks_left))
        

def startGame():
    speak("Do you want to know the rules : yes or no ")
    y = listen()
    if (y == "yes"):
        printRules()
        playGame()
    elif(y == "no"):
        speak("Okay...  Let's get started then")
        playGame()
    else :
        speak("Type only yes or no")
    

def game():
    speak("Do you want to play a 21-Stick game : yes or no ")
    x = listen()
    if (x == "yes") :
        speak("Okay... let's start")
        startGame()
    elif (x == "no"):
        speak("Bye then")
    else :
        speak("Type only yes or no")

while (True):
    resp = listen()
    if ("game" in resp):
        game()
    elif(resp in hi):
        speak(random.choice(hi))
    elif(resp in made):
        speak(random.choice(["CHIANX made me", "CHIANX created me", "I was made by CHIANX"]))
    elif("open" in resp):
        print(resp)
        for i in range(0, len(sites)):  
            if(sites[i] in resp):
                print(resp) 
                speak("loading " + sites[i])
                webbrowser.open_new("www." + sites[i] + ".com")
                break;
    elif(("your name" in resp) | ("who are you" in resp)):
         speak("My name is Khoosh")
    elif(resp in basic):
        speak(random.choice(["I am good. How about you ?", "Great, What about you ?", "I am fine, What can i do for you ?"]))
    elif(resp in bye):
        speak(random.choice(["Okay bye", "bye bye", "tata", "bye then", "bye"]))
        break
    elif("time" in resp):
        time = datetime.datetime.now()
        speak(time.strftime("The time is %H:%M"))
    elif("date" in resp):
        date =  datetime.date.today()
        speak(date)
    elif(resp in ok):
        speak(random.choice(["Cool", "great", "awesome", "Good, What can I do for you?"]))
    elif(resp in ques):
        webbrowser.open_new('www.google.com/search?q=' + resp)
    elif(resp in extra):
        speak("Okay")
    elif("search" in resp):
        speak("Searching " + resp.split(' ', 1)[1] + " on google")
        webbrowser.open_new('www.google.com/search?q=' + resp.split(' ', 1)[1])    
    elif(("you" in resp) | ("your" in resp)):
            speak("Sorry I did not follow that, please contact my developer CHIANX")
    else: 
        speak(firstLine(wikipedia.summary(resp)))
        speak("Do you want more information. Say yes or no")
        x = listen()
        if(x == "yes"):
            speak(wikipedia.summary(resp))
            speak("Say 'Search " + resp + " ' , if you want to look on Google")
        elif(x == "no"):
            speak("Okay")
        else :
            speak("Say yes or no only")