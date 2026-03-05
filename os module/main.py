import os

# os.mkdir("data")

for i in range(0, 100):
    # os.mkdir(f"data/Day{i+1}")
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")


