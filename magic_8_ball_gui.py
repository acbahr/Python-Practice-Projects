# 1. Simulate a magic 8-ball.
# 2. Allow the user to enter their question.
# 3. Display an in progress message(i.e. "thinking").
# 4. Create 20 responses, and show a random response.
# 5. Allow the user to ask another question or quit.
# Bonus:
# - Add a gui.
# - It must have box for users to enter the question.
# - It must have at least 4 buttons:
# - ask
# - clear (the text box)
# - play again
# - quit (this must close the window)

# Basic text in TKinter is called a label
import random
import tkinter as tk

"""
def magic_8ball():
    root = tk.Tk()   # constructor class in TKinter. Creates a blank window
    active = True
    responses = ['Yes', 'No', 'Maybe', 'Try Again', "It's Possible", 'It is in the stars', 'Ask me another time',
                 'I am not sure', 'Ask your mother', 'Ask your father', 'Only if you Live Bearded']

    while active:
        label1 = tk.Label(text='What would you like to ask?')
        label1.pack()
        entry = tk.Entry(width=75)
        entry.pack()

        question = entry.get()
        if question != 'n' or question != 'N':
            thinking = tk.Label(text='thinking....')
            thinking.pack()
            return random.choice(responses)
        else:

        print('thinking...')
        print(random.choice(responses))
        try_again = input('Would you like to try again? y/n: ')
        if try_again.lower() == 'n':
            active = False

    root.mainloop()      # mainloop keeps running the window until closed by user

magic_8ball()
"""
