import pdftables_api as pdf
from tkinter import *
from tkinter.filedialog import *


class PDFTablesGUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.api_key = 'wd2t2slpdcr6'
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.filepathInput = Button(
            self, text='Transfer', command=self.ChoseFile)
        self.filepathInput.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def ChoseFile(self):
        self.filename = LoadFileDialog(self).go()
        self.outname = self.filename[:-3] + 'xlsx'
        self.Transfer()

    def Transfer(self):
        c = pdf.Client(self.api_key)
        c.xlsx(self.filename, self.outname)

app = PDFTablesGUI()
app.master.geometry('270x80+50+50')
app.master.title('PDF Tables GUI')
app.mainloop()
