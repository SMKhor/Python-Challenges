user1 = 0
user2 = 0
print("ONLY User 1 views the screen.")
question1 = input("User1's question: ")
answer1 = input("Answer to User1's question: ")

print("SWITCH - ONLY User 2 views the screen.")
question2 = input("User2's question: ")
answer2 = input("Answer to User2's question: ")

print("User 1 to answer this question:")
print(question2)
user1ans = input("Answer to question: ")
if answer2 == user1ans:
    user1 = user1 + 1


print("User 2 to answer this question:")
print(question1)
user2ans = input("Answer to question: ")
if answer1 == user2ans:
    user2 = user2 + 1

print("User 1's score: ", user1)
print("User 2's score: ", user2)
