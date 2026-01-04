import time
# timestamp = time.strftime("%H:%M:%S")
# print("Good morning sir, the time is:", timestamp)
timestamp = time.strftime("%H")
hour = int(timestamp)
print(hour)

if hour < 12:
    print("Good morning sir, the time is: ", timestamp)
elif hour >= 12 and hour < 18:
    print("Good afternoon sir, the time is: ", timestamp)
elif hour >= 18 and hour < 21:
    print("Good evening sir, the time is: ", timestamp)
else:
    print("Good night sir, the time is: ", timestamp)