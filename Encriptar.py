def encriptar(escolhaInicial):

    # Criando uma lista com alguns caracteres da tabela ASCII (alfabeto + alguns símbolos)
    alphabet = list()
    for i in range(32, 127):
        alphabet.append(chr(i))

    # Pede o texto para o usuário
    mensagem = input("Digite o texto que você quer encriptar: ")

    # Codifica a mensagem
    def codify(char):
        index = 0
        codified = list()

        # Vai letra por letra da mensagem e vê se ela existe na lista que criamos anteriormente
        for i in range(0, len(char)):
            for k in range(0, len(alphabet)):
                # Caso não exista, insere o caractere como ele está 
                if (char[i] not in alphabet):
                    codified.append(char[i])
                    break
                else:
                    # Caso exista, insere o caractere transposto 5 caracteres para a frente 
                    if (char[i] == alphabet[k]):
                        index = k
                        codified.append(alphabet[(index + 5) % 95])
                        
        return codified;
    
    # Falta integrar aqui a parte da chave pública
    # cp = int(input("Digite a sua chave pública: "))
    mensagemEncriptada = codify(mensagem)
    mensagemEncriptada = ''.join(codify(mensagemEncriptada))
    print(mensagemEncriptada)

    arquivo = open("arquivo.txt", "a")
    arquivo.writelines(mensagemEncriptada)
    
    print("Sua mensagem encriptada é:", mensagemEncriptada)

encriptar(1)
