from astropy.io import fits
import numpy as np

fits_file = 'k4v7t030829t153435_i.fts'

# Open with memory mapping for large file
with fits.open(fits_file, memmap=True) as hdul:
    hdul.info()  # Show HDU structure
    header = hdul[0].header
    image_data = hdul[0].data  # Shape (128, 2048, 2048)

    # Print key header info
    print("Header keys (first 10):")
    for key, value in list(header.items())[:10]:
        print(f"{key}: {value}")
    print("\nData shape:", image_data.shape)
    print("Data type:", image_data.dtype)
    print("Wavelength (if available):", header.get('WAVELNTH', 'Not specified'))
    print("Observation date:", header.get('DATE-OBS', 'Not specified'))
