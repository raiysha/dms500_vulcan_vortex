import numpy as np
import scipy.io as sio

# Load the data from the MATLAB file
behavData = sio.loadmat("DMS500_behavData.mat")

# Accessing specific data
data2 = behavData['MegaBehav']
data = behavData['trialCounts']

# Saving the data to an .npy file
np.save("behavData.npy", data2)

# Defining session names
dms500sessionNames = [
    'DMS_500-Vortex-01-17-2018.mat',
    'DMS_500-Vortex-01-18-2018.mat',
    'DMS_500-Vortex-01-23-2018.mat',
    'DMS_500-Vortex-01-24-2018.mat',
    'DMS_500-Vortex-01-25-2018.mat',
    'DMS_500-Vortex-01-26-2018.mat',
    'DMS_500-Vortex-01-29-2018.mat',
    'DMS_500-Vortex-01-30-2018.mat',
    'DMS_500-Vortex-02-01-2018(02).mat',
    'DMS_500-Vortex-02-02-2018.mat',
    'DMS_500-Vortex-02-06-2018.mat',
    'DMS_500-Vortex-02-07-2018(05).mat',
    'DMS_500-Vortex-02-09-2018.mat',
    'DMS_500-Vortex-02-14-2018.mat',
    'DMS_500-Vortex-02-16-2018(02).mat',
    'DMS_500-Vulcan-03-12-2018(01).mat',
    'DMS_500-Vulcan-03-16-2018.mat',
    'DMS_500-Vulcan-03-21-2018.mat',
    'DMS_500-Vulcan-03-23-2018(02).mat',
    'DMS_500-Vulcan-03-26-2018(02).mat',
    'DMS_500-Vulcan-03-27-2018.mat',
    'DMS_500-Vulcan-03-28-2018.mat',
    'DMS_500-Vulcan-03-29-2018(00).mat',
    'DMS_500-Vulcan-04-09-2018.mat',
    'DMS_500-Vulcan-04-10-2018(00).mat',
    'DMS_500-Vulcan-04-12-2018.mat',
    'DMS_500-Vulcan-04-13-2018(01).mat',
    'DMS_500-Vulcan-05-08-2018(01).mat',
    'DMS_500-Vulcan-05-09-2018.mat'
    ]

# Define d500specs
d500specs = {'upperLim': 0.66, 'lowerLim': 0.33}