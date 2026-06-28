#%%
##exercio de comprehension em listas que cria listas
## de formas interáveis utilizando o laço for na criação da lista


x = []

for i in range(1,101):
    x.append(i)

x

# %%

y = [i for i in range(1,101)]


#%%
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False
    

z = [par(i) for i in range(1,101)]
z
# %%

w= [i for i in range(1,101) if par(i)]
w