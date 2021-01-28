import tkinter


root = tkinter.Tk()   # constructor class in TKinter. Creates a blank window
    # I want to create text on my screen so I am using Label
#    the_label = tkinter.Label(root, text="This is too easy, make sure this is long enough!")
#    the_label.pack()   # pack is placing the window where ever you can fit it

topFrame = tkinter.Frame(root)  # make an invisible container and it will go in the main window (root)
topFrame.pack()
bottomFrame = tkinter.Frame(root)
bottomFrame.pack(side='bottom')
rightFrame = tkinter.Frame(root)
rightFrame.pack(side='right')

button1 = tkinter.Button(topFrame, text='Button 1', fg = 'red')
button2 = tkinter.Button(topFrame, text='Button 2', fg = 'blue')
button3 = tkinter.Button(topFrame, text='Button 3', fg = 'green')
button4 = tkinter.Button(bottomFrame, text='Button 4', highlightbackground='purple')

label1 = tkinter.Label(rightFrame, text='Label 1', fg='white', bg='black')
tkinter.Label(bottomFrame, text='Label 2', fg='blue', bg='green').pack(side='right')


button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
button4.pack(side='right')
label1.pack(fill=tkinter.Y)

root.mainloop()   # mainloop keeps running the window until closed by user
