from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt

wcs_input_dict = {
    'CTYPE1': 'RA---TAN',
    'CUNIT1': 'deg',
    'CDELT1': -0.0002777777778,
    'CRPIX1': 1,
    'CRVAL1': 337.5202808,
    'NAXIS1': 1024,
    'CTYPE2': 'DEC--TAN',
    'CUNIT2': 'deg',
    'CDELT2': 0.0002777777778,
    'CRPIX2': 1,
    'CRVAL2': -20.833333059999998,
    'NAXIS2': 1024
}
wcs_helix_dict = WCS(wcs_input_dict)

# print(wcs_helix_dict)

wcs_helix_list = WCS(naxis=2)
wcs_helix_list.wcs.crpix=[1,1]
wcs_helix_list.wcs.crval=[337.5202808, -20.833333059999998]
wcs_helix_list.wcs.cunit=["deg","deg"]
wcs_helix_list.wcs.ctype = ["RA---TAN", "DEC--TAN"]
wcs_helix_list.wcs.cdelt=[-0.0002777777778, 0.0002777777778]

wcs_helix_list.array_shape=[1024,1024]

print(wcs_helix_list, "\n")

header_data_unit_list = fits.open('https://github.com/astropy/astropy-data/raw/6d92878d18e970ce6497b70a9253f65c925978bf/tutorials/celestial-coords1/tailored_dss.22.29.38.50-20.50.13_60arcmin.fits')

header_data_unit_list.info()

image= header_data_unit_list[0].data
header=header_data_unit_list[0].header

# print(header)

wcs_helix=WCS(header)

print(wcs_helix)

# fig=plt.figure(figsize=(10,10))
# ax=plt.subplot(projection=wcs_helix)
# plt.imshow(image, origin='lower', cmap='cividis', aspect='equal')
# plt.xlabel(r'RA')

# overlay = ax.get_coords_overlay('icrs')
# overlay.grid(color='white', ls='dotted')



fig=plt.figure(figsize=(10,10), frameon=False)
ax=plt.subplot(projection=wcs_helix)
ax.arrow(337, -21.2, 0, 0.1,
         head_width=0, head_length=0,
         fc='white', ec='white', width=0.003,
         transform=ax.get_transform('icrs'))
plt.text(336.98, -21.18, '0.1 deg',
         color='white', rotation=90,
         transform=ax.get_transform('icrs'))
ax.arrow(337, -21.2, 0.1, 0,
         head_width=0, head_length=0,
         fc='white', ec='white', width=0.003,
         transform=ax.get_transform('icrs'))
plt.text(337.1, -21.23, '0.25 deg',
         color='white', rotation=0,
         transform=ax.get_transform('icrs'))

plt.imshow(image, origin='lower', cmap='cividis', aspect='equal')

plt.xlabel(r'RA')
plt.ylabel(r'Dec')
plt.show()