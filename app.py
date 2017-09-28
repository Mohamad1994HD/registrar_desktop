from Tkinter import Tk

from excelsheet import Controller
from settings import PATH_TO_EXCEL_FILE
from entrywidget import Input, InputButton

controller = Controller(PATH_TO_EXCEL_FILE)
##
root = Tk()

#
nameInput = Input(root, 'Name', r=1)
emailInput = Input(root, 'Email', r=2)
phoneInput = Input(root, 'Phone Number', r=3)

        
def on_click():
    controller.append([nameInput.text, emailInput.text, phoneInput.text])
    nameInput.clear()
    emailInput.clear()
    phoneInput.clear()
    

submit = InputButton(root, on_click, location=(4,2))

if __name__ == '__main__':
    root.mainloop()

