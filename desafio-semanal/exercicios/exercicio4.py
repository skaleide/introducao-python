# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.


def contar_frutas(lista_frutas):
    contagem_frutas = {}
    for fruta in lista_frutas:
        contagem_frutas[fruta] = contagem_frutas.get(fruta, 0) + 1
    return contagem_frutas

def main():
   
    lista_frutas = ["Maçã", "Banana", "Maçã", "Pera", "Banana", "Maçã", "Laranja", "Pera"]

  
    contagem = contar_frutas(lista_frutas)

   
    print("Contagem de frutas:")
    for fruta, quantidade in contagem.items():
        print(fruta + ":", quantidade)

if __name__ == "__main__":
    main()
