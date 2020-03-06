#-------------------------------------
#    Program by Smolyak EW
#
#   Version   Date   Information
#     1.0     2019     13/06
#
#-------------------------------------
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser


engine = pyttsx3.init()
engine.say("Чего ты докоопался до меня,что я тебе сдеаал")
engine.runAndWait()

r =  sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("Скажи что-нибудь")
    audio = r.listen(source)

query = r.recognize_google(audio,language="ru-RU")
print("Вы сказали:" +query.lower())