#%%
A=1
B=5

A,B=B,A

print(A)
print(B)
# %%


a, b, *_ = [1, 2, 3, 4, 5]

print(a,b,_)
# %%

a, *_, b = [1, 2, 3, 4, 5]

print(a,b,_)
# %%

def soma(a, *args):
    return a + sum(args)

resultado = soma(1, 2, 3, 4, 5)
print(resultado)
# %%

def somaquatro(a, b, c, d):
    return a + b + c + d

values = [1, 2, 3, 4]
somaquatro(*values)

# %%
