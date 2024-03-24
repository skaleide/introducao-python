# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.


preco_original = float(input("Digite o preço original do produto: "))
desconto_percentual = float(input("Digite o desconto percentual (%): "))

 
desconto_percentual = desconto_percentual/100
preco_final = preco_original * (1 - desconto_percentual / 100)

print("O preço final do produto após aplicar um desconto de", desconto_percentual, "% é:", preco_final)
