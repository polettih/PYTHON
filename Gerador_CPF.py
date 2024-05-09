from random import randint

nove_digitos = ''
for contar_nove in range(9):
    nove_digitos +=  str(randint(0,9))    

contador_regressivo_1 = 10 
#Variavel que recebe o valor do primeiro digito do CPF depois do traço
resultado_digito_1 = 0          
#Lista que recebe todos os numeros do CPF, um a um
numeros_int = []                

for digito_1 in nove_digitos:
    digito_1 = int(digito_1)  
    #Soma-se o resultado da conta do ciclo passado a do atual                              
    resultado_digito_1 += digito_1 * contador_regressivo_1    
    contador_regressivo_1 -= 1   
    #Em cada volta adiciona o valor a lista "numeros_int"                           
    numeros_int.append(digito_1)                            

digito_1 = (resultado_digito_1 * 10) % 11
#Se o resto for <= 9 o primeiro numero é o da variavel, se for maior será 0
digito_1 = digito_1 if digito_1 <= 9 else 0     

#Adiciona o resultado a lista "numeros_int"
numeros_int.append(digito_1)                    


#Fase 2
contador_regressivo_2 = 11          
resultado_digito_2 = 0              

for digito_2 in numeros_int:
    resultado_digito_2 += digito_2 * contador_regressivo_2  
    contador_regressivo_2 -= 1                              

digito_2 = (resultado_digito_2 * 10) % 11          
#Se "digito_2" for menor ou igual a 9 "digito_2" será igual ao resto, caso contrario será 0
digito_2 = digito_2 if digito_2 <= 9 else 0         

#Adiciona o "digito_2" na lista "numeros_int"
numeros_int.append(digito_2)        

#CPF inteiro e concatenado
cpf_gerado = int(f'{nove_digitos}{digito_1}{digito_2}')     

print(cpf_gerado)

