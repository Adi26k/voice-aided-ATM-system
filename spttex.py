from traceback import print_tb
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
def spttx():
    while(1):	


        try:
    
    
            with sr.Microphone() as source2:
    
                r.adjust_for_ambient_noise(source2, duration=0.2)
        
    
                audio2 = r.listen(source2)
                print("Input accepted...")
        
                MyText = r.recognize_google(audio2)
                print(MyText)
                MyText = MyText.lower()

                return(MyText)
        
        
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    
        except sr.UnknownValueError:
            print("unknown error occured")
            SpeakText("Speak Again")
def SpeakText(command):
    print(command)  
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()