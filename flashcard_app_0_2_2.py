import tkinter as tk
import pyaudio
import wave
import datetime
import os
import subprocess
import random
from PIL import Image, ImageTk
from io import BytesIO

# Written in python 3.10.9


def launch_learning_app():
    def Open_New_Card():
        AddCard= tk.Toplevel()
        AddCard.title("Add A Card")
        AddCard.geometry("600x800")
        
        #Define a class for the flashcard
        class Flashcard:
            def init(self, x, y, Eng_Gloss, Other_Language_Pronunciation, Note, Picture, Recording):
                self.x = x
                self.y = y
                self.Eng_Gloss = Eng_Gloss
                self.Other_Language_Pronunciation = Other_Language_Pronunciation
                self.Note = Note
                self.Picture = Picture
                self.Recording = Recording
        #Initialize a list to store the flashcards
        #flashcards = []
        
        def paste_image():
            # Get image data from the clipboard
            image_data = AddCard.clipboard_get()
            # Use Pillow to open the image
            image = Image.open(BytesIO(image_data))
            # Convert the image to a PhotoImage object
            photo = ImageTk.PhotoImage(image)
            # Update the label to display the image
            label.config(image=photo)
            label.image = photo
            Picture.set(photo)
            
            # Save the image with a unique file name
            Eng_Gloss = Eng_Gloss.get()
            now = datetime.datetime.now()
            Picture_file_name = f"{Eng_Gloss.get()}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.png"
            image.save(Picture_file_name)
            
        def save_flashcard():
            # Get the gloss of the flashcard and the current date and time to create unique file names
            Eng_Gloss = Eng_Gloss.get()
            now = datetime.datetime.now()
            Recording_file_name = f"{Eng_Gloss}_{now.strftime('%Y-%m-%d_%H-%M-%S')}"#May need.wav
            
            # Save the recording with the unique file name
            recording = Recording.get()
            Recording_file_path = os.path.join("recordings", Recording_file_name)
            wf = wave.open(Recording_file_path, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            with wave.open(Recording_file_path, 'wb') as f:
                f.write(recording)
            
            flashcard = Flashcard(0, 0, Eng_Gloss, Other_Language_Pronunciation.get(), Note.get(), Picture_file_name, Recording_file_path)
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
            subprocess.run(["afplay", WAVE_OUTPUT_FILENAME])
            
        #Create the text entry boxes
        Eng_Gloss = tk.Entry(AddCard, font=("Helvetica", 25), validate="key")
        Eng_Gloss.insert(0, "Enter English Gloss")
        Eng_Gloss.pack()

        Other_Language_Pronunciation = tk.Entry(AddCard, font=("Helvetica", 25), validate="key")
        Other_Language_Pronunciation.insert(0, "Enter Pronunciation")
        Other_Language_Pronunciation.pack()
        
        Note = tk.Entry(AddCard, font=("Helvetica", 15), validate="key")
        Note.insert(0, "Write Notes Here")
        Note.pack()
        
        #Create the record button
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
        #Incriment number_of_cards_on_screen index one lower
        print("Pressed")
        
    def Randomzie_Card_Screen():
        # code goes here
        #Do something to shuffle cards around screen
        print("Pressed")
        
    def Show_another_Card():
        # code goes here
        #Incriment number_of_cards_on_screen index higher, check this index against the number of cards available
        #If number_of_cards_on_screen = Total number of cards, then do not do anything
        print("Pressed")
        
    # Set window size and title
    language_app = tk.Toplevel()
    language_app.title("Learning App")
    language_app.geometry("1200x800")
    width, height = 1200, 800
    
    #Setup grid for buttons
    for i in range(5):
        language_app.columnconfigure(i, weight=1, minsize=200)
    
    # Define a class for the flashcard
    class Flashcard:
        def __init__(self, x, y, Eng_Gloss, Other_Language_Pronunciation, Note, Picture, Recording):
            self.x = x
            self.y = y
            self.Eng_Gloss = Eng_Gloss
            self.Other_Language_Pronunciation = Other_Language_Pronunciation
            self.Note = Note
            self.Picture = Picture
            self.Recording = Recording
            
    # Initialize a list to store the flashcards
    flashcards = []
    
    def Display_flashcards
        ## This is where the flashcards pictures are displayed -- This will not work yet!!
        for i in range (20):
            # Get the flashcard you want to display
            flashcard = flashcards[i]
            
            # Create a label widget
            label = tk.Label(language_app)
            # Load the image of the flashcard using the Pillow library
            image = Image.open(flashcard.Picture)
            #Get the flashcard positioning
            x = (flashcard.x)
            y = (flashcard.y)
            # Convert the image to a PhotoImage object
            photo = ImageTk.PhotoImage(image)

            # Set the "image" option of the label to the PhotoImage object
            label.config(image=photo)
            label.image = photo

            # Pack the label widget to display it on the screen
            label.grid(row=x, column=y)
            
    # Function to play the sound
    def play_sound(flashcard):
        with wave.open(flashcard.Recording, 'rb') as f:
            # Use `subprocess` to play the sound
            subprocess.Popen(['aplay', flashcard.Recording])
            
    # Add the code to display a green border on the picture when the user selects the correct flashcard
    def on_flashcard_select(flashcard):
        play_sound(flashcard)
        border_color = 'green'
        picture.config(bd=20, relief='solid', bg=border_color)
        # Remove the border after 1 second
        frame.after(1000, lambda: picture.config(bd=0, relief='flat', bg=bg_color))
        # Randomly choose a different flashcard
        new_flashcard = random.choice(flashcards)
        picture.config(image=new_flashcard.Image)

    # Load the buttons
    plus_button = tk.Button(language_app, text="+", command=Show_another_Card, font=("Helvetica", 15), highlightthickness=5)
    minus_button = tk.Button(language_app, text="-", command=Remove_Card_Screen, font=("Helvetica", 15), highlightthickness=5)
    randomize_button = tk.Button(language_app, text="Randomize", command=Randomzie_Card_Screen, font=("Helvetica", 15), highlightthickness=5)
    CreateCard_button = tk.Button(language_app, text="Create Card", command=Open_New_Card, font=("Helvetica", 15), highlightthickness=5)
    
    plus_button.place(x=width-30, y=0, width=30, height=30)
    minus_button.place(x=width-30, y=30, width=30, height=30)
    randomize_button.place(x=width/2, y=0, height=30)
    CreateCard_button.place(x=0, y=0, height=30)
    
    


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
