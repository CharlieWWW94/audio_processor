
import _soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np 


#returns the number of samples in file, and sample rate( default: 22050)
sample_num, sample_rate =librosa.load('audio_files/voice.wav')
print(sample_num)
#returns evenly spaced values for number of samples. sample rate is number of sampples, without the division below we just get the acccumulatiing number of samples on the x axis.
#By dividing the length of the array by number of samples per second, we get time in seconds. 
time = np.arange(0, len(sample_num)) / sample_rate

#ax is the axes of the graph. Not entirely sure what fig is...
fig, ax = plt.subplots()
#Plots the values across 2 dimensions: time on the X, amplitude on the y
ax.plot(time, sample_num)
#Adds labels to graph
ax.set(title='original signal', xlabel = 'Time (s)', ylabel = 'Sound Amplitude')
plt.show()

