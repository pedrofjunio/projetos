import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    """
    Gera uma senha aleatória com base nos critérios fornecidos.
    
    :param comprimento: Comprimento da senha (padrão: 12).
    :param incluir_maiusculas: Incluir letras maiúsculas na senha (padrão: True).
    :param incluir_minusculas: Incluir letras minúsculas na senha (padrão: True).
    :param incluir_numeros: Incluir números na senha (padrão: True).
    :param incluir_especiais: Incluir caracteres especiais na senha (padrão: True).
    :return: Uma senha aleatória.
    """
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
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("=== Gerador de Senhas ===")
    try:
        comprimento = int(input("Digite o comprimento da senha desejada: "))
        if comprimento <= 0:
            raise ValueError("O comprimento da senha deve ser maior que zero.")
        
        incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
        incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
        incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

        senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
        print(f"\nSenha gerada: {senha}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()