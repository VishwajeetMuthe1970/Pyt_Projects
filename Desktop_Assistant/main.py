import speech_recognition as sr
import win32com.client
import webbrowser


def say(s):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    #  print("Now type whatever you want your computer to speak for you. ")
    # s = input()
    speaker.Speak(s)


# To take command from microphone.
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from  Assistant."


# if __name__ == '__main__':
print("Listening....")
say("Hello I am your A.I. based desktop  assistant.")
while True:
    query = takecommand()
    if "Open YouTube" in query.lower():
        say("Opening youtube sir...")
        webbrowser.open("https://youtube.com")

# say(query)
