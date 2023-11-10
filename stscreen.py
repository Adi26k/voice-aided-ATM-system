from modulefinder import IMPORT_NAME
from unicodedata import name
import customtkinter
import tkinter
from pocketsphinx import LiveSpeech,AudioFile
from spttex import spttx
from spttex import SpeakText
def gui(acc):
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")

    def button_function():
        print("button pressed")
    label = customtkinter.CTkLabel(master=app, text="Account Name :- "+acc["name"])
    label.place(relx=0.3, rely=0.1, anchor=tkinter.N)

    label = customtkinter.CTkLabel(master=app, text=str("Balance :- "+str(acc["balance"])))
    label.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="Deposit", command=button_function)
    button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

    button1 = customtkinter.CTkButton(master=app, text="Withdraw", command=button_function)
    button1.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
    SpeakText("For Withdraw speak zero to check balance speak one ")
    ch=int(spttx())
    print(ch)
    if(ch==0):
        SpeakText("Processing Withdraw request")
        SpeakText("Speak amount")
        amt=int(spttx())
        acc["balance"]= acc["balance"]-amt
        SpeakText("Amount to be withdrawan is "+str(amt))
        SpeakText("New balance is "+str(acc["balance"]))
        
    elif(ch==1):
        SpeakText("Processing  request")
        SpeakText("The balance is "+str(acc["balance"]))
        
    app.mainloop()



