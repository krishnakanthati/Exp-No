import random

li1 = list(range(1, 11))
li2 = []


def cycle(li1, li2):
    n = random.randint(1, 10)
    command = str(input("Enter your command "))

    while len(li1) and command == 'next':
        if n not in li2:
            print(n)
            li2.append(n)
            li1.remove(n)
            command = str(input("Enter your command "))
        else:
            n = random.randint(1, 10)
    else:
        li1, li2 = li2, li1
        print("New Cycle")
        cycle(li1, li2)


cycle(li1, li2)
