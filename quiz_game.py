print("Welcome to Quiz Game!")

playing = input("Dou you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let's get Started")
score = 0 

answer = input("What does CPU stand for? ")
if answer.lower == "central procesing unit":
    print("Corect!")
    score += 1

else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random acces memory":
    print("Correct!")
    score += 1

else:
    print("Incorrects")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical proccesing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 3 ) * 100) + "%")



