import random

name = input("Please enter student's name: ")

insults = [", if I throw a stick, will you leave?",
", you're a gray sprinkle on a rainbow cupcake.",
", if your brain was dynamite, there wouldn't be enough to blow your hat off.",
", you are more disappointing than an unsalted pretzel.",
", light travels faster than sound, which is why you seemed bright until you spoke.",
", your secrets are always safe with me. I never even listen when you tell me them.",
", I'll never forget the first time we met. But I'll keep trying.",
", hold still. I'm trying to imagine you with a personality.",
", your face makes onions cry.",
", it's impossible to underestimate you.",
", wow your maker really didn't waste time giving you a personality, huh?",
", I'd give you a nasty look, but you've already got one.",
", you are the human version of period cramps.",
", don't worry about me. Worry about your eyebrows.",
", you just might be why the middle finger was invented in the first place.",
", when you start talking, I stop listening."]

print(name, insults[random.randint(0,15)])
