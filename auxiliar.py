# lista 
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
nomes.append('Fernanda')  # adiciona um nome à lista
print(nomes)

primeiro_nome = nomes[0]  # acessa o primeiro nome da lista
print(primeiro_nome)

# dicionario python
mensagem = {"role": "user", "content": "Coe galera"}
# dicionario = {chave: valor, chave: valor}

texto_mensagem = mensagem["content"]  # acessa o valor associado à chave "content"
print(texto_mensagem)  # imprime o valor associado à chave "quem"

# dicionario com lista
lista_mensagens = [
    {"quem": "user", "content": "Oi, tudo bem?"},
    {"quem": "assistant", "content": "Tudo sim, e você?"},
    {"quem": "user", "content": "Estou bem, obrigado!"}
]

lista_mensagens.append(
    {"quem": "assistant", "content": "Que bom saber disso!"}
    )  # adiciona uma nova mensagem

print(lista_mensagens)