import random
import string  

#irei importar a biblioteca string para facilitar a geração de caracteres especiais

def gerar_senha(tamanho: int) -> str:
    if tamanho <= 0:
        raise ValueError("O tamanho da senha deve ser maior que zero.")
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return ''.join(random.choice(caracteres) for _ in range(tamanho))


def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")

    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha = gerar_senha(tamanho)
        print(f"\nSenha gerada com sucesso:\n{senha}")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()

    