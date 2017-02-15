from essentia import *
from essentia.standard import *
from spectrum_analysis import *

def averageHarmonicity(sp_freq, sp_mag):
    ## Functions used
    _harm = Inharmonicity()

    ## Values used through out function
    ## declared for maximum compatibility
    i , j, result  = 0 , 0,  0
    limit_calc = len(sp_freq)
    raw_values = []

    ## Get inharmonicity values from spectrum frames
    ##
    for i in range(limit_calc):
        x_freq, x_mag = sp_freq[i], sp_mag[i]
        y = _harm(x_freq, x_mag)
        raw_values.append(y)
        i += 1

    ## Loop should only run for number of vectors present
    ##
    limit_agr = len(raw_values)
    for j in range(limit_agr):
        ## Sum all inharmonicity real values
        result += raw_values[j]
        j += 1

    ## Divide by total number of samples present for
    ## Average inharmonicity
    result = result / limit_agr

    return result
