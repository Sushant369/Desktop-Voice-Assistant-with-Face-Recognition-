import os
from Face_Recognition import *



try:
  import speech_recognition
except ImportError:
  print("Trying to Install required module: SpeechRecognition\n")
  os.system('python -m pip install SpeechRecognition')

try:
  import wikipedia
except ImportError:
  print("Trying to Install required module: wikipedia\n")
  os.system('python -m pip install wikipedia')

try:
  import webbrowser
except ImportError:
  print("Trying to Install required module: webbrowser\n")
  os.system('python -m pip install webbrowser')

try:
  import smtplib
except ImportError:
  print("Trying to Install required module: smtplib\n")
  os.system('python -m pip install smtplib')

try:
  import pyttsx3
except ImportError:
  print("Trying to Install required module: pyttsx3\n")
  os.system('python -m pip install pyttsx3')


import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyttsx3
import subprocess

 

 

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

global mails
mails={"Sushant":"2015sushant.shelar@ves.ac.in","Sahil":"2015sahil.bhaldar@ves.ac.in"}
# print(voices[0].id)

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

    return True


def WishMe():

    hour=int(datetime.datetime.now().hour)

    if(hour>=6 and hour<12):

        speak("good morning")

    elif(hour>=12 and hour<=16):

        speak("good afternoon")

    elif(hour>=16 and hour<=19):

        speak("good evening")

    else:

        speak("good night")

 

def takeCommand():
    #takes microphone input from user return string
    r=sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening....")

        r.pause_threshold=1

        audio=r.listen(source)

        try:

            print("Recognizing....")

            query=r.recognize_google(audio,language="en-in")

            print(query)

        except Exception:

            #print(e)

            print("say that again")

            return "None"

    return query

def RecognitionFace():
  faceRec()

 

 
def sendEmail(to,content):
    try:
        print(content)
        send="sushantshelar121@gmail.com"
        #rec="2015sushant.shelar@ves.ac.in"
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.login(send,"***")
        print("login success")
        s.sendmail(send,to,content)
        s.quit()
        return True
    except Exception as e:
        print(e)
        #s= smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
        speak("send Email function failed")
        return False
 
name=["sushant shelar","sahil bhaldar"]
def code():

    while True:

      query=takeCommand().lower()

      if query != None:
          if "hey martian" or "ok martian" or "hie martian" or "hello martian" or "kay bolto martian" in query:

            Id1=faceRec()
            WishMe()
            # faceRec()
            for i in name:
              if Id1 == i:
                if speak("martian aiktoy"):

                    query=takeCommand().lower()

                    if "on google" in query:

                        speak("searching on google")

                        query=query.replace("google","")

                        query=query.replace("search","")

                        webbrowser.open("https://www.google.com/search?q="+query+"&rlz=1C1GCEB_enIN879IN880&oq="+query+"&aqs=chrome..69i57j0l7.1389j0j8&sourceid=chrome&ie=UTF-8")

                        code()

                    if "on wikipedia" in query:

                        speak("searching wikipedia")

                        print(query)

                        query=query.replace("wikipedia","")

                        print(query)

                        results=wikipedia.summary(query,sentences=2)

                        speak("According to wikipedia")

                        speak(results)

                        code()
                    
                    if "open notepad" in query:
                        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                        code()

                    if "on youtube" in query:
                        
                        speak("searching on youtube")

                        query=query.replace("on youtube","")

                        query=query.replace("search","")

                        webbrowser.open("https://www.youtube.com/results?search_query="+query)

                        code()
                    if "recognise me" in query:
                      id1=faceRec()
                      # time.sleep(6)
                      print(id1)
                      speak(id1)


                    if "send email" in query: 
                        try:
                            speak("tell me  recipient's name")
                            to=takeCommand()
                            print(to)
                            to=mails[to]
                            speak("what should I say")
                            content=takeCommand()
                            check=sendEmail(to,content)
                            if check :
                                speak("email has been sent!")
                        except Exception as e:
                            print(e)
                            speak("Unable to send email")
                    else:
                        time.sleep(1.5)
              else:
                speak("Identity did not matched")

if __name__ == "__main__":

    code()
