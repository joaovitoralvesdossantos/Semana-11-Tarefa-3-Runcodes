# Verifica se a resposta é "Lionel":
def variavel(resposta):
    if resposta == "Lionel":
        print(" :) " * 100)
    else:
        print(" :( " * 100)
# Função principal
def main():

    #entrada de dados
    print("Qual o primeiro nome do jogador de futebol 'Messi'?")
    resposta = input()
    
    #processamento
    variavel(resposta)

    #saida de dados
    print("Obrigado por jogar!")

# Chama a função principal
if __name__ == '__main__':
    main()