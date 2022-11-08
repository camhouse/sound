import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open("C:\\Users\\camho\\Downloads\\PinkPanther30.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)

print(len(signal))

signal = np.fromstring(signal, int)


# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
plt.show()


