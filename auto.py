#Automatically choosing number 1, then switching. The program ends when it loses. A counter is placed to keep track on how many times the program ran before losing.
import random
x = [1, 2, 3, 4, 5]
whileender = True
count = 0

while whileender:
    mark = x[random.randint(0, 4)]
    chsn = 1

    z = mark

    if chsn == mark:
        while z == mark:
            z = x[random.randint(0, 4)]

    def y(num):
        if x[num] != mark and x[num] != chsn and x[num] != z:
                print(f"{x[num]} is not it!")

    y(0)
    y(1)
    y(2)
    y(3)
    y(4)

    ask = "y"

    if ask == "y":
        if chsn != mark:
            chsn = mark
        elif chsn == mark:
            chsn = z
        print(f"Chosen is now {chsn}")
    elif ask == "n":
        print(f"Chosen is still {chsn}.")

    if chsn == mark:
        print("You won!")
    elif chsn != mark:
        print("You lose!")
        whileender = False
    
    count += 1

    print(f" Mark is {mark}")
    print(f" Chosen is {chsn}")

print(f"\n Lost after {count} runs")
