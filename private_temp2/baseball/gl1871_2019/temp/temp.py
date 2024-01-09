import numpy as np
import nfft
from pylab import plot,show,scatter

x = -0.5 + np.random.rand(1000)
f = np.sin(10 * 2 * np.pi * x)
N = 1000

###print(x,f)
###q=nfft.nfft(x, f, N)
q=nfft.nfft_adjoint(x, f, N)
###scatter(x,f)
toplot=abs(q)**2
plot(toplot)
for val in range(len(q)):
  print(val/len(q),toplot[val])

show()