# Classe de exceção, caso a matriz não seja quadrada
class MatrizNaoQuadrada(Exception):
    def __init__(self, mensagem="""Matriz inválida. Verifique seu código para que a 
            Matriz tenha a mesma quantidade de linhas e colunas. 
            Ou que nao tenha elementos faltando."""):
        super().__init__(mensagem)

# Classe de exceção, caso a matriz seja Singular
class MatrizSingular(Exception):
    def __init__(self, mensagem="""Matriz Singular ou Pivô Zero!"""):
        super().__init__(mensagem)

def DecomposicaoLU(A):
    #A é uma matriz quadrada nxn
    #L e U serao matrizes nxn com L tendo 1 na diagonal

    # Pegando o n pela quantidade de linhas da matriz, ja que as duas medidas devem ser iguais
    n = len(A)
    
    #Criação das matrizes L e U
    L = []
    U = []
    try:
        """
        Verificação, caso a matriz não seja quadrada.  
        """        
        for linha in A:
            qtdNums = len(linha) # qtd de valores em cada linha da matriz
            """
            se a quantidade de valores nao bater com a quantidade de linhas, 
            significa que não é uma matriz quadrada
            """
            if(qtdNums != n): 
                raise MatrizNaoQuadrada


        # Preenchendo as duas matrizes L e U com 0 em todas as casas
        for i in range(n):
            linhaU = []
            linhaL = []
            for j in range(n):
                linhaU.append(0)
                linhaL.append(0)
            L.append(linhaL)
            U.append(linhaU)

        """ 
        Esse for vai percorrer de 0 até o valor da matriz quadrada
        exemplo: 3x3, 4x4, 5x5. Vai percorrer de 0 a 2, 0 a 3 e 0 a 4, respectivamente, 
        pois o for in range ignora a última casa.
        """
        for k in range(n): 
            #calcula os elementos de U na linha k
            for j in range(k, n): #Percorre todos os valores da linha da matriz U
                soma = 0
                for s in range(0, k): # Para cada valor, é feita a soma dos produtos dos valores de L e U
                    soma += L[k][s] * U[s][j]
                """
                Ao terminar a soma, é feita a subtração do valor de mesma posição da matriz A e a soma
                E é iterado no valor da linha k e coluna j, assim concluindo a linha de U, ao fazer para todos os valores
                """
                U[k][j] = A[k][j] - soma
                

            """
            Verificação, caso o elemento da diagonal principal (PIVÔ) de U seja ZERO.
            Significa que a matriz A é singular e não é possível executar a decomposição.
            Deve-se lançar a exceção e encerrar o programa.
            """
            if U[k][k] == 0:
                raise MatrizSingular
            
            """
            Os valores da Matriz U são calculados linha por linha.
            Enquanto os valores da Matriz L são coluna por coluna.
            Isso acontece porque a matriz U é uma matriz triangular superior,
            enquanto a matriz L é uma matriz triangular inferior.

            O valor k no for que engloba as contas das duas matrizes, serve para lidar
            com as posições de U e L. Quando o valor k vai aumentando, devido a quantidade de passadas
            do for. Vai limitando as linhas e colunas de U e L, "pulando" as posições que devem 
            permanecer ZERO.



            Ficando assim:

            Exemplo: uma matriz 3x3



                    Antes de do for    k = 0     k = 1    k = 2
            MATRIZ U:
                         0 0 0         x x x     x x x    x x x               
                         0 0 0         0 0 0     0 x x    0 x x
                         0 0 0         0 0 0     0 0 0    0 0 x
            
            MATRIZ L:                
                         0 0 0         1 0 0     1 0 0    1 0 0
                         0 0 0         x 0 0     x 1 0    x 1 0
                         0 0 0         x 0 0     x x 0    x x 1
            

            Desse jeito, Nós temos 2 matrizes triangulares: uma superior(U) 
            e outra inferior(L) que tem a diangonal principal completa de 1

            
            """


            
            
            # Calcula os elementos de L na coluna k
            """
            Esse primeiro for vai cuidar das posições das colunas que devem ser preenchidas.
            Note que esse for começar no k+1, enquanto no for que calcula a matriz U é só k.
            Isso acontece porque a matriz L tem a diagonal principal 1, logo deve sempre pular
            o primeiro valor da coluna, já que o for k de fora já pula os valores que devem
            permanecer ZERO.
            """
            for i in range(k+1, n):
                soma = 0
                for s in range(0, k): # Esse for serve para calcular a soma dos produtos dos valores de L e U, igual a matriz U
                    soma += L[i][s] * U[s][k]

                # verificação extra para garantir que o pivô da matriz U não seja ZERO
                if U[k][k] != 0: # Se nao for, segue a formula normalmente
                    """
                    Essa conta é parecida com a conta de U, com a diferença de que tem que dividir 
                    pelo pivô da matriz U da coluna que estamos calculando, por isso o pivô nunca 
                    deve ser ZERO, pois não é possível dividir um numero por ZERO.
                    """
                    L[i][k] = (A[i][k] - soma) / U[k][k]
                else: # Se for igual a ZERO o pivô
                    """
                    Significa que a matriz A é singular e não é possível executar a decomposição.
                    Deve-se lançar a exceção e encerrar o programa.
                    """
                    raise MatrizSingular
                
        
            """
            Ao fim das contas da linha de U e coluna de L
            Define L[k][k] como 1 (diagonal principal de L)
            """
            L[k][k] = 1
          
          


        """
        Aqui são mostradas todas as matrizes (A, L e U) depois da decomposição LU
        """
          
        
          
          
        print("========= RESULTADO DA DECOMPOSICAO LU =========")
        print()
        print('Matriz A: ')
        for linha in A:
            print("      ".join(f"{num:>10.2f}" for num in linha))
          
        print()  
          
            
        print('Matriz L: ')
        for linha in L:
            print("      ".join(f"{num:>10.2f}" for num in linha))
        
        print()
        
        print('Matriz U: ')
        for linha in U:
            print("      ".join(f"{num:>10.2f}" for num in linha))
    
        
    
    
        """
        Aqui é onde cai a exceção, quando uma exceção é levantada usando o raise
        """
    except MatrizSingular as erro:
        print(f'Erro: {erro}')
    except MatrizNaoQuadrada as erro:
        print(f"Erro: {erro}")



