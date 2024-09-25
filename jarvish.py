

import pyttsx3
import speech_recognition as sr
import openai
import main

#openai key
openai.api_key= main.OPEN_AI_KEY

#initailize speech engine

engine = pyttsx3.init()

def speak(word):
    engine.setProperty('rate',135)
    engine.setProperty('volume',0.8)

    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()

#initialize speech recoganizer

rec = sr.Recognizer()
speak('hlo little fool, speak what do u want')
with sr.Microphone() as source:
    audio= rec.listen(source)
    speak('i am getting answer little fool, wait')

text = rec.recognize_google(audio)

discussion=openai.Completion.create(
    prompt=text,
    engine='text-davinci-002',
    max_tokens=1000,
)


answer=discussion.choices[0].text


if answer:
    speak(answer)
