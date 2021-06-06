import tkinter #importing the library for tkinter



window = tkinter.Tk() #creating an instance of tkinter

window.geometry("312x324") #setting the GUIs size
window.resizable(0, 0)
window.title("Calculator")

#greeting = tkinter.Label(text="Hello, Tkinter")



label = tkinter.Label(text="Hello, Tkinter")

label = tkinter.Label(
    text="Hello, Tkinter",
    foreground="white", #Set the text color to white
    background="black" # Set the background color to black
)

def printerTextButton():
    label = tkinter.label(
        text="Number 8",
        foreground="white",
        background="black"
    )

button = tkinter.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="white",
    fg="orange",
    command= printerTextButton,
)

button.pack()
#greeting.pack()
label.pack()

window.mainloop() 