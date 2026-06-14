from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#171c22") # pure calculator ka background grey/black karne ke liye

expression = ""
equation = StringVar()

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
equation = StringVar()


entry = Entry(root,textvariable=equation,font=("Arial", 28, "bold"),bg="#171c22",fg="#ffffff",bd=0, justify="right",insertbackground="white")
entry.grid(row=0, column=0,columnspan=4, ipady=30, padx=10, pady=10,sticky="nsew")
btn_font = ("Arial", 14, "bold")
num_bg = "#212933"
op_bg = "#2d3846"
equal_bg = "#ff9500"
clear_bg = "#f44336"
text_fg = "#ffffff"

Button(root, text="7", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(7)).grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="8", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(8)).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="9", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(9)).grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="/", font=btn_font, bg=op_bg, fg=text_fg, bd=0, command=lambda:press("/")).grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="4", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(4)).grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="5", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(5)).grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="6", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(6)).grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="*", font=btn_font, bg=op_bg, fg=text_fg, bd=0, command=lambda:press("*")).grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="1", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(1)).grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="2", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(2)).grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="3", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(3)).grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="-", font=btn_font, bg=op_bg, fg=text_fg, bd=0, command=lambda:press("-")).grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="0", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(0)).grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text=".", font=btn_font, bg=num_bg, fg=text_fg, bd=0, command=lambda:press(".")).grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="=", font=btn_font, bg=equal_bg, fg=text_fg, bd=0, command=equal).grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="+", font=btn_font, bg=op_bg, fg=text_fg, bd=0, command=lambda:press("+")).grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
for i in range(6):
    root.rowconfigure(i, weight=1)
    for j in range(4):
        root.columnconfigure(j, weight=1)

root.mainloop()















