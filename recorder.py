import sounddevice as sd
from scipy.io.wavfile import write


class audioRecorder:
    '''
    Class that when instantiated can record live audio (currently only for a hardcoded length of time.)
    This class also saves teh file to .wav format with a file name from user input.
    '''
    def __init__(self):
        #Introduces recording length and sample rate
        self.duration = 20
        self.sample_rate = 22050
    
    def record(self):
        #Allows user to record audio using their device's microphone
        self.my_recording = sd.rec(int(self.duration * self.sample_rate), samplerate= self.sample_rate, channels=2)
        sd.wait()
        return self.my_recording
    def save(self, rec_name, recording=None):
        #Saves the recording to the new_audio folder.
        if recording:
            rec_to_save = recording
        else:
            rec_to_save = self.my_recording
        #This writes the recorded audio to a .wav file
        write(f'new_audio/{rec_name}.wav', rate=self.sample_rate, data=rec_to_save)

#This code was used for testing the functionality of the libraries. Only runs if __name__ == "__main__"

if __name__ == "__main__":
    recorder = audioRecorder()
    recorder.record()
    recorder.save(rec_name='test_audio')