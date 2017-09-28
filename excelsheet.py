import openpyxl

from settings import PATH_TO_EXCEL_FILE

class Controller(object):
    def __init__(self, path=None, new_file=False):
        self.path = PATH_TO_EXCEL_FILE
        if path:
            self.path  = path
        if new_file:
            self.wb    = openpyxl.Workbook() 
        else:
            self.wb    = openpyxl.load_workbook(self.path) 
        self.sheet = self.wb.active

    def save(self):
        self.wb.save(self.path)    
    
    def append(self, val):
        try:
            self.sheet.append(val)
            self.save()
            return True
        except:
            return False
