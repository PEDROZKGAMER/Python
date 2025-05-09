#ABS ele retorna numeros negativos em positivos
#Por exemplo:
numero = -23
print(abs(numero)) #Retorna 23

#Dá pra fazer em números flutuantes
#Por exemplo:
numero_flutuante = -3.14
print(abs(numero_flutuante)) #Retorna 3.14

#É importante notar que o ABS() não funciona diretamente com números complexos da mesma forma que para números reais.
#Para números complexos, ela retorna a magnetude(ou módulo), que é calculada usando a seguinte fórmula:
#|z| = √a² + b²; onde z = a + bi, a parte real e b a parte imaginária por exemplo:
numero_complexo = 3 - 4j
print(abs(numero_complexo)) #Retorna 5.0