import speech_recognition as sr
import pyttsx3


def listen(recognizer, language='es-ES'):
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio, language=language)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


engine = pyttsx3.init()
recognizer = sr.Recognizer()

user_input = listen(recognizer, 'en-US')

engine.say(user_input)
engine.runAndWait()
