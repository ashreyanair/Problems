import tkinter
def cal_bmi():
    h = float(ht_val.get())
    w = float(wt_val.get())
    h1 = h / 100
    bmi = w / (h1 ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        status = "Normal"
    elif 25.0 <= bmi <= 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    res.config(text=f"BMI IS {bmi} ({status})", bg="blue")


root = tkinter.Tk()
root.geometry("600x400")
root.title("BMI CALCULATOR")
root.config(bg="green")

head = tkinter.Label(root, text="BMI CALCULATOR", font=("Arial", 20, "bold"), bg="green")
head.pack(pady=30)

frame = tkinter.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

ht_label = tkinter.Label(frame, text="HEIGHT (in cm)", font=("Arial", 10, "bold"), bg="#f0f0f0")
ht_label.grid(row=0, column=0, padx=5, pady=5)
ht_val = tkinter.Entry(frame)
ht_val.grid(row=0, column=1, padx=5, pady=5)

wt_label = tkinter.Label(frame, text="WEIGHT (in kg)", font=("Arial", 10, "bold"), bg="#f0f0f0")
wt_label.grid(row=1, column=0, padx=5, pady=5)
wt_val = tkinter.Entry(frame)
wt_val.grid(row=1, column=1, padx=5, pady=5)

bt = tkinter.Button(frame, text="Calculate", font=("Arial", 12, "bold"), command=cal_bmi)
bt.grid(row=2, column=0, columnspan=2, pady=10)

res = tkinter.Label(text="Your BMI will appear here", bg="blue", font=("Arial", 10, "bold"))
res.pack(pady=10)

root.mainloop()
