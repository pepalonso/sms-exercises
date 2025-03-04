import numpy as np
from smstools.models import stft as STFT
from smstools.models import utilFunctions as UF
import matplotlib.pyplot as plt


(fs, x) = UF.wavread('../../../sounds/piano.wav')
w = np.hamming(1024)
N = 1024
H = 512
mX, pX = STFT.stftAnal(x, w, N, H)
y = STFT.stftSynth(mX, pX, w.size, H)

plt.figure(1, figsize=(9.5, 7))
plt.subplot(411)
plt.plot(np.arange(x.size)/float(fs), x, 'b')
plt.title('x (piano.wav)')
plt.axis([0,x.size/float(fs),min(x),max(x)])

plt.subplot(412)
# Size of X and Y must be 1 larger than the size of mX for flat shading
numFrames = int(mX[:,0].size) + 1
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(mX[0,:].size + 1)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.transpose(mX), shading = 'flat')
plt.title('mX, Hamming window, M=1024, N=1024, H=512')
plt.autoscale(tight=True)

plt.subplot(413)
# Size of X must be 1 larger than the size of np.diff(pX) (which has the Y axis size
# reduced by 1) for flat shading
numFrames = int(pX[:,0].size) + 1
frmTime = H*np.arange(numFrames)/float(fs)
binFreq = np.arange(pX[0,:].size)*float(fs)/N
plt.pcolormesh(frmTime, binFreq, np.diff(np.transpose(pX),axis=0), shading = 'flat')
plt.title('pX derivative, Hamming window, M=1024, N=1024, H=512')
plt.autoscale(tight=True)

plt.subplot(414)
plt.plot(np.arange(y.size)/float(fs), y,'b')
plt.axis([0,y.size/float(fs),min(y),max(y)])
plt.title('y')

plt.tight_layout()
plt.savefig('stft-system.png')
UF.wavwrite(y, fs, 'piano-stft.wav')
plt.show()



