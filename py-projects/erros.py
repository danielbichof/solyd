"""
 erros em tempo de compilacao
 ||         ||  de execução
 ||   de lógica
"""



def div(a, b):
    try:
        print(a/b)
    except:
        print('Divisão invalida')



div(20,9)