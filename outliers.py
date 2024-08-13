import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset=[11,10,12,14,12,15,14,13,15,102,12.14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
outliers = []

 
# 1st Method(using z-score)
def detect_out(data):
    threshold = 3
    mean = np.mean(data)
    std = np.std(data)
 
    for i in data:
        z_score = (i - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers

print(detect_out(dataset))

sns.boxplot(dataset)
plt.show()


# 2nd Method(using percentile)
dataset1 = sorted(dataset)
dataset1 = np.sort(dataset)
Q1, Q3 = np.percentile(dataset1, [25, 75])
IQR = Q3 - Q1
MinIQR = Q1 - 1.5 * IQR
MaxIQR = Q3 + 1.5 * IQR
for i in dataset1:
    if i > MaxIQR or i < MinIQR:
        outliers.append(i)
print(outliers)

sns.boxplot(dataset)
plt.show()
