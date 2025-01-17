import os
import pyaes

def decrypt_file(file_name, key):
    # Abrir o arquivo criptografado
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Criar o objeto de descriptografia AES
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypt_data = aes.decrypt(file_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o arquivo descriptografado
    original_file_name = file_name.replace(".encrypted", "")
    with open(original_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypt_data)

    print(f"Arquivo {file_name} descriptografado com sucesso como {original_file_name}.")

# Exemplo de uso
if __name__ == "__main__":
    file_name = "teste.txt.encrypted"
    key = b"minhachavecripto"  
    decrypt_file(file_name, key)
