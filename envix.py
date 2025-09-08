import tkinter as tk
from tkinter import filedialog
from tkinter import ttk 
import customtkinter as ctk
import envix_whats as ew
from PIL import ImageTk, Image


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
    def Effects(self):
        self.bt_whats.configure(state='normal')
        path_s = filedialog.askopenfilename()
    def buttons(self):
        self.bt_whats = ctk.CTkButton(self.frame_1, text="Enviar mensagens", command=ew.start_whats, state='disabled')
        self.bt_whats.place(relx=0.5,rely=0.5, anchor='center')
               

        self.bt_arq = ctk.CTkButton(self.frame_1, text="Escolher arquivo", command=self.Effects )
        self.bt_arq.place(relx=0.5,rely=0.55, anchor='center')

        
        

Application()