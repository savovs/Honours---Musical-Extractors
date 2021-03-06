from essentia import *
from essentia.standard import *
from numpy import *
from matplotlib import pyplot as plt
from spectrum_analysis import *
from heightmap_generator import generateHeightmap
from inharmonicity import averageHarmonicity


## Declare our variables (filename etc.)
_f = "test_3.wav"
_r = "result_wav"
## Load audio in to Essentia container
loader = MonoLoader(filename = _f)
writer = MonoWriter(filename = _r)
audio = loader()

## Declare Functions
## Utility
_dcremoval = DCRemoval()
## Main Functions
key_func = KeyExtractor()
beat_func = RhythmExtractor2013()

hfc = HFC()
spectral_complexity = SpectralComplexity()
dyn_intensity = Intensity()
dyn_complexity = DynamicComplexity()


## Perform analysis
## Data manipulation methods
## aggregates spectra of frame size x, adds to an array
spectrum_frames = spectrumFrames(audio, 512, 256)
## uses spectra to generate frames of spectral peaks
## used by a number of functions
sp_freq, sp_mag = getSpectralPeaks(spectrum_frames)
## The aggregated spectrum, obtained by summing all spectra
aggregated_spectrum = meanSpectrum(spectrum_frames)
## DC offset must be eliminated to calculate inharmonicity
audio = _dcremoval(audio)

## Analyse input
k_key, k_scale, k_strength = key_func(audio)
b_bpm, b_ticks, b_confidence, b_estimates, b_bpm_intervals = beat_func(audio)
_hfc = hfc(aggregated_spectrum)
s_complexity = spectral_complexity(aggregated_spectrum)
d_intensity = dyn_intensity(audio)
d_complexity, d_loudness = dyn_complexity(audio)
s_inharmonicity = averageHarmonicity(sp_freq, sp_mag)



## NOT WORKING
## s_inharmonicity = averageHarmonicity(sp_freq, sp_mag)
## writer(b_ticks)
## generateHeightmap(513, 513, spectrum_frames, 128, 4)

print len(spectrum_frames)

print "key is: " + k_key, k_scale

print "BPM is : %d" % b_bpm

print "Confidence of BPM is : %d" % b_confidence

print "HFC is : %d" % _hfc

print "Spectral Complexity is : %d" % s_complexity

print "Dynamic Intensity is : %d" % d_intensity

print "Dynamic Complexity is : %d" % d_complexity

print "Loudness  : %d dB" % d_loudness

print "Inharmonicity is %d" % s_inharmonicity

