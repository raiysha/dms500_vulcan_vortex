# Importing the required library
import numpy as np
import matplotlib.pyplot as plt

# Loading the data from the npy file
behavData = np.load("behavData.npy")

# Creating a figure with specific dimensions and setting font
plt.figure(figsize=(8, 16))
plt.rc('font', family='Arial')

# First subplot: Behavioural Sessions BEFORE FIX
plt.subplot(1, 2, 1)
plt.plot(behavData[:, 4], behavData[:, 1], 'k.', markersize=10)  # Adjust markersize as needed
plt.xlabel('Number of Trials')
plt.ylabel('Session Number')
plt.title('Behavioural Sessions: BEFORE FIX')

# Filtering the data to remove JUNK trials
valid_trials = np.isin(behavData[:, 5], [0, 6])
behavData = behavData[valid_trials]

# Second subplot: Behavioural Sessions AFTER FIX
plt.subplot(1, 2, 2)
plt.plot(behavData[:, 4], behavData[:, 1], 'r.', markersize=10)  # Adjust markersize as needed
plt.xlabel('Number of Trials')
plt.ylabel('Session Number')
plt.title('Behavioural Sessions: AFTER FIX')
plt.suptitle('Filtering out Bad Trials', fontsize=16, color=[0, 0, 1], x=0.5, y=0.95)

# Counting the number of trials per session
unique_sessions = np.unique(behavData[:, 1])
trialCounts = np.zeros((len(unique_sessions), 3))
for i, session in enumerate(unique_sessions):
    trialCounts[i, 2] = np.sum(behavData[:, 1] == session)

print('done.')
plt.show()

# Calculate trial counts for "GOOD" trials
# Initialize an empty list to store trial counts for each unique value in column 2 of behavData
trialCounts = []
for ss in np.unique(behavData[:, 1]):  # Iterate through unique values in the 2nd column (index 1)
    # Count how many times each unique value appears in column 2 and append to trialCounts
    trialCounts.append(np.sum(behavData[:, 1] == ss))
# Convert trialCounts to a NumPy array and reshape for columnar structure
trialCounts = np.array(trialCounts).reshape(-1, 1)
# Adding an extra column to trialCounts for the next steps (placeholder)
trialCounts = np.hstack((np.zeros((trialCounts.shape[0], 2)), trialCounts))


# Simple "Demographics"
behavSummary = np.zeros((6, 2))  # Initialize behavSummary matrix with zeros

# Number of sessions for each monkey (M1 and M2)
behavSummary[0, :] = [len(np.unique(behavData[behavData[:, 0] == 1, 1])),
                      len(np.unique(behavData[behavData[:, 0] == 2, 1]))]

# Number of trials for each monkey (M1 and M2)
behavSummary[1, :] = [len(behavData[behavData[:, 0] == 1, 0]),
                      len(behavData[behavData[:, 0] == 2, 0])]

# Number of passive trials > 3 for each monkey
behavSummary[2, :] = [len(behavData[(behavData[:, 0] == 1) & (behavData[:, 6] > 3), 0]),
                      len(behavData[(behavData[:, 0] == 2) & (behavData[:, 6] > 3), 0])]

# Number of correct passive trials for each monkey
behavSummary[3, :] = [len(behavData[(behavData[:, 0] == 1) & (behavData[:, 6] > 3) & (behavData[:, 5] == 0), 0]),
                      len(behavData[(behavData[:, 0] == 2) & (behavData[:, 6] > 3) & (behavData[:, 5] == 0), 0])]

# Number of active trials < 4 for each monkey
behavSummary[4, :] = [len(behavData[(behavData[:, 0] == 1) & (behavData[:, 6] < 4), 0]),
                      len(behavData[(behavData[:, 0] == 2) & (behavData[:, 6] < 4), 0])]

# Number of correct active trials for each monkey
behavSummary[5, :] = [len(behavData[(behavData[:, 0] == 1) & (behavData[:, 6] < 4) & (behavData[:, 5] == 0), 0]),
                      len(behavData[(behavData[:, 0] == 2) & (behavData[:, 6] < 4) & (behavData[:, 5] == 0), 0])]

# Displaying summaries

print("-------------------------------------------------------------------------------------------")
print(f"Total Number of Sessions (M1): {behavSummary[0, 0]}")
print(f"Total Number of Sessions (M2): {behavSummary[0, 1]}")
print(f"Total Number of Trials (M1): {behavSummary[1, 0]}")
print(f"Total Number of Trials (M2): {behavSummary[1, 1]}")
print("-------------------------------------------------------------------------------------------")
print(f"Total Number of Passive Trials (M1): {behavSummary[2, 0]}")
print(f"Total Number of Passive Trials (M2): {behavSummary[2, 1]}")
print(f"Total Number of Passive Trials (Correct) (M1): {behavSummary[3, 0]} "
      f"({behavSummary[3, 0]/behavSummary[2, 0]*100}%)")
print(f"Total Number of Passive Trials (Correct) (M2): {behavSummary[3, 1]} "
      f"({behavSummary[3, 1]/behavSummary[2, 1]*100}%)")
print("-------------------------------------------------------------------------------------------")
print(f"Total Number of Active Trials (M1): {behavSummary[4, 0]}")
print(f"Total Number of Active Trials (M2): {behavSummary[4, 1]}")
print(f"Total Number of Active Trials (Correct) (M1): {behavSummary[5, 0]} "
      f"({behavSummary[5, 0]/behavSummary[4, 0]*100}%)")
print(f"Total Number of Active Trials (Correct) (M2): {behavSummary[5, 1]} "
      f"({behavSummary[5, 1]/behavSummary[4, 1]*100}%)")

