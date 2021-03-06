'''
Functions to synthesize text to speech
'''

# Imports
from gtts import gTTS
from playsound import playsound

# Functions
def Text2Speech(text, language):
    if language in ['en', 'english']:
        language = 'en'
    return gTTS(text=text, lang=language, slow=False)

def PlayAudio(audio_file_path, block=True):
    playsound(audio_file_path, block=block)

def SaveAudio(audio_file_path, audio):
    audio.save(audio_file_path)

# Driver Code
# Params
audio_save_path = "wimbaway.mp3"
text = "Lala kahle"
language = "en"
# Params

audio = Text2Speech(text, language)
SaveAudio(audio_save_path, audio)
PlayAudio(audio_save_path)