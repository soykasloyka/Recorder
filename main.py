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
            text="🎙",
            font=('Arial', 120, "bold"),
            command=self.click_handler
        )
        self.button.pack()
        self.label = tkinter.Label(text='00:00:00')
        self.label.pack()
        self.recording = False
        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
        else:
            self.recording = True
            threading.Thread(target=self.record).start()

    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
            # input_device_index=9
        )

        frames = []
        start = time.time()