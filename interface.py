mport tkinter as tk
from tkinter import messagebox

def verificar_resposta():
    resposta = entry.get()
    if resposta == "Azul":
        messagebox.showinfo("Resultado", "Resposta correta! Você pode passar.")
    else:
        messagebox.showinfo("Resultado", "Resposta incorreta! Tente novamente.")

# Configuração da janela principal
root = tk.Tk()
root.title("Aventura do Programador")

# Pergunta
label = tk.Label(root, text="Qual é a cor do céu?")
label.pack()

# Caixa de entrada
entry = tk.Entry(root)
entry.pack()

# Botão de verificação
button = tk.Button(root, text="Verificar", command=verificar_resposta)
button.pack()

# Executar o loop principal da interface
root.mainloop()