#2.14. Exercises (1)
word1 = "All"
word2 = " work"
word3= " and"
word4 = " no"
word5 = " play"
word6 = " makes"
word7 = " Jack"
word8 = " a"
word9 = " dull"
word10 = " boy."

print(word1+word2+word3+word4+word5+word6+word7+word8+word9+word10)

#2.14. Exercises (2)
i = 6 * (1 - 2)
print(i)

#2.14. Exercises (3)
#print("hello")
#the code before will no run, hello doesn't print

#2.14. Exercises (4)
bruce = 6
print(bruce + 4)

#2.14. Exercises (5)
P = 10000
n = 12
r = 0.08
t = int(input("Number of years: "))
final_amount = P * (1+r/n)**(n * t)
print(final_amount)

#2.14. Exercises (6)
print(5%2)
print(9%5)
print(15%12)
print(12%15)
print(6%6)
print(0%7)
#print(7%0) - results in a ZeroDivisionError: integer division or modulo by zero

#2.14. Exercises (7)
hour = 51 % 24
print("The alarm goes off at ", hour+2, "pm")

#2.14. Exercises (8)
time_now = int(input("Time now in hours (use 24 hours, 11 for 11am and 23 for 11pm): "))
time_wait = int(input("Number of hours to wait: "))

hours_left = time_wait % 24
final_time = time_now + hours_left
if final_time >= 24:
    final_time = final_time - 24

print("Time when the alarm goes off:", final_time)


