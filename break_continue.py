#break

for i in range(12):
    print("5 X", i, "=", 5 * (i+1))
    if i == 10:
        break

print("Loop ended")

#continue

for i in range(12):
    if i == 10:
        continue
    print("5 X", i + 1, "=", 5 * (i+1))