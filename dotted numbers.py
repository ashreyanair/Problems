import tkinter as tk

# 7x5 dot matrix patterns for digits 0–9
DIGIT_PATTERNS = {
    "0": [
        " ●●● ",
        "●   ●",
        "●  ●●",
        "● ● ●",
        "●●  ●",
        "●   ●",
        " ●●● "
    ],
    "1": [
        "  ●  ",
        " ●●  ",
        "  ●  ",
        "  ●  ",
        "  ●  ",
        "  ●  ",
        " ●●● "
    ],
    "2": [
        " ●●● ",
        "●   ●",
        "    ●",
        "   ● ",
        "  ●  ",
        " ●   ",
        "●●●●●"
    ],
    "3": [
        "●●●● ",
        "    ●",
        "   ● ",
        "  ●● ",
        "    ●",
        "●   ●",
        " ●●● "
    ]
}

# Digit sequence
digit_sequence = ["2", "1", "2", "3"]
current_index = 0

# GUI setup
root = tk.Tk()
root.title("Blinking Dot Numbers")
root.configure(bg="white")
root.geometry("500x400")
root.resizable(False, False)

# Create 7x5 grid of labels
dot_labels = []
for r in range(7):
    row = []
    for c in range(5):
        lbl = tk.Label(root, text=" ", font=("Courier New", 24), bg="white", fg="black")
        lbl.grid(row=r, column=c, padx=4, pady=2)
        row.append(lbl)
    dot_labels.append(row)


# Show digit
def show_digit(digit, color="black"):
    pattern = DIGIT_PATTERNS[digit]
    for r in range(7):
        for c in range(5):
            char = pattern[r][c]
            if char == "●":
                dot_labels[r][c].config(text="●", fg=color)
            else:
                dot_labels[r][c].config(text=" ", fg=color)


# Blink once and then move to next digit
def blink_and_change():
    current_digit = digit_sequence[current_index]
    show_digit(current_digit, color="black")

    # Blink: dim the dots briefly
    root.after(1000, lambda: show_digit(current_digit, color="#cccccc"))  # Blink (dim)
    root.after(1400, next_digit)  # Then change digit


# Move to next digit in sequence
def next_digit():
    global current_index
    current_index = (current_index + 1) % len(digit_sequence)
    show_digit(digit_sequence[current_index], color="black")
    root.after(2000, blink_and_change)


# Start sequence
show_digit(digit_sequence[0])
root.after(2000, blink_and_change)

root.mainloop()