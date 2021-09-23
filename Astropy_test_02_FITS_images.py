import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# you can import small parts of modules using from [module] import [what you want]
from astropy.io import fits
# download FITS file
from astropy.utils.data import download_file
image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)

hdu_list = fits.open(image_file)
# hdu_list.info()

# stores data as 2D numpy array
image_data = hdu_list[0].data

print(type(image_data))
print(image_data.shape)

# closing the file or not doesn't seem to do anything? I assume it just returns file permissions
hdu_list.close()

# ------------------------SHORTCUT----------------------------
# image_data = fits.getdata(image_file)
# print(type(image_data))
# print(image_data.shape)
def PrintImage():
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.show()

print('Min:', np.min(image_data), '\nMax:', np.max(image_data), '\nMean:', np.mean(image_data), '\nStdev:', np.std(image_data))

#Making a histogram
# what does this do?
print(type(image_data.flatten()))

def PrintHist():
    histogram = plt.hist(image_data.flatten(), bins='auto')
    plt.show()


def PrintLogImage():
    from matplotlib.colors import LogNorm
    plt.imshow(image_data, cmap='gray', norm=LogNorm())

    cbar = plt.colorbar(ticks=[5.e3,1.e4,2.e4])
    cbar.ax.set_yticklabels(['5,000','10,000','20,000'])

    plt.show()
PrintHist()
