import time
seconds = int(input("How long do you want this countdown to last?"))

for i in range(seconds):
    print(str(seconds-i) + "s left")
    time.sleep(1)

print("LIFT-OFF")
