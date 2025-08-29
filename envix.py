import tkinter as tk
from tkinter import ttk # Importe o módulo ttk para os widgets de aparência mais moderna
import envix_whats as ew

janela = tk.Tk()
janela.title("Envio primeiro atendimento")
janela.geometry("800x650") # Defina um tamanho inicial para a janela



notebook = ttk.Notebook(janela)
notebook.pack(pady=10, padx=10, fill="both", expand=True) # Empacote o notebook para que ele preencha o espaço da janela

# Aba 1
aba1_frame = ttk.Frame(notebook, padding="10")
aba1_frame.pack(fill="both", expand=True) # Garante que o frame preencha a aba

botao = tk.Button(janela, text="ENVIAR", command=ew.start_whats)
botao.pack(pady=10) # pady adiciona um espaçamento vertical


botao_selecionar = tk.Button(janela, text="Selecionar Arquivo", command=ew.escolherArquivo)
botao_selecionar.pack(pady=10)

# Widgets para a Aba 1N
label1 = ttk.Label(aba1_frame, text="Este é o conteúdo da Aba 1")
label1.pack(pady=5)


# Aba 2
aba2_frame = ttk.Frame(notebook, padding="10")
aba2_frame.pack(fill="both", expand=True) # Garante que o frame preencha a aba

# Widgets para a Aba 2
label2 = ttk.Label(aba2_frame, text="Este é o conteúdo da Aba 2")
label2.pack(pady=5)

notebook.add(aba1_frame, text=" Primeiro atendimento whats ")
notebook.add(aba2_frame, text=" Primeiro atendimento outlook ")

janela.mainloop()