# %%
listas = [1, 2, 3, 4, 5,2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6,7, 8, 9, 10,2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15]


print(listas)


numero = input("Digite um número: ")
numero = int(numero)

contador = 0
for i in listas:
    if i == numero:
        contador += 1

        
print(f"O número {numero} aparece {contador} vezes na lista.")

# %%
