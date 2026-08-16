from customtkinter import *
import speech_recognition as sr
import pyttsx3
from google import genai


class VoiceChat:

    def __init__(self):
        self.root = CTk()
        self.root.title("voic chat")
        self.root.geometry("400x500+900+100")
        self.root.configure(fg_color="#67faff")

        self.box = CTkTextbox(self.root, width=350, height=419, corner_radius=10,fg_color="#f0f0f0", text_color="#333333",
                              font=("Arial", 25, "bold"))
        self.box.place(x=25, y=13)


        self.button = CTkButton(self.root, text="   🎙️",font=("Arial", 30, "bold"),width=60, height=60,corner_radius=30,
                                fg_color="#0052cc",hover_color="#050505",command=self.voice)
        self.button.place(x=120, y=439)
        self.root.mainloop()


    def voice(self):
        mic = sr.Recognizer()
        mic.pause_threshold = 3

        with sr.Microphone() as source:
            self.box.insert("end", "Recording")
            self.box.update()

            audio = mic.listen(source, timeout=5, phrase_time_limit=5)

            self.box.delete("1.0", "end")

        self.box.update()

        text = mic.recognize_google(audio, language="en-US")

        client = genai.Client(api_key=">>>> GOOGLE API <<<")

        Model = "gemini-2.5-flash"

        chat = client.chats.create(model=Model,config={"system_instruction": "کوتاه و اینگلیسی"})

        response = chat.send_message(text)

        self.box.delete("1.0", "end")
        self.box.update()

        self.box.insert("end", response.text)

        e = pyttsx3.init()
        e.setProperty("rate", 120)
        e.say(response.text)
        e.runAndWait()


VoiceChat()