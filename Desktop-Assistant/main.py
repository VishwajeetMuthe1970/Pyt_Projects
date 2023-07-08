import speech_recognition as sr
import os


def speak(text):
    os.system(f"say {text}")


if __name__ == '__main__':
    speak("Hello I am your assistant AI.")

