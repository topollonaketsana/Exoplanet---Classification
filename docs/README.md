# Kepler Exoplanet Search Results

This repository is the Kepler Exoplanet Search Results dataset, which includes key terms and columns. The dataset provides information about various potential exoplanets and fully identified exoplanets by the mission.

## Dataset Overview

The dataset is available in a CSV file named `cumulative.csv` on `..data` path. Each row in the dataset represents a particula exoplanet, with various attributes describing its characteristics and the observations made by the Kepler Space Telescope.

### Key Terms and Columns

Here are some of the key columns in the dataset and their descriptions:

- **kepid**: The Kepler ID of the star hosting a particula exoplanet.
- **kepoi_name**: The Kepler Object of Interest (KOI) identifier for the single exoplanet.
- **kepler_name**: The official name of the confirmed exoplanet.
- **koi_disposition**: The status of the exoplanet (e.g., 'CONFIRMED', 'FALSE POSITIVE').
- **koi_pdisposition**: The preliminary status of the exo.
- **koi_score**: A score indicating the likelihood that the potential exoplanets is a true exoplanet.
- **koi_fpflag_nt**: A flag indicating if the potential exo is a false positive based on centroid motion.
- **koi_fpflag_ss**: A flag indicating if the potential exo is a false positive based on significant secondary events.
- **koi_fpflag_co**: A flag indicating if the potential exo is a false positive based on ephemeris matching with a known false positive.

### Stellar Parameters

- **koi_steff**: The effective temperature of the host star.
- **koi_steff_err1**: The upper error bound for the effective temperature.
- **koi_steff_err2**: The lower error bound for the effective temperature.
- **koi_slogg**: The logarithm of the surface gravity of the host star.
- **koi_slogg_err1**: The upper error bound for the surface gravity.
- **koi_slogg_err2**: The lower error bound for the surface gravity.
- **koi_srad**: The radius of the host star.
- **koi_srad_err1**: The upper error bound for the stellar radius.
- **koi_srad_err2**: The lower error bound for the stellar radius.

### Positional Information

- **ra**: The right ascension of the host star.
- **dec**: The declination of the host star.

### Photometric Information

- **koi_kepmag**: The Kepler magnitude of the host star, indicating its brightness as observed by the Kepler Space Telescope.
