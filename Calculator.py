import tkinter


window = tkinter.Tk()

#greeting = tkinter.Label(text="Hello, Tkinter")



label = tkinter.Label(text="Hello, Tkinter")

label = tkinter.Label(
    text="Hello, Tkinter",
    foreground="white", #Set the text color to white
    background="black" # Set the background color to black
)

#greeting.pack()
label.pack()

window.mainloop() 