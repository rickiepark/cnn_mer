import matplotlib.pyplot as plt
import wave
import glob
import scipy as sp

for fname in glob.glob("CAL500_wav/*.wav"):
    print(fname)

    wo = wave.open(fname, 'rb' )
    chunk = 65536
    data = sp.fromstring(wo.readframes(chunk), sp.int16)
    srate = wo.getframerate()
    nFFT = 1024
    window = sp.hamming(nFFT)

    fig, ax = plt.subplots(1)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax.set_axis_off()
    Pxx, freq, bins, im = ax.specgram(data,
                                      NFFT=nFFT,
                                      Fs=srate,
                                      noverlap=512,
                                      window=window)
    plt.savefig(fname.replace('wav', 'png'))
    plt.close(fig)
