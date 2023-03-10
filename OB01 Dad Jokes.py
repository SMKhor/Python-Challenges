import random

class DadJokes():
    def __init__(self, prompt: str, answer: str):
        self.__prompt = prompt #String
        self.__answer = answer #String

    def print_random_joke(self):
        print(self.__prompt)
        user = input("What is your answer? ")
        print("The actual answer: ", self.__answer)
        print("Your answer: ", user)

file = open('DadJokes.txt','r')
content = file.readlines()
file.close()

num = random.randint(0,9)
print(num)
theJoke = DadJokes(content[(num*2)].strip(),content[(num*2)+1].strip())
theJoke.print_random_joke()
