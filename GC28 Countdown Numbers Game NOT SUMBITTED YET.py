import random
import time
tiles = []
large_num = [25,50, 75, 100]
small_num = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
setlarge = int(input("How many tiles from the large set do you want? "))
tiles.append(random.sample(large_num, k=setlarge))
tiles.append(random.sample(small_num, k= 6 - setlarge))
target_num = random.randint(100,1000)
print("Your target number is", target_num)
print("Your tiles are", tiles)

n = 3
while n > 0:
    print("Your timer starts in", n, "second(s)")
    time.sleep(1)
    n -= 1
print("START")
time.sleep(1)
n = 30
while n > 0:
    print("You have", n, "second(s) left.")
    time.sleep(1)
    n -= 1
answer = eval(input("Please enter your solution: "))

if answer == target_num:
    print("Congrats! You've achieved 10 points!")
elif target_num - answer in [5,4,3,2,1,-1,-2,-3,-4,-5]:
    print("Congrats! You've achieved 7 points!")
elif target_num - answer in [10,9,8,7,6,-6,-7,-8,-9, -10]:
    print("Congrats! You've achieved 5 points!")
else:
    print("Sorry, you didn't reach the target number...Try Again.")
