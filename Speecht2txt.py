import audioop
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine. runAndWait()


def StartUp():
    Start = int(datetime.datetime.now().hour)
    if Start>=0  and Start<12:
        speak("Good Morning Shubh: ")
    elif Start>=12 and Start<16:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("This is a programme for speech to text conversion, Please say something to convert into text")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listning to you : ")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("please Say that again..")
        return "None"

    return query 
if __name__ =="__main__":
    StartUp()
    takecommand()