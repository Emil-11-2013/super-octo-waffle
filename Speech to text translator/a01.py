import speech_recognition as sr
import pyttsx3
from googletrans import Translator



def speak(text, lang="en"):
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if lang == "en":
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

        engine.say(text)
        engine.runAndWait()


def speech_to_text(text):
   recognizer = sr.Recognizer()
   with sr.Microphone() as source:
       print("Say something!")
       audio = recognizer.listen(source)



   try:
       print("Recognizing...")
       text = recognizer.recognise_google(audio, language="en")

       print(text)
       return text
   except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio")
       return "Google Speech Recognition could not understand audio"
   except sr.RequestError:
       print("Could not request results from Google Speech Recognition service")
   return ""

def translate_text(text, lang="en"):
    translator = Translator()
    translation = translator.translate(text, dest=lang)
    return translation

def display_language_options():
   print("Language options:")
   print(" 1 Tamil")
   print(" 2 Hindi")
   print(" 3 Telugu")
   print(" 4 Malayalam")
   print(" 5 Gujarati")
   print(" 6 Punjab")
   print(" 7 Bengali")
   print(" 8 Kannada")

   choice = int(input("Enter your choice: "))
   language_dict ={
   "1":"ta",
   "2":"hi",
    "3":"te",
    "4":"mal",
    "5":"guj",
    "6":"pun",
     "7":"beng",
       "8":"kan",

   }

   return language_dict.get(choice,"es")
def main():
   target_language = display_language_options()

   original_text = speech_to_text(target_language)

   translation_text = translate_text(original_text)

   speak(translation_text, target_language)

   print(translation_text)



if __name__ == "__main__":
    main()