from cryptography.fernet import Fernet

# Gera uma chave de criptografia aleatória
def gerar_chave():
    return Fernet.generate_key()

# Criptografa os dados usando uma chave fornecida
def criptografar_dados(chave, dados):
    cipher_suite = Fernet(chave)
    return cipher_suite.encrypt(dados.encode())

# Descriptografa os dados usando uma chave fornecida
def descriptografar_dados(chave, dados_criptografados):
    cipher_suite = Fernet(chave)
    return cipher_suite.decrypt(dados_criptografados).decode()

# Exemplo de uso
chave = gerar_chave()
dados = "Texto sensível que precisa ser protegido!"

dados_criptografados = criptografar_dados(chave, dados)
print("Dados criptografados:", dados_criptografados)

dados_descriptografados = descriptografar_dados(chave, dados_criptografados)
print("Dados descriptografados:", dados_descriptografados)

