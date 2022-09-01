import time
hours = int(input("How many hours of playtime does each brother get? "))
hoursleft = hours
for i in range (hoursleft):
    print("One brother plays now until the timer is up: %d hour(s) left" % hoursleft)
    time.sleep(5)
    hoursleft = hoursleft-1
print("BROTHER SWAP")
hoursleft = hours
for i in range (hoursleft):
    print("Another brother plays now until the timer is up: %d hour(s) left" % hoursleft)
    time.sleep(5)
    hoursleft = hoursleft-1
print("NO MORE PLAYTIME")
