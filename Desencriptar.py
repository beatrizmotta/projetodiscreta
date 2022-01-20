def desencriptar(escolhaInicial):

    # Criando uma lista com alguns caracteres da tabela ASCII (alfabeto + alguns símbolos) para poder fazer 
    # a decodificação 

    alphabet = list()
    for i in range(32, 800):
        alphabet.append(chr(i))

    # Pede o texto para o usuário
    mensagem = input("Digite o texto que você quer encriptar: ")

    # Decodifica a mensagem
    def decodify(char):
        index = 0
        decodified = list()
        # Vai letra por letra da mensagem e vê se ela existe na lista que criamos anteriormente
        for i in range(0, len(char)):
            for k in range(0, len(alphabet)):
                # Caso não exista, insere o caractere como ele está 
                if (char[i] not in alphabet):
                    decodified.append(char[i])
                    break
                else:
                    # Caso exista, insere o caractere transposto 5 caracteres para a trás
                    if (char[i] == alphabet[k]):
                        index = k
                        decodified.append(alphabet[(index - 5) % 768])
                        # 768 = 800 - 32, o número de caracteres que temos no 'alfabeto' que criamos na lista
                    
        return decodified;
    
    # cp = int(input("Digite a sua chave pública: "))
    mensagemDesencriptada = decodify(mensagem)
    mensagemDesencriptada = ''.join(decodify(mensagemDesencriptada))

    arquivo = open("arquivo.txt", "a")
    arquivo.writelines(mensagemDesencriptada)
    
    print("Sua mensagem desencriptada é:", mensagemDesencriptada)


desencriptar(2)
