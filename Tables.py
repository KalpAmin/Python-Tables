import speech_recognition as sr
import pyttsx3

x = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)

with sr.Microphone() as source:
    def speak(text):
        engine.say(str(text))
        engine.runAndWait()

    def listen():
        print("listening...")
        audio = x.listen(source)
        print('recognising...')
        query = x.recognize_google(audio)
        print(f"You said : {query}\n")
        return query

    print("Hello everyone! Welcome to Python Tables!")
    speak("Hello everyone! Welcome to Python Tables!")

    x.adjust_for_ambient_noise(source)

    while True:
        speak("Enter a number whose table you need!")
        no = input("Type the number here : ")
        no = int(no)

        for m in range(1, 11):
            res = no*m
            print(f"{no} X {m} = {res}")

        speak("There you go!")
        speak("Now, do you want to continue or stop? Say yes or no...")
        user_input = listen()
        if user_input.lower()=="no":
            print("Thank you for using Python Tables!")
            speak("Thank you for using Python Tables!")
            break
        elif user_input.lower()=="yes":
            pass
