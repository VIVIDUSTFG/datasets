import numpy as np

with open('./annotations.txt', 'r') as file:
    data = []
    for line in file:
        row = list(map(int, line.strip().split(',')))
        data.extend(row)

data_array = np.array(data)

np.save('gt.npy', data_array)

print("File converted to gt.npy with shape:", data_array.shape)
