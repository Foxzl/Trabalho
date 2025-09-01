import tkinter as tk
from tkinter import filedialog
from tkinter import ttk 
import envix_whats as ew


janela = tk.Tk()

class Application():
    def __init__(self):
        self.janela = janela
        self.screen()
        self.frames()
        self.buttons()
        janela.mainloop()
    def screen(self):
        self.janela.title("SStelecom")
        self.janela.configure(background= '#2e8b57')
        self.janela.geometry("800x640")
        self.janela.resizable(True, True)
    def frames(self):
        self.frame_1 = tk.Frame(self.janela, background='#2e8b57')
        self.frame_1.place(relx=0 , rely=0, relheight=1, relwidth=1)
    def buttons(self):
        self.bt_whats = tk.Button(self.frame_1, text='Enviar', command=ew.start_whats)
        self.bt_whats.place(relx=0.5,rely=0.5, anchor='center')

        self.bt_whats = tk.Button(self.frame_1, text='Selecionar arquivo', command=ew.escolherArquivo)
        self.bt_whats.place(relx=0.5,rely=0.55, anchor='center')

        
        
    def selecionar_pasta(self):
    # Abre a janela de diálogo para selecionar uma pasta
        self.path_paste_1 = filedialog.askopenfilename()
        
        

Application()