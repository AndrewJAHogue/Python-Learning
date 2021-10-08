import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.coordinates import SkyCoord, Distance
from astropy.io import fits
from astropy.table import QTable
from astropy.utils.data import download_file

from astroquery.gaia import Gaia
Gaia.ROW_LIMIT = 10000

ngc188_center_deg = SkyCoord(12.11*u.deg, 86.26*u.deg, frame = 'icrs')
ngc188_center_string = SkyCoord('00h48m26.4s', '85d15m36s', unit=(u.hour, u.deg), frame = 'icrs')

print("ngc188_center_deg is: \n", ngc188_center_deg, "\nAnd ngc188_center_string is: \n", ngc188_center_string)

ngc188_center_from_name = SkyCoord.from_name('NGC 188')
print("\nThe from_name function returns: ", ngc188_center_from_name)

print(ngc188_center_string.ra, ngc188_center_deg.dec)

print(type(ngc188_center_string.ra), type(ngc188_center_deg.dec))

print(ngc188_center_string.ra.to(u.hourangle), ngc188_center_deg.ra.to(u.radian), ngc188_center_from_name.ra.to(u.degree))

print("\n",ngc188_center_string.ra.hour, ngc188_center_string.ra.radian, ngc188_center_string.ra.degree)

print(ngc188_center_string.ra.to_string(unit=u.hourangle, sep=':', pad=True))
print(ngc188_center_string.dec.to_string(unit=u.hourangle, sep=':', pad=True))

# Query Gaia Archive

job = Gaia.cone_search_async(ngc188_center_string, radius=0.5*u.deg)
ngc188_table = job.get_results()

ngc188_table = ngc188_table[ngc188_table['phot_g_mean_mag']<19*u.mag]

cols = ['source_id',
    'ra',
    'dec',
    'parallax',
    'pmra',
    'pmdec',
    'radial_velocity',
    'phot_g_mean_mag',
    'phot_bp_mean_mag',
    'phot_rp_mean_mag']
ngc188_table[cols].write('gaia_results.fits', overwrite=True)
len(ngc188_table)
# print(ngc188_table['ra'])
# print(ngc188_table['dec'])
ngc188_gaia_coords = SkyCoord(ngc188_table['ra'], ngc188_table['dec'])
# print(ngc188_gaia_coords)

print(ngc188_center_from_name.to_string(style="hmsdms", sep=":", precision=1))

print(ngc188_gaia_coords.separation(ngc188_center_from_name))

ngc188_center_3d = SkyCoord(ngc188_center_from_name.ra.to(u.degree), ngc188_center_from_name.dec.to(u.degree), distance=1.96*u.kpc)
parallax_snr = ngc188_table['parallax'] / ngc188_table['parallax_error']
ngc188_table_3d = ngc188_table[parallax_snr > 10]
print(ngc188_table_3d)
Distance(parallax=1*u.mas)
ngc188_parallax = ngc188_table_3d.filled()
gaia_dist =  Distance(parallax=ngc188_parallax['parallax'])
ngc188_coords_3d = SkyCoord(ra=ngc188_table_3d['ra'],dec=ngc188_table_3d['dec'],distance=gaia_dist)
print(ngc188_coords_3d)