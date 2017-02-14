from essentia import *
from essentia.standard import *
import numpy as np

def meanSpectrum(signal, frameSize, hopSize):
    # Signal must be loaded in to essentia first
    # Declaring essentia function(s)
    spec = Spectrum()

    # Declaring Variables, container for frames
    # and length of the input signal
    i , j = 0, 1
    number_of_frames = 0
    limit = len(signal)
    frames = []

    # Run through the signal and extract spectrum at provided intervals
    for i in range(limit):
        if i + frameSize > limit:
            number_of_frames = len(frames)
            break
        else:
            print "Total number of sample = %d" % limit
            print "Samples processed = %d" % i
            x = signal[i : i + hopSize]
            f = spec(x)
            frames.append(f)
            i = i + hopSize

    raw_mean_spec = frames[0]

    for j in range(number_of_frames):
        raw_mean_spec += frames[j]

    raw_mean_spec = raw_mean_spec

    return  raw_mean_spec
