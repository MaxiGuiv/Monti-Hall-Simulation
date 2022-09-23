#Manually putting the desired number, and being asked to switch or not.
import random
x = [1, 2, 3, 4, 5]

print("Numbers are 1 through 5")

mark = x[random.randint(0, 4)]
chsn = int(input("What is your chosen number? "))

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

ask = (input("Want to change? (y/n) "))

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

print(f" Mark is {mark}")
print(f" Chosen is {chsn}")
