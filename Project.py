import os
import json
import matplotlib.pyplot as plt

a, b = 0, 0
incomes = []
expenses = []

if os.path.exists("data.txt"):
    print("File exists.")
else:
    print("File doesn't exist. Creating...")
    with open("data.txt", "a") as f:
        pass

while a == 0:
    user_input = input("Enter income (sadece sayı) or 'continue': ")
    if user_input.lower() == "continue":
        break
    else:
        incomes.append(user_input)

while b == 0:
    user_input = input("Enter expense (örn: 300, market) or 'continue': ")
    if user_input.lower() == "continue":
        break
    else:
        expenses.append(user_input)

data = {
    "incomes": incomes,
    "expenses": expenses
}
with open("data.txt", "w") as f:
    json.dump(data, f, indent=4)

with open("data.txt", "r") as f:
    data = json.load(f)

incomes = [float(i) for i in data["incomes"]]
expenses_raw = data["expenses"]

total_income = sum(incomes) #this prompt is so good use this regularly
expenses_by_category = {}
total_expenses = 0

for entry in expenses_raw:
    try:
        amount, category = entry.split(",")
        amount = float(amount.strip())
        category = category.strip()
        print(f"Girdi: {entry} → {amount} TL ({category})")

        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount

        total_expenses += amount
    except:
        print(f"Hatalı format: {entry}")

# Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(["Gelir", "Gider"], [total_income, total_expenses], color=["green", "red"])
plt.title("Toplam Gelir ve Gider")
plt.ylabel("Tutar (TL)")
plt.tight_layout()
plt.show()

# Grafik 2: Giderler Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(expenses_by_category.values(),
        labels=expenses_by_category.keys(),
        autopct="%1.1f%%",
        startangle=140)
plt.title("Giderlerin Kategoriye Göre Dağılımı")
plt.tight_layout()
plt.show()
