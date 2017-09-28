from Tkinter import (
    StringVar, 
    Label, 
    Entry, 
    Button
    )

from settings import FONT_TYPE

class Input(object):
    def __init__(self, root=None, label=None, r=0):
        labelText = StringVar()
        labelText.set(label)
        labelObj = Label(root, textvariable=labelText, font=FONT_TYPE)
        #labelObj.pack(padx=10, side='left')
        labelObj.grid(row=r, column=0, padx=10, pady=10)
 
        self.inputFieldText = StringVar(None)
        inputField     = Entry(
                                root,
                                textvariable=self.inputFieldText, 
                                width=40, 
                                font=FONT_TYPE
        )
        #inputField.pack(padx=10, side='left')
        inputField.grid(row=r, column=1, padx=10, pady=10)

    @property 
    def text(self):
        return self.inputFieldText.get()
    
    def clear(self):
        self.inputFieldText.set('')

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text

class InputButton(object):
    def __init__(self, root=None, command=None, text='save', bg='blue', location=(0,0)):
        Button(root, text=text, command=command, bg=bg).grid(row=location[0], column=location[1], padx=10,pady=10)
