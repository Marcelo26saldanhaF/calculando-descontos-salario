from calculo_de_salario_liquido import calculo_fgts, calculo_irrf, calculo_s_liquido
from funcoes import arquivo_existe, cadastrar,criar_arquivo, leia_float, ler_arquivo
from interface import cabecalho, menu_de_opcoes,leia_int


arq="funcionarios.csv"

cabecalho("MENU")

opcoes=["cadastrar funcionario","ver tabela","pesquisar","sair"]


menu_de_opcoes(opcoes)

while True:
    num=leia_int("sua opção: ")
    if(num==0):
        if not (arquivo_existe(arq)):
            criar_arquivo(arq)
            while True:
                funcionario=input("digite o nome do funcionario: ")
                salario_bruto=leia_float("digite o salario bruto: ")
                fgts=calculo_fgts(salario_bruto)
                irrf=calculo_irrf(salario_bruto)
                salario_liquido=calculo_s_liquido(salario_bruto,fgts,irrf)
                cadastrar(arq,funcionario,salario_bruto,fgts,irrf,salario_liquido)
                op=input("deseja continuar cadastrando [S/N]: ")
                if("S" or "s"in op):
                    continue
                elif("N"or"n" in op):
                    break
        else:
             while True:
                funcionario=input("digite o nome do funcionario: ")
                salario_bruto=leia_float("digite o salario bruto: ")
                fgts=calculo_fgts(salario_bruto)
                irrf=calculo_irrf(salario_bruto)
                salario_liquido=calculo_s_liquido(salario_bruto,fgts,irrf)
                cadastrar(arq,funcionario,salario_bruto,fgts,irrf,salario_liquido)
                op=input("deseja continuar cadastrando [S/N]: ")
                if(op in "Ss"):
                    continue
                elif(op in "Nn"):
                    break
        
    elif(num==1):
        if arquivo_existe(arq):
            ler_arquivo(arq)
        else:
            criar_arquivo(arq)
        
    elif(num==2):
        print("2")
        
    elif(num==3):
        print("obrigado por usar o nosso sitema :)")
        break
    else:
        print("digite um dos valores acima")