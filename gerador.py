import random
import string

def gerar_senha(tamanho: int) -> str:
    if tamanho <= 0:
        raise ValueError("O tamanho deve ser maior que zero.")

    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return ''.join(random.choice(caracteres) for _ in range(tamanho))