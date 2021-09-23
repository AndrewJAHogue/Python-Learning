import astropy.units as u
import astropy.coordinates as coord

coord.galactocentric_frame_defaults.set('latest')
# star HD 155967
icrs = coord.SkyCoord(ra=258.58356362*u.deg, dec=14.55255619*u.deg, radial_velocity=-16.1*u.km/u.s, frame='icrs')
# velocity of the sun in assumed GSR frame
v_sun = coord.Galactocentric().galcen_v_sun.to_cartesian()

gal = icrs.transform_to(coord.Galactic)
cart_data = gal.data.to_cartesian()
unit_vector = cart_data / cart_data.norm()

v_proj = v_sun.dot(unit_vector)

# add project of solar velocity to radial velocity = GSR radial velocity
rv_gsr = icrs.radial_velocity + v_proj
print(rv_gsr)