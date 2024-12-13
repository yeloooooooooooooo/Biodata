import tkinter as tk

valid_names = ["Enter", "ENTER", "enter"]  # Add more valid names as needed

def Bionote():
    entered_name = enter_entry.get().strip()  # Get the entered name
    if entered_name in valid_names:
        kim = "Congratulations!"
    else:
        kim = "System Error!"
    result_label.config(text=f"{kim}")


BioData = tk.Tk()
BioData.title("Biography")

BioData.geometry("250x250")
BioData.resizable(True, True)
BioData.configure(background="pink")

label = tk.Label(BioData, text="Please Fill Up the Form!", font=("Arial", 25), bg="pink")
label.grid(row=0, column=3, padx=1, pady=1, sticky="W")

name_label = tk.Label(BioData, text="Name:", font=("Arial", 14), bg="Pink")
name_label.grid(row=2, column=0, padx=1, pady=1, sticky="e")
name_entry = tk.Entry(BioData, font="Arial")
name_entry.grid(row=2, column=3, padx=1, pady=1)

age_label = tk.Label(BioData, text="Age:", font=("Arial", 14), bg="pink")
age_label.grid(row=5, column=0, padx=1, pady=1, sticky="e")
age_entry = tk.Entry(BioData, font="Arial")
age_entry.grid(row=5, column=3, padx=1, pady=1)

place_label = tk.Label(BioData, text="Place:", font=("Arial", 14), bg="pink")
place_label.grid(row=7, column=0, padx=1, pady=1, sticky="e")
place_entry = tk.Entry(BioData, font="Arial")
place_entry.grid(row=7, column=3, padx=1, pady=9)

enter_label = tk.Label(BioData, text="Type Enter for Confirmation", font=("Arial", 14), bg="pink")
enter_label.grid(row=9, column=0, padx=0, pady=1, sticky="e")
enter_entry = tk.Entry(BioData, font="Arial")
enter_entry.grid(row=9, column=3, padx=1, pady=1, ipady= 9)

confirm_button = tk.Button(BioData, text="Confirm", command=Bionote, font=("Arial", 18), cursor=("hand2"))
confirm_button.grid(row=11, column=3, columnspan=2, pady=1)

result_label = tk.Label(BioData, text="", font=("Arial", 14), bg="#def5ff")
result_label.grid(row=13, column=3, columnspan=1)

BioData.mainloop()