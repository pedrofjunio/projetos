import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    """
    Gera uma senha aleatória com base nos parâmetros selecionados na interface.
    """
    try:
        comprimento = int(comprimento_entry.get())
        if comprimento <= 0:
            raise ValueError("O comprimento da senha deve ser maior que zero.")
        
        incluir_maiusculas = maiusculas_var.get()
        incluir_minusculas = minusculas_var.get()
        incluir_numeros = numeros_var.get()
        incluir_especiais = especiais_var.get()

        # Conjunto de caracteres disponíveis
        caracteres = ""
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_especiais:
            caracteres += string.punctuation

        # Verifica se pelo menos um tipo de caractere foi selecionado
        if not caracteres:
            messagebox.showerror("Erro", "Pelo menos um tipo de caractere deve ser selecionado.")
            return

        # Gera a senha aleatória
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        senha_label.config(text=f"Senha Gerada: {senha}")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x300")
root.resizable(False, False)

# Título
titulo_label = tk.Label(root, text="Gerador de Senhas Aleatórias", font=("Arial", 16, "bold"))
titulo_label.pack(pady=10)

# Entrada para o comprimento da senha
comprimento_frame = tk.Frame(root)
comprimento_frame.pack(pady=5)
tk.Label(comprimento_frame, text="Comprimento da Senha:").pack(side=tk.LEFT)
comprimento_entry = tk.Entry(comprimento_frame, width=5)
comprimento_entry.pack(side=tk.LEFT)
comprimento_entry.insert(0, "12")  # Valor padrão

# Opções para os tipos de caracteres
opcoes_frame = tk.Frame(root)
opcoes_frame.pack(pady=10)

maiusculas_var = tk.BooleanVar(value=True)
minusculas_var = tk.BooleanVar(value=True)
numeros_var = tk.BooleanVar(value=True)
especiais_var = tk.BooleanVar(value=True)

tk.Checkbutton(opcoes_frame, text="Incluir Letras Maiúsculas", variable=maiusculas_var).pack(anchor=tk.W)
tk.Checkbutton(opcoes_frame, text="Incluir Letras Minúsculas", variable=minusculas_var).pack(anchor=tk.W)
tk.Checkbutton(opcoes_frame, text="Incluir Números", variable=numeros_var).pack(anchor=tk.W)
tk.Checkbutton(opcoes_frame, text="Incluir Caracteres Especiais", variable=especiais_var).pack(anchor=tk.W)

# Botão para gerar a senha
gerar_button = tk.Button(root, text="Gerar Senha", command=gerar_senha, font=("Arial", 12), bg="lightblue")
gerar_button.pack(pady=10)

# Exibição da senha gerada
senha_label = tk.Label(root, text="Senha Gerada: ", font=("Arial", 12), wraplength=380)
senha_label.pack(pady=10)

# Executar a interface gráfica
root.mainloop()
