import random
import copy 

while True:
    try:
        linhas = int(input("Digite a altura do mapa (máximo 10):"))
        colunas = int(input("Digite a largura do mapa (máximo 10):"))
        if linhas <= 10 and colunas <= 10 and linhas > 0 and colunas > 0:
            mapa = []
            numero_de_minas = int(input("Digite o número minas que deseja enfrentar:"))
            if numero_de_minas <= (linhas*colunas) and numero_de_minas > 0:
                for i in range(linhas):
                    linha = []
                    for j in range(colunas):
                        coluna = []
                        linha.append("*")
                    mapa.append(linha)
    
                for linha in mapa:
                    print(*linha, sep=" ")
                break 
            else:
                print("Inválido, o número de minas não pode ser 0 e nem superior ao tamanho do mapa! ")
        else:
            print("Valor inválido!")        
    except(ValueError):
        print("Digite valores válidos!")

numero_de_linhas = len(mapa)
numero_de_colunas = len(mapa[0])
mapa_invisivel = copy.deepcopy(mapa)
while numero_de_minas>0:
    bomba_linha = random.randint(0, numero_de_linhas-1)  
    bomba_coluna = random.randint(0, numero_de_colunas-1)
    
    if not mapa_invisivel[bomba_linha][bomba_coluna]=="m": 
        mapa_invisivel[bomba_linha][bomba_coluna] = "m"
        numero_de_minas = numero_de_minas - 1
    
print()

def marcar_bomba(mapa):
    '''Marca uma posição como possível mina (M)'''
    try:
        marcar_linha = int(input("Digite a linha que você acredita que há mina está: "))
        marcar_coluna = int(input("Digite a coluna que você acredita que há mina está: "))

        marcar_linha = marcar_linha - 1
        marcar_coluna = marcar_coluna - 1
        
        '''Verifica se está dentro dos limites'''
        if marcar_linha >= linhas or marcar_coluna >= colunas or marcar_linha < 0 or marcar_coluna < 0:
            print("Posição escolhida inválida!")
        else:
            mapa[marcar_linha][marcar_coluna] = "M"

        '''Mostra o mapa atualizado'''
        for linha in mapa:
            print(*linha, sep=" ")
    except(ValueError):
        print("Digite valores válidos!")

def abrir_posicao(mapa):
    '''Abre uma posição e mostra número de minas próximas'''

    try:
        marcacao_lin = int(input("Digite a linha da posição que deseja abrir: "))
        marcacao_col = int(input("Digite a coluna da posição que deseja abrir: "))

        marcacao_lin = marcacao_lin - 1
        marcacao_col = marcacao_col - 1

        '''Verifica se está dentro dos limites'''
        if marcacao_lin >= linhas or marcacao_col >= colunas or marcacao_lin < 0 or marcacao_col < 0:
            print("Posição escolhida inválida")
        else:
            '''Se for mina, perde'''
            if mapa_invisivel[marcacao_lin][marcacao_col] == "m":
                print("Boooom")
                print("Vocẽ perdeu!")
                return False
            else:
                posicoes_verificadas = set()
                bomba = 0

                '''Verifica as 8 posições ao redor'''
                if marcacao_lin + 1 < len(mapa_invisivel):
                    if mapa_invisivel[marcacao_lin + 1][marcacao_col] == "m" and (marcacao_lin + 1, marcacao_col) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin + 1, marcacao_col))

                if marcacao_col + 1 < len(mapa_invisivel[0]):        
                    if mapa_invisivel[marcacao_lin][marcacao_col + 1] == "m" and (marcacao_lin, marcacao_col + 1) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin, marcacao_col + 1))

                if marcacao_lin + 1 < len(mapa_invisivel) and marcacao_col + 1 < len(mapa_invisivel[0]):        
                    if mapa_invisivel[marcacao_lin + 1][marcacao_col + 1] == "m" and (marcacao_lin + 1, marcacao_col + 1) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin + 1, marcacao_col + 1))

                if marcacao_lin - 1 >= 0:
                    if mapa_invisivel[marcacao_lin - 1][marcacao_col] == "m" and (marcacao_lin - 1, marcacao_col) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin - 1, marcacao_col))

                if marcacao_col - 1 >= 0:
                    if mapa_invisivel[marcacao_lin][marcacao_col - 1] == "m" and (marcacao_lin, marcacao_col - 1) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin, marcacao_col - 1))

                if marcacao_lin - 1 >= 0 and marcacao_col - 1 >= 0:
                    if mapa_invisivel[marcacao_lin - 1][marcacao_col - 1] == "m" and (marcacao_lin - 1, marcacao_col - 1) not in posicoes_verificadas:    
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin - 1, marcacao_col - 1))

                if marcacao_lin - 1 >= 0 and marcacao_col + 1 < len(mapa_invisivel[0]):
                    if mapa_invisivel[marcacao_lin - 1][marcacao_col + 1] == "m" and (marcacao_lin - 1, marcacao_col + 1) not in posicoes_verificadas:
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin - 1, marcacao_col + 1))

                if marcacao_lin + 1 < len(mapa_invisivel) and marcacao_col - 1 >= 0:
                    if mapa_invisivel[marcacao_lin + 1][marcacao_col - 1] == "m" and (marcacao_lin + 1, marcacao_col - 1) not in posicoes_verificadas:        
                        bomba = bomba + 1
                        posicoes_verificadas.add((marcacao_lin + 1, marcacao_col - 1))
                        
                '''Mostra número de minas ao redor'''
                mapa[marcacao_lin][marcacao_col] = (bomba)
                for linha in mapa:
                    print(*linha, sep=" ")
                return True
    except(ValueError):
        print("Digite valores válidos!")


def verificador_vitoria(mapa, mapa_invisivel):
    '''Verifica se todas as minas foram marcadas corretamente'''
    for linha in range(len(mapa_invisivel)):
        for coluna in range(len(mapa_invisivel[0])):
            if mapa_invisivel[linha][coluna] == "m":
                if mapa[linha][coluna] != "M":
                    return False
            else:
                if mapa[linha][coluna] == "M":
                    return False
    return True        

    
while True:
        try:
            opcao = int(input("Digite 1 para marcar uma bomba! \n" \
                              "Digite 2 para abrir uma posição! \n" \
                              "Digite 3 para desistir! \n"))

            match opcao:
                case 1:
                    marcar_bomba(mapa)
                    if verificador_vitoria(mapa,mapa_invisivel):
                        print("Parabéns você venceu!")
                        break
                    else:
                        continue
                case 2: 
                    verificador_derrota = abrir_posicao(mapa)
                    if verificador_derrota == False:
                        break
                case 3:
                    print("Desistiu!")
                    break
                case _ :
                    print("Digite um valor do menu!")
        except(ValueError):
            print("Erro digite um número do menu")
