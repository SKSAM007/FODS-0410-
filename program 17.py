import numpy as np
likes = np.array([10, 20, 30, 20, 10, 40, 50, 10, 20, 30, 40, 50, 20, 10])
unique_likes, counts = np.unique(likes, return_counts=True)
print("Frequency distribution of likes:")
for likes, frequency in zip(unique_likes, counts):
    print(f"Likes: {likes}, Frequency: {frequency}")
