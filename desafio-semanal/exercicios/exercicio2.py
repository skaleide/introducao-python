# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

def preco_total(preco_frutas) :
     total = sum(preco_frutas)
     return total

def main():
  preco_frutas = {}

  while True:
   fruta = input("Digite nome da fruta ou digiti 'fim'para encerrar")

   if fruta == 'fim':
     break
   preco = float(input(" Digite o valor da fruta '{fruta}'"))
   preco_frutas[fruta] = preco

   total = preco_total(preco_frutas)
   print("Preco total", total)
  
