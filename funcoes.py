import csv



def arquivo_existe(arq):
    try:
        open(arq,"r")
    except(FileNotFoundError):
        return False
    else:
        return True


def criar_arquivo(arq):
    a=open(arq,"x")
    print("seu aruivo foi criado com sucesso...")
    a.close()

def cadastrar(arq,funcionario,salario_bruto,fgts,irrf,salario_liquido):
    f = open(arq,"a",newline='') 
    w=csv.writer(f)
    w.writerow([funcionario,salario_bruto,fgts,irrf,salario_liquido])


def ler_arquivo(arq):
    with open(arq,"r") as arquivo:
        arquivo_csv=csv.reader(arquivo,delimiter=";")
        for linha in arquivo_csv:
            print(linha)
    

def leia_float(msg):
    while True:
        try:
            n=float(input(msg))
        except(ValueError,TypeError):
            print("digite o salário bruto")
        else:
            return n

   

    


    