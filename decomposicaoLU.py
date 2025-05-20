class MatrizNaoQuadrada(Exception):
    def __init__(self, mensagem="""Matriz inválida. Verifique seu código para que a 
            Matriz tenha a mesma quantidade de linhas e colunas. 
            Ou que nao tenha elementos faltando."""):
        super().__init__(mensagem)

class MatrizSingular(Exception):
    def __init__(self, mensagem="""Matriz Singular ou Pivô Zero!"""):
        super().__init__(mensagem)

def DecomposicaoLU(A):
    #A é uma matriz quadrada nxn
    #L e U serao matrizes nxn com L tendo 1 na diagonal
    
    n = len(A)
    
    #Criação das matrizes L e U
    L = []
    U = []
    try:
        for linha in A:
            qtdNums = len(linha)
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

        
        for k in range(n): # Esse for vai percorrer de 0 até o valor da matriz quadrada, exemplo: 3x3, 4x4, 5x5. Vai percorrer de 0 a 2, 0 a 3 e 0 a 4, respectivamente, pois o for in range ignora a última casa.
            #calcula os elementos de U na linha k
            for j in range(k, n):
                soma = 0
                for s in range(0, k):
                    soma += L[k][s] * U[s][j]
                U[k][j] = A[k][j] - soma
            
            if U[k][k] == 0:
                raise MatrizSingular
            
            
            
            # Calcula os elementos de L na coluna k
            for i in range(k+1, n):
                soma = 0
                for s in range(0, k):
                    soma += L[i][s] * U[s][k]
                if U[k][k] != 0:
                    L[i][k] = (A[i][k] - soma) / U[k][k]
                else:
                    # Matriz singular ou pivô zero
                    #interromper ou tratar erro
                    raise MatrizSingular
                
        
            # Define L[k][k] como 1 (diagonal principal de L)
            L[k][k] = 1
          
          
          
          
        print("========= RESULTADO DA DECOMPOSICAO LU =========")
        print()
        print('Matriz A: ')
        for i in range(n):
            for j in range(n):
                print(f"{A[i][j]:.2f}", end='  ')
            print()  
          
        print()  
          
            
        print('Matriz L: ')
        for i in range(n):
            for j in range(n):
                print(f"{L[i][j]:.2f}", end='  ')
            print()
        
        print()
        
        print('Matriz U: ')
        for i in range(n):
            for j in range(n):
                print(f"{U[i][j]:.2f}", end='  ')
            print() 
    
        
    
    
    
    except MatrizSingular as erro:
        print(f'Erro: {erro}')
    except MatrizNaoQuadrada as erro:
        print(f"Erro: {erro}")



def definicao_matrizA_Por_Inputs():
    
    num = ' '
    while type(num) != int or num <= 0:
        try: 
            num = int(input("Altura e largura(As duas devem ser iguais) da matriz: "))
            
            if num <= 0:
                print("Erro: Valor inválido. Digite um número inteiro e positivo.")
            
        except:
            print("Erro: Valor inválido. Digite um número inteiro e positivo.")
    A = []
        
    for i in range(num):
        linhaA = []
        for j in range(num):
            linhaA.append('-    ')
        A.append(linhaA)


    for i in range(num):
        for j in range(num):
            valor = ' '
            while type(valor) != float:
                try:
                    valor = float(input(f"Digite o valor para a posicão {i}X{j}: "))
                except:
                    print("Erro: Valor inválido. Digite um número.")
            A[i][j] = valor
            for k in range(num):
                for l in range(num):
                    if type(A[k][l]) == str:
                        print(f"{A[k][l]}", end='  ')
                    else:
                        print(f"{A[k][l]:.2f}", end='  ')
                print()  
            print()
            

    return A
    
    
    
#A = definicao_matrizA_Por_Inputs()    


A = [[2, 3, 1],
     [4, 7, 7],
     [-2, 4, 5]
    ]

DecomposicaoLU(A)






