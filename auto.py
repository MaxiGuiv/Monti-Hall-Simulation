#Automatically choosing number in chsn, then switching. Set numCount to the number of choices. Set runcap to an integer to make the program run that many times. In the end, the program counts how much it wins by decimal and percentage.
#The program gives an estimated expected probability in the end IF the theory is right.

import random
runcap = 1000
chsn = 1
numCount = 100
ask = "y"

x = []
for c in range(numCount):
	x.append(c + 1)

runs = 0
wins = 0

while runs != runcap:
    mark = x[random.randint(0, numCount-1)]

    z = mark
    if chsn == mark:
        while z == mark:
            z = x[random.randint(0, numCount-1)]

    def y(num):
        if x[num] != mark and x[num] != chsn and x[num] != z:
            print(f"{x[num]} is not it!")

    for i in x:
    	y(i - 1)

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
        wins += 1
    elif chsn != mark:
        print("You lose!")
    runs += 1

    print(f" Mark is {mark}")
    print(f" Chosen is {chsn}")

print(f"\n Wins {wins} times, out of {runs} runs. \n {wins}/{runs}")
print(wins / runs)
print(f"{(wins / runs) * 100}%")

if ask == "y":
	print(f"\n Since you chose to switch. If the theory is right, the probability should be close to {numCount-1}/{numCount} or {((numCount-1)/numCount)*100}%. Otherwise it should be closer to 1/2")
elif ask == "n":
	print(f"\n Since you chose to switch. If the theory is right, the probability should be close to {1}/{numCount} or {(1/numCount)*100}%. Otherwise it should be closer to 1/2")
