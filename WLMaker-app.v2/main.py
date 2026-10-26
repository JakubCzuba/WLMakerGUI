import customtkinter

app = customtkinter.CTk()
app.title("WL-Maker GUI")
app.geometry("1300x800")
customtkinter.set_appearance_mode("dark")

app.grid_columnconfigure(0, weight=1)

button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()