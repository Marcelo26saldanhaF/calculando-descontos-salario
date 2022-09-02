def calculo_fgts(salario_bruto):
    return (salario_bruto*8)/100

def calculo_irrf(salario_bruto):
    if(salario_bruto>=0 and salario_bruto<=1903.98):
        return 0.00
    elif(salario_bruto>1903.98 and salario_bruto<=2826.55):
        return (salario_bruto*7.50)/100
    elif(salario_bruto>2826.55 and salario_bruto<=3751.05):
        return (salario_bruto*15)/100
    elif(salario_bruto>3751.05 and salario_bruto<=4664.08):
        return (salario_bruto*22.50)/100
    elif(salario_bruto>4664.08):
        return(salario_bruto*27.50)/100

def calculo_s_liquido(salario_bruto,fgts,irrf):
    return (salario_bruto-fgts-irrf)
