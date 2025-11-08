# Verifica se a respostas do questionario está certa, e adiciona uma pontuação:
def variavel(resposta, resposta2, resposta3, resposta4):
    score = 0
    if resposta == "lionel":
        score = score + 1

    if resposta2 == "argentina":     
        score = score + 1

    if resposta3 == "miroslav klose":       
        score = score + 1
    
    if resposta4 == "real madrid":    
         score = score + 1

    if score == 4:
        print("\nMuito Bem!") 
    else:
        print("\nTente Novamente! As respostas não estão todas corretas.") 
    
# Função principal
def main():

    #entrada de dados
    # Pergunta 1
    print("Qual o primeiro nome do jogador de futebol 'Messi'?")
    resposta = input().lower()

    # Pergunta 2
    print("Qual país venceu a Copa do Mundo de 2022?")
    resposta2 = input().lower()

    # Pergunta 3 
    print("Quem é o maior artilheiro da história das Copas do Mundo? (Nome e Sobrenome)")
    resposta3 = input().lower()

    # Pergunta 4 
    print("Em que time joga Kylian Mbappé atualmente?")
    resposta4 = input().lower()
    
    #processamento
    variavel(resposta, resposta2, resposta3, resposta4)

    #saida de dados
    print("Obrigado por jogar!")


# Chama a função principal
if __name__ == '__main__':
    main()