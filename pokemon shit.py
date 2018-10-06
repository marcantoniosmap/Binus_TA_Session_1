import random
li = []
x = 0

y = 0
file = open("data_in.txt", "r")
for row in file:
    content = file.read().split("\n")
for row in range(0,8):
    f = content[row].split(",")
    li.append([])
    for col in range(len(f)):
        if f[col] == "0":
            print("o", end="  ")
            li[row].append("o")
        elif f[col] == "1":
            print("X", end="  ")
            li[row].append("o")
            x = col
            y = row
        elif f[col] == "2":
            print("#", end="  ")
            li[row].append("#")
    print(" ")
for i in range (0,8):
    if content[i] == "0":
        li[y][x] = "o"
    if content[i] == "2":
        li[y][x] = "#"

print("HELLO POKEWORLD")

print('''

=============

    MENU

==============

Press "W" to Move front
Press "S" to Move back
Press "A" to Move left
Press "D" to Move right
press "E" Save & End Game

 ''')

while 1:

    n =(input("Please choose your command: 1 to 5: "))

    if n == "w":
        if (y - 1 >= 0):
            y -= 1
    elif n == "s":
        if (y + 1 <= 7):
            y += 1
    elif n == "a":
        if (x - 1 >= 0):
            x -= 1
    elif n == "d":
        if (x + 1 <= 7):
            x += 1
    elif n == "E":
        file = open("data.txt", "w")
        temp = ""
        for i in range(len(li)):
            for j in range(len(li[i])):
                if i == y and j == x:
                    temp += "1"
                elif li[i][j] == "o":
                    temp += "0"
                elif li[i][j] == "#":
                    temp += "2"
                if j < len(li[i]) - 1:
                    temp += ","
            temp += "\n"
        if li[y][x] == "#":
            temp += "2"
        else:
            temp += "0"
        file.write(temp)
        file.close()
        break
    if (li[y][x] == "#"):
        probability = random.randint(0,1)
        if probability == 0:
            print("POKEMON,POKEMON, THERE'S A POKEMON!!")
    for i in range(len(li)):
        for j in range(len(li[i])):
            if i == y and j == x:
                print("X", end="  ")
            elif li[i][j] == "o":
                print("o", end="  ")
            elif li[i][j] == "#":
                print("#", end="  ")
        print(" ")
    else:
        print("Sorry 1Wrong Input, try again!")