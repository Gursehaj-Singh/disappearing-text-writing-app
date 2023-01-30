import tkinter as tk

timer = 0
has_written = False


# ---------- FUNCTIONS ---------- #

def check_flag(_event=None):
    global has_written
    if has_written:
        reset_timer()
    else:
        has_written = True
        countdown()


def countdown():
    global has_written
    if has_written:
        global timer
        timer += 1
        if timer >= 5:
            delete_text()
            has_written = False
        window.after(1000, countdown)


def reset_timer():
    global timer
    timer = 0


def delete_text():
    textbox.delete("1.0", "end")
    reset_timer()


# ---------- GUI ---------- #

window = tk.Tk()
window.title("Disappearing Text Writing App")
window.geometry('600x800')
window.configure(bg="black")

intro = "Don't type for 5 seconds, everything gets deleted!"
words_label = tk.Label(window, text=intro, font=('Arial', 14), bg="black", fg="gray")
words_label.pack(padx=10, pady=10)

textbox = tk.Text(window, height=40, font=('Arial', 12), bg="black", fg='white')
textbox.bind("<Key>", check_flag)
textbox.pack(padx=20, pady=10)

window.mainloop()
