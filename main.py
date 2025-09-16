import speech_recognition as sr
import webbrowser
import pyttsx3
import os

recognizer = sr.Recognizer()

def speak(text):
    tts = pyttsx3.init()
    tts.say(text)
    tts.runAndWait()
    tts.stop()

if __name__ == "__main__":
    speak("Allow me to introduce myself. I am Jarvis, A virtual artificial intelligence assistant. And i am here to assist you in your daily tasks.")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)

            activate = recognizer.recognize_google(audio).lower()

            if (activate.lower() == "jarvis"):
                speak("Yes, Sir how can I help you?")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower()
                print(command)

                if "open youtube" in command:
                    speak("Opening YouTube")
                    webbrowser.open("https://www.youtube.com")

                elif "open google" in command:
                    speak("Opening Google")
                    webbrowser.open("https://www.google.com")
                
                elif "open notepad" in command:
                    speak("Opening Notepad")
                    os.system("notepad.exe")

                elif "exit" in command or "quit" in command or "stop" in command:
                     speak("Goodbye, have a great day!")
                     break

                else:
                    speak("Sorry, I didn't understand that.")

        except sr.WaitTimeoutError: 
            continue
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            speak(f"Could not connect to recognition service; {e}")
            continue

