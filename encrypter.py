import os
import pyaes

def encrypt_file(file_name, key):
    # Abrir o arquivo a ser criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criar o objeto de criptografia AES
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = f"{file_name}.encrypted"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(crypto_data)

    print(f"Arquivo {file_name} criptografado com sucesso como {encrypted_file_name}.")

# Exemplo de uso
if __name__ == "__main__":
    file_name = "teste.txt"
    key = b"minhachavecripto" 
    encrypt_file(file_name, key)
