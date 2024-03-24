# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def main():

    frutas = ["Banana", "Maçã", "Abacaxi", "Pera", "Uva"]

 
    frutas.sort(key=str.lower)


    print("Lista de frutas ordenada em ordem alfabética:")
    for fruta in frutas:
        print(fruta)

if __name__ == "__main__":
    main()
