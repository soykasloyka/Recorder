import wave
import os
import time
import threading
import tkinter
import pyaudio


class VoiceRecorder():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.resizable(True, False)
        self.button = tkinter.Button(
            text="🎙️",
            font=('Arial', 120, "bold")
        )
        self.button.pack()
        self.root.mainloop()

VoiceRecorder()