def definicao_matrizA_Por_Inputs():
    
    num = ' '

    """
    Pergunta do tamanho da matriz
    Enquanto o valor for menor ou igual a ZERO,
    continuará sendo perguntado, até ser digitado um valor valido
    """
    while type(num) != int or num <= 0:
        try: 
            num = int(input("Altura e largura(As duas devem ser iguais) da matriz: "))

            """
            Exibe mensagem de erro, pois um numero 0 ou negativo, ainda sim é um inteiro,
            logo não é ativada a exceção.
            """            
            if num <= 0:
                print("Erro: Valor inválido. Digite um número inteiro e positivo.")

            """
            Se for digitado um valor inválido, como: string ou float, cairá nessa exceção
            e o while coontinuará.
            """
        except:
            print("Erro: Valor inválido. Digite um número inteiro e positivo.")


    
    A = []
    """
    Colocação de hífens para cada posição da Matriz A para melhorar visualmente
    """
    for i in range(num):
        linhaA = []
        for j in range(num):
            linhaA.append("- ")
        A.append(linhaA)



    """
    Trecho responsável por perguntar qual o número a ser colocado na posição, 
    seguindo do 0x0 -> 0x1 -> 0x2 -> 1x0, e assim por diante.
    Se for digitado um valor não numérico(que nao seja int nem float) cairá na exceção
    e o codigo só irá avançar, quando for digitado um valor numérico.
    """

    
    for i in range(num):
        for j in range(num):
            valor = ' '
            while type(valor) != float:
                try:
                    valor = float(input(f"Digite o valor para a posicão {i}X{j}: "))
                except:
                    print("Erro: Valor inválido. Digite um número.")
            A[i][j] = valor
            for linha in A:
                print("      ".join(f"{num:>10}" for num in linha))
                
            print()
            

    return A
    
    
"""
chamada de uma funcao que possibilita colocar valor por valor usando inputs
"""
#A = definicao_matrizA_Por_Inputs()    

"""
Definicao de uma matriz 3x3 usando o código
"""

A = [[1, 2, 3],
     [4, 5, 10],
     [7, 8, 9]
    ]


DecomposicaoLU(A)





