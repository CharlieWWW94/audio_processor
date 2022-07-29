from processor import AudioProcessor
import tkinter as tk
import PIL.Image
import PIL.ImageTk
from recorder import audioRecorder

class Gui(tk.Tk):
    '''
    Class for graphical user interfact - inherits from Tk.
    An OOP approach allows for the dynamic editing of visuals, without
    having to be concerned about the event loop and global variables.
    '''
    def __init__(self):
        #creates a window and the basic layout of GUI
        super().__init__()
        self.title('Python Audio Processor')
        self.record_label = tk.Label(text='Record audio file. Name:')
        self.name = tk.Entry(width=40)
        self.record_btn = tk.Button(text='Record', command=self.record_audio)
        self.path_label = tk.Label(text='Enter .wav for processing:')
        self.path_entry = tk.Entry(width=40)
        self.submit = tk.Button(text='Submit', command=self.make_image)
        
        self.path_label.grid(row=1, column=0, sticky='w')
        self.path_entry.grid(row=1, column=1, sticky='w')
        self.submit.grid(row=1, column=2, columnspan=2)
        self.record_label.grid(row=2, column=0, sticky="w")
        self.name.grid(row=2, column=1, sticky="w")
        self.record_btn.grid(row=2, column=2, sticky="w")
    
    def make_image(self):
        #Takes the file path of a .wav and creates a visual waveform
        if self.path_entry.get():
            file_path = self.path_entry.get()
        else:
            file_path = f'new_audio/{self.name.get()}.wav'
        self.processor = AudioProcessor(file_path)
        self.update_gui()
    
    def update_gui(self):
        #Adds the visual waveform to the GUI and button to drop pitch of audio
        new_image = PIL.Image.open('wave_graphs/new_wave.png')
        image_ready = PIL.ImageTk.PhotoImage(new_image)
        
        self.graph = tk.Label(self, image=image_ready)
        self.graph.image = image_ready
        self.graph.grid(row=3, column=0, columnspan=3)
        
        self.slide = tk.Scale(from_=5, to=-5)
        self.slide.grid(row=4, column=0, columnspan=3)

        self.drop_button = tk.Button(text='Change pitch.', command=self.alter_audio)
        self.drop_button.config(width=80, height=2)
        self.drop_button.grid(row=5, column=0, columnspan=3)
    
    def record_audio(self):
        #Allows users to record audio and then display the soundwave in the GUI
        self.record_btn = tk.Button(text='Record', command=self.record_audio, bg='RED')
        audio_recorder = audioRecorder()
        audio_recorder.record()
        self.record_btn = tk.Button(text='Record', command=self.record_audio, bg='WHITE')
        audio_recorder.save(rec_name=self.name.get())
        self.make_image()
    
    def alter_audio(self):
        #Initiates audio processer pitch manipulation.

        if self.name.get():
            new_name = self.name.get()
        else:
            new_name = 'pitch_edited_file'
        self.processor.alter_pitch(change=self.slide.get(), name=new_name)




if __name__ == "__main__":
    app = Gui()
    app.mainloop()

