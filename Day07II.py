import time

my_time = int(input("Enter a number of seconds to wait: "))
print(f"Waiting for {my_time} seconds...")

for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i // 3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
