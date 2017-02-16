from PIL import Image, ImageDraw
from numpy import interp

def generateHeightmap(sizeX, sizeY, spectrumFrames, samplesPerFrame, real2smooth):
    ## Declare vars
    ## Create an image
    size = (sizeX, sizeY)
    heightmap_raw = Image.new('L', size, color=0)
    _heightmap = ImageDraw.Draw(heightmap_raw)

    ## Pixel limit - 1 to make working with audio easier
    ## Frames will take form 2n + 1 x 2n +1 for unity terrain error compensation
    iterator_limit = sizeX - 1
    ## How often should we plot sample value
    sample_limit = iterator_limit / real2smooth

    number_of_frames = len(spectrumFrames)
    frames_required = sizeX / real2smooth
    FrameHopSize = number_of_frames / frames_required
    SampleHopSize = iterator_limit / samplesPerFrame

    ## Create array of pixel values
    final_spectrum_columns = []

    ## Maps spectrum to be suitable for pixelisation
    for k in range(frames_required):
        spectrum_column = []
        currentFrame = spectrumFrames[k * FrameHopSize]

        for t in range(sample_limit):
            currentValue = currentFrame[t]
            spectrum_column.append(currentValue)

        final_spectrum_columns.append(spectrum_column)


    ## Remember last used spectrum, which has been converted in to column of pixels
    _previous_column = []


    ## Generate Map
    for i in range(iterator_limit): ## X axis
        if i % real2smooth == 0:
            _column = final_spectrum_columns[i / real2smooth]
        else:
            _column = _previous_column

        for j in range(iterator_limit): ## Y axis
            currentPoint = (i, j)

            if i % real2smooth != 0:
                ## Plot Spectrum
                if(j % SampleHopSize == 0):
                    currentIndex = j / SampleHopSize
                    val = _column[currentIndex]
                    val = interp(val, [0,1],[0,255])
                    _heightmap.putpixel(currentPoint, val)
                    _previous_column = _column


            else:
                ## Do lerp work
                ## Lerp between current frame and previous frame
                _previous_column = _column



    ## Save to file
    heightmap_raw.save("Result.png")

