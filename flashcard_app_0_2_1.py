import tkinter as tk
import pyaudio
import wave
import datetime
import os
import subprocess

#import pygame
#import random

def launch_learning_app():
    def Open_New_Card():
        AddCard= tk.Tk()
        AddCard.title("Add A Card")
        
        #Define a class for the flashcard
        class Flashcard:
            def init(self, x, y, Eng_Gloss, Other_Language_Pronunciation, Note, Picture, Recording):
                self.x = x
                self.y = y
                self.image = image
                self.Eng_Gloss = Eng_Gloss
                self.Other_Language_Pronunciation = Other_Language_Pronunciation
                self.Note = Note
                self.Picture = Picture
                self.Recording = Recording
        #Initialize a list to store the flashcards
        flashcards = []

        def save_flashcard():
            # Get the front of the flashcard and the current date and time
            Eng_Gloss = Eng_Gloss.get()
            now = datetime.datetime.now()
            file_name = f"{Eng_Gloss}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.wav"

            # Save the recording with the unique file name
            recording = Recording.get()
            file_path = os.path.join("recordings", file_name)
            with open(file_path, "wb") as f:
                f.write(recording)

            flashcard = Flashcard(0, 0, Eng_Gloss, Other_Language_Pronunciation.get(), Note.get(), Picture.get(), file_path)
            flashcards.append(flashcard)
            print(f"Flashcard saved: {Eng_Gloss} / {Other_Language_Pronunciation}")
        
        #Function to create recordings
        def start_recording():
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 2
            RATE = 44100
            RECORD_SECONDS = 5
            WAVE_OUTPUT_FILENAME = "output.wav"

            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)

            print("* recording")

            frames = []

            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("* done recording")

            stream.stop_stream()
            stream.close()
            p.terminate()

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
        
        #Function to play recordings
        def play_recording():
            subprocess.run(["afplay", Recording.get()])
            
        #Create the text entry boxes
        Eng_Gloss = tk.Entry(AddCard, font=("Helvetica", 15), validate="key")
        Eng_Gloss.pack()

        Other_Language_Pronunciation = tk.Entry(AddCard, font=("Helvetica", 15), validate="key")
        Other_Language_Pronunciation.pack()
        
        record_button = tk.Button(AddCard, text="Record", command=start_recording, font=("Helvetica", 15))
        record_button.pack()
        
        #Create the play button
        play_button = tk.Button(AddCard, text="Play", command=play_recording, font=("Helvetica", 15))
        play_button.pack()

        #Create the save button
        save_button = tk.Button(AddCard, text="Save", command=save_flashcard, font=("Helvetica", 15))
        save_button.pack()
        
        AddCard.mainloop()
        
    def Remove_Card_Screen():
        # code goes here
        print("Remove Card pressed")
    def Randomzie_Card_Screen():
        # code goes here
        print("Randomize_Card_Screen pressed")
    def Add_Card_Screen():
        # code goes here
        print("Open_New_Card")
        
    # Set window size and title
    language_app = tk.Tk()
    language_app.title("Learning App")
    language_app.geometry("1200x800")
    width, height = 1200, 900
    
    #Setup grid for buttons
    for i in range(5):
        language_app.columnconfigure(i, weight=1, minsize=200)
    
    # Define a class for the flashcard
    class Flashcard:
        def __init__(self, x, y, image):
            self.x = x
            self.y = y
            self.image = image
            
    # Initialize a list to store the flashcards
    flashcards = []

    # Load the buttons
    plus_button = tk.Button(language_app, text="+", command=Add_Card_Screen, font=("Helvetica", 15), highlightthickness=5)
    minus_button = tk.Button(language_app, text="-", command=Remove_Card_Screen, font=("Helvetica", 15), highlightthickness=5)
    randomize_button = tk.Button(language_app, text="Randomize", command=Randomzie_Card_Screen, font=("Helvetica", 15), highlightthickness=5)
    CreateCard_button = tk.Button(language_app, text="Create Card", command=Open_New_Card, font=("Helvetica", 15), highlightthickness=5)
    
    plus_button.grid(row=0, column=6, pady=3, sticky='e')
    minus_button.grid(row=1, column=6, pady=3, sticky='e')
    randomize_button.grid(row=0, column=2, padx=15, sticky='w')
    CreateCard_button.grid(row=0, column=0, padx=15, sticky='nsew')
    
    language_app.mainloop()



def open_dictionary():
    # code to open dictionary goes here
    print("Dictionary Button pressed")


def show_settings():
    # Code to show the settings menu goes here
    print("Showing settings...")


root = tk.Tk()
root.title("Home Menu")
root.geometry("400x600")

launch_game_button = tk.Button(root, text="Launch DD", command=launch_learning_app, font=("Helvetica", 20), highlightthickness=10)
launch_game_button.pack(pady=20)

dictionary_button = tk.Button(root, text="Dictionary", command=open_dictionary, font=("Helvetica", 20), highlightthickness=10)
dictionary_button.pack(pady=20)

settings_button = tk.Button(root, text="Settings", command=show_settings, font=("Helvetica", 20), highlightthickness=10)
settings_button.pack(pady=20)

root.mainloop()
