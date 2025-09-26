outdoors = 0
indoors = 0


answer = input("After school would you rather A go hangout at a park or B go home and sleep?")
if answer == "A":
	outdoors += 1
elif answer == "B":
	indoors += 1


answer = input("would you rather A go on a hike B watch a movie?")
if answer == "A":
	outdoors += 1
elif answer == "B":
	indoors += 1


answer = input("If you go to a restaurant would you rather A eat indoors B eat outdoors")
if answer == "A":
	indoors += 1
elif answer == "B":
	outdoors += 1

if answer == "B" and outdoors > 2:
	print("You seem to like outdoors.. Wait!! Theres still more questions.")
	
answer = input("Would you rather A have PE outside or B PE in the gym")
if answer == "A":
    outdoors += 1
elif answer == "B":
	indoors += 1

answer = input("Would you rather A hangout with friends or B text them")
if answer == "A":
    outdoors += 1
elif answer == "B":
	indoors += 1
if answer == "A" or answer == "B":
	print("you are finally done with the quiz! Are you ready for your result")
input("")
if indoors > outdoors:
	print("You are a indoors person!!!!")
if outdoors > indoors:
	print("you are a outdoors person!!!")