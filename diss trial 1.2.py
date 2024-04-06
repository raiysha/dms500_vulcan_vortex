# importing the required modules
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np


# loading the data from v4 mega matrix vulcan
vulcanV4 = sio.loadmat("megamatrixvulcan.mat")
data1 = vulcanV4['V4_megaMatrix500NoScrubs']

# loading the data from TE mega matrix vulcan
vulcanTE = sio.loadmat("noscrubsvulcan.mat")
data2 = vulcanTE['TE_megaMatrix500NoScrubs']

# loading data from TE mega matrix vortex
vortexTE = sio.loadmat("TEmegamatrixvortex.mat")
data3 = vortexTE['TE_megaMatrix500NoScrubs']

# loading data from v4 mega matrix vortex
vortexV4 = sio.loadmat("V4megamatrixvortex.mat")
data4 = vortexV4['V4_megaMatrix500NoScrubs']

# creating a dictionary with the values of vulcanV4 as an array
i = 1  # assigning i the value the dictionary is to begin at

vulcan_v4 = {}
for i, array in enumerate(data1):
    vulcan_v4[i] = array
np.save("vulcan_v4.npy", vulcan_v4)
vulcan_v4.shape()

# creating a dictionary with the values of vulcanTE as an array
i = 1  # assigning i the value the dictionary is to begin at

vulcan_TE = {}
for i, array in enumerate(data2):
    vulcan_TE[i] = array
np.save("vulcan_TE.npy", vulcan_TE)
# creating a dictionary with the values of vortexTE as an array
i = 1  # assigning i the value the dictionary is to begin at

vortex_v4 = {}
for i, array in enumerate(data3):
    vortex_v4[i] = array
np.save("vortex_v4.npy", vortex_v4)
# creating a dictionary with the values of vortexV4 as an array
i = 1  # assigning i the value the dictionary is to begin at

vortex_TE = {}
for i, array in enumerate(data4):
    vortex_TE[i] = array
np.save("vortex_TE.npy", vortex_TE)



