#%%
import random  as rand

escolhido = 0
gerado = rand.randint(1, 15)
count = 0
print("Bem-vindo à Loteria Babilônia! Tente adivinhar o número gerado entre 1 e 15. Você tem 3 tentativas.")

while escolhido !=  gerado and count <3:

    
    escolhido = int(input("Digite o número para adivinhar: "))

    count+=1

    if escolhido == gerado:
        print(f"Parabéns, você acertou o número {gerado} em {count} tentativas!")
    elif escolhido < gerado:
        print("O número escolhido é menor do que o número gerado. Tente novamente.")    
    elif escolhido > gerado:
        print("O número escolhido é maior do que o número gerado. Tente novamente.")    
        

if escolhido != gerado:
    print(f"Infelizmente, você não acertou o número {gerado} em 3 tentativas. Tente novamente!")
# %%
