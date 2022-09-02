from multiprocessing.sharedctypes import Value


def cabecalho(msg):
    print("="*40)
    print(msg.center(40))
    print("="*40)

def menu_de_opcoes(lst):
    for i,v in enumerate(lst):
        print(f'{i}-{v}')


def leia_int(msg):
    while True:
        try:
            n=int(input(msg))
        except(TypeError,ValueError):
            print("insira um número válido")
        else:
            return n
