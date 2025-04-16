import os
import json
a,b=0,0
incomes=[]
expenses=[]

if os.path.exists("data.txt"):
    print("File exists.")
else:
    print("File doesn't exist. Creating...")
    with open("data.txt","a") as f:
        pass

while a==0:
    user_input = input("Enter income or /continue")
    if user_input == "continue":
        break
    else :
        incomes.append(user_input)

while b==0:
    user_input = input("Enter expenses or /continue")
    if user_input == "continue":
        break
    else:
        expenses.append(user_input)
with open("data.txt","w") as f:
    json.dump(incomes,f)
    json.dump(expenses,f)
