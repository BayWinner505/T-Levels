Teams =["Ferrari","Williams","Haas","Racing Point"]
print("Current bonus payment: ",Teams[0])
print("Current team rival:",Teams[1])
Teams[3] = "Aston Martin"
Teams.append("McLaren")
Teams.append("Red Bull")
print(Teams)
print("Choose a team from the list above 0 being the first team and 5 being the last")
num = int(input("Enter the number you want to change"))
newTeam = input("What is the name of the new team ?")
Teams[num] = newTeam
print(Teams)

          
