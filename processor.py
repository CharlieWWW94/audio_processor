
import soundfile as sf
from playsound import playsound
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np 



class AudioProcessor:
    '''
    Takes the file path of an audio file, creates a visual waveform
    and saves it as a png. 
    '''
    def __init__(self, audio_file):
        self.sample_num, self.sample_rate = librosa.load(audio_file)
        self.time = np.arange(0, len(self.sample_num)) / self.sample_rate
        self.fig, self.ax = plt.subplots()
        self.ax.set(title=audio_file, xlabel = 'Time (s)', ylabel = 'Sound Amplitude')
        self.ax.plot(self.time, self.sample_num)
        plt.savefig('wave_graphs/new_wave.png')
    
    def alter_pitch(self, change, name):
        #Change the pitch of the previously given/recorded audio file, and reproduces the audio.
        self.dropped = librosa.effects.pitch_shift(self.sample_num, sr=self.sample_rate, n_steps=change)
        sf.write(f'new_audio/{name}.wav', self.dropped, self.sample_rate)
        playsound(f'new_audio/{name}.wav')




#OLD CODE - Here I was working out exactly how to convert audio to dataframe and create a figure with it.
# #returns the number of samples in file, and sample rate( default: 22050)
# sample_num, sample_rate =librosa.load('audio_files/voice.wav')

# '''sample_num returns evenly spaced values for accumulating number of samples.  
# without the division below we just get the acccumulatiing number of samples overall on the x axis.
# By dividing the length of the array by overall number of samples, we get time in seconds.'''

# time = np.arange(0, len(sample_num)) / sample_rate

# #ax is the axes of the graph. Not entirely sure what fig is...
# fig, ax = plt.subplots()
# #Plots the values across 2 dimensions: time on the X, amplitude on the y
# ax.plot(time, sample_num)
# #Adds labels to graph
# #ax.set(title='original signal', xlabel = 'Time (s)', ylabel = 'Sound Amplitude')
# plt.savefig('wave_graphs/new_wave.png')
# plt.show()
