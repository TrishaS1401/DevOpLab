print("Rock...")
print("Paper...")
print("Scissors...")


p1 = input("Player 1:Plz enter your choice: ")
p2 = input("Player 2:Plz enter your choice: ")


if (p1 == p2) :
	print("Its a tie")
elif( p1 == 'rock' and p2 == 'paper' or p1 == 'paper' and p2 == 'scissors' or p1 == 'scissors' and p2 == 'rock') :
	print("Congratulations!!! Player 2 wins")
elif( p2 == 'rock' and p1 == 'paper' or p2 == 'paper' and p1 == 'scissors' or p2 == 'scissors' and p1 == 'rock') :
	print("Congratulations!!! Player 1 wins")
else :
	print("Please try again")

