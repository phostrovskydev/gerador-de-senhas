from gerador import gerar_senha

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
