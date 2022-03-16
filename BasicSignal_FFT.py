#   Python program 
        # 1. to generate basic synthetic sinusoidal wave 
        # 2. to plot the sinusoidal signal
        # 3. to compute Fourier spectrum using FFT
        # 4. plot double side spectrum
        # 5. plot one side spectrum
        
# %%  import necessary libraries

from matplotlib import pyplot as plt
import numpy as np


# %%  Basic signal generation

#  specifications to generate signal
sampleRate = 1000  # # samples
timeMax = 1        # Seconds
maxAmp=1           # Max amplitude

#   construct a time vector  
discT = np.linspace(0, timeMax, sampleRate * timeMax)

#   specify the maximum frequency in the signal
f = 10              # Hertz
 
#  construct a  sinusoidal signal 
signal = maxAmp*np.sin((2 * np.pi)*discT * f)

plt.plot(discT, signal)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()


# %%  1.  computation of spectrum using FFT 

from scipy.fft import fft, fftfreq
#  signal with frequency of 20 Hz
f = 20
signal2 = maxAmp*np.sin((2 * np.pi)*discT * f)
N = sampleRate * timeMax

plt.figure()
plt.plot(discT, signal2)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()


# using FFT to compute spectrum
yf = fft(signal2)
# constructing frequency vector 
xf = fftfreq(N, 1 / sampleRate)
# plot the double side spectrum
plt.figure()
plt.plot(xf, np.abs(yf))
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.show()


# display one side spectrum
from scipy.fft import rfft, rfftfreq

# yf = rfft(sig1Norm)
yf = rfft(signal2)
xf = rfftfreq(N, 1 / sampleRate)

plt.plot(xf, np.abs(yf))
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.show()

#   2.  computation of spectrum using FFT 

#  signal with frequency of 200 Hz
f = 200
signal2 = maxAmp*np.sin((2 * np.pi)*discT * f)
N = sampleRate * timeMax

plt.figure()
plt.plot(discT, signal2)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()


# using FFT to compute spectrum
yf = fft(signal2)
# constructing frequency vector 
xf = fftfreq(N, 1 / sampleRate)
# plot the double side spectrum
plt.figure()
plt.plot(xf, np.abs(yf))
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.show()


# display one side spectrum
from scipy.fft import rfft, rfftfreq

# yf = rfft(sig1Norm)
yf = rfft(signal2)
xf = rfftfreq(N, 1 / sampleRate)

plt.plot(xf, np.abs(yf))
plt.xlabel('frequency')
plt.ylabel('magnitude')
plt.show()

