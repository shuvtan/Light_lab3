import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

def readIntensity(name, name2, lamp, surface):
	image = iio.imread(name)
	background = image[510:1060, 1140:1395, 0:3].swapaxes(0, 1)
	cut = image[510:1060, 1150:1330, 0:3].swapaxes(0, 1)
	rgb = np.mean(cut, axis=(0))
	luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]
	
	plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))
	
	fig = plt.figure(figsize=(10, 5), dpi=200)
	plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
	plt.xlabel('Номер пикселя')
	plt.ylabel('Яркость')
	    
	plt.minorticks_on()
	
	plt.plot(rgb, label=['r', 'g', 'b'])
	plt.plot(luma, 'w', label='I')
	plt.legend()
	    
	plt.imshow(background, origin='lower')
	plt.savefig(name2)

	return luma
