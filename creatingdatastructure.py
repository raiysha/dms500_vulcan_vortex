import numpy as np
import pandas as pd

# Load behavData from a .npy file
behavData = np.load('behavData.npy')

# Convert the NumPy array to a pandas DataFrame

columns = [
    'Animal', 'Session', 'OtherColumn1', 'OtherColumn2', 'TrialNumber',
    'CorrectIncorrect', 'Block Number', 'Condition Number', 'ReactionTime',
    'OtherColumn5', 'Stim1Presented', 'Stim2Presented', 'Expectation', 'RepeatOrAlternation',
    'ActiveOrPassive', 'RightOrLeft', 'OtherColumn3', 'OtherColumn4', 'OtherColumn5', 'OtherColumn6'
]

behavData_df = pd.DataFrame(behavData, columns=columns)

# Creating evdata structure
evdata = pd.DataFrame()
evdata['trialNumber'] = behavData_df['TrialNumber']
evdata['animal'] = behavData_df['Animal']
# Assuming RepeatOrAlternation == 1 indicates a 'repeat' action
evdata['actual'] = np.where(behavData_df['RepeatOrAlternation'] == 1, 1, -1)
evdata['session'] = behavData_df['Session']
# Assuming CorrectIncorrect == 0 indicates a correct choice
evdata['cor'] = (behavData_df['CorrectIncorrect'] == 0).astype(int)
evdata['active'] = np.where(behavData_df['ActiveOrPassive'] == 1, 1, -1)
evdata['stim1'] = np.where(behavData_df['Stim1Presented'] == 1, 1, -1)
evdata['stim2'] = np.where(behavData_df['Stim2Presented'] == 1, 1, -1)
evdata['reactiontime'] = behavData_df['ReactionTime']
evdata['expect'] = behavData_df['Expectation']
evdata['correctRight'] = behavData_df['RightOrLeft']
evdata['date_lastModified'] = pd.to_datetime('today')

# Relabel evdata.expect
evdata['expect'] = evdata['expect'].replace({1: 1, 2: -1, 3: 0})


# Initialize the variables as new columns
evdata['congruent_n1'] = 0
evdata['congruent_n2'] = 0
evdata['congruent_n3'] = 0

# Initialize the variables for previous trial stimulus comparison
evdata['prevtrial_n1'] = 0
evdata['prevtrial_n2'] = 0
evdata['prevtrial_n3'] = 0

# Calculate congruency for n-1, n-2, and n-3
evdata.loc[1:, 'congruent_n1'] = (evdata['correctRight'].iloc[1:].values == evdata['correctRight'].iloc[:-1].values).astype(int)
evdata.loc[2:, 'congruent_n2'] = (evdata['correctRight'].iloc[2:].values == evdata['correctRight'].iloc[:-2].values).astype(int)
evdata.loc[3:, 'congruent_n3'] = (evdata['correctRight'].iloc[3:].values == evdata['correctRight'].iloc[:-3].values).astype(int)

# Calculate if previous STIM2 is the same as current STIM1 for n-1, n-2, and n-3
evdata.loc[1:, 'prevtrial_n1'] = (evdata['stim2'].iloc[:-1].values == evdata['stim1'].iloc[1:].values).astype(int)
evdata.loc[2:, 'prevtrial_n2'] = (evdata['stim2'].iloc[:-2].values == evdata['stim1'].iloc[2:].values).astype(int)
evdata.loc[3:, 'prevtrial_n3'] = (evdata['stim2'].iloc[:-3].values == evdata['stim1'].iloc[3:].values).astype(int)

# Initialise columns for latent expectation repetition program

evdata['p_rep'] = np.nan
evdata['log_p_rep'] = np.nan
evdata['choseRepeat'] = np.nan

print(evdata.columns)