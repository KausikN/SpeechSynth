'''
Functions to synthesize speech to text
'''

# Imports
import speech_recognition as sr
import pyttsx3

# Functions
def InitRecognizer():
    r = sr.Recognizer()
    return r

# Text to Speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Speech2Text(rec):
    # Loop Infinitely to hear user voice
    while(1):
        print("Speak Now")
        # Exception handling to handle
        # exceptions at the runtime
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                rec.adjust_for_ambient_noise(source2, duration=0.2)

                #listens for the user's input
                audio2 = rec.listen(source2)

                # Using ggogle to recognize audio
                MyText = rec.recognize_google(audio2)
                MyText = MyText.lower()

                print("Spoken Text:", MyText)
                SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown Error Occured")

# Driver Code
# Params

# Params

Recognizer = InitRecognizer()
Speech2Text(Recognizer)