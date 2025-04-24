import os
import json
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

incomes = []
expenses = []

# Dosya varsa oku, yoksa oluştur
if not os.path.exists("data.txt"):
    with open("data.txt", "w") as f:
        json.dump({"incomes": [], "expenses": []}, f)

with open("data.txt", "r") as f:
    try:
        data = json.load(f)
        incomes = data.get("incomes", [])
        expenses = data.get("expenses", [])
    except json.JSONDecodeError:
        incomes, expenses = [], []

# GUI Başlat
root = tk.Tk()
root.title("Harcama Takip Uygulaması")
root.geometry("400x300")

tk.Label(root, text="Gelir (sadece sayı):").pack()
income_entry = tk.Entry(root)
income_entry.pack()

tk.Label(root, text="Gider (örn: 300, market):").pack()
expense_entry = tk.Entry(root)
expense_entry.pack()

def veri_ekle():
    if income_entry.get():
        incomes.append(income_entry.get())
    if expense_entry.get():
        expenses.append(expense_entry.get())
    income_entry.delete(0, tk.END)
    expense_entry.delete(0, tk.END)
    messagebox.showinfo("Başarılı", "Gelir/Gider eklendi.")

def verileri_kaydet():
    with open("data.txt", "w") as f:
        json.dump({"incomes": incomes, "expenses": expenses}, f, indent=4)
    messagebox.showinfo("Kaydedildi", "Veriler kaydedildi.")

def grafik_goster():
    try:
        with open("data.txt", "r") as f:
            data = json.load(f)
    except:
        messagebox.showerror("Hata", "Veriler okunamadı.")
        return

    # Gelirleri işle
    try:
        income_values = [float(i) for i in data["incomes"]]
    except:
        income_values = []

    # Giderleri işle
    expenses_by_category = {}
    total_expenses = 0
    for entry in data["expenses"]:
        try:
            amount_str, category = entry.split(",")
            amount = float(amount_str.strip())
            category = category.strip()
            expenses_by_category[category] = expenses_by_category.get(category, 0) + amount
            total_expenses += amount
        except:
            continue  # hatalı format varsa atla

    # Grafik 1: Toplam gelir ve gider
    plt.figure(figsize=(6, 4))
    plt.bar(["Gelir", "Gider"], [sum(income_values), total_expenses], color=["green", "red"])
    plt.title("Toplam Gelir ve Gider")
    plt.ylabel("Tutar (TL)")
    plt.tight_layout()
    plt.show()

    # Grafik 2: Gider kategorileri
    if expenses_by_category:
        plt.figure(figsize=(6, 6))
        plt.pie(expenses_by_category.values(),
                labels=expenses_by_category.keys(),
                autopct="%1.1f%%",
                startangle=140)
        plt.title("Giderlerin Kategoriye Göre Dağılımı")
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("Bilgi", "Gösterilecek gider verisi yok.")

# Butonlar
tk.Button(root, text="Veriyi Ekle", command=veri_ekle).pack(pady=5)
tk.Button(root, text="Verileri Kaydet", command=verileri_kaydet).pack(pady=5)
tk.Button(root, text="Grafikleri Göster", command=grafik_goster).pack(pady=5)

root.mainloop()
