import random

# Função para encontrar a posição de partição
def partition(array, low, high):
    # Escolhe o elemento do meio como pivô
    middle = (low + high) // 2
    pivot = array[middle]

    # Move o pivô para o final para reutilizar a lógica
    array[middle], array[high] = array[high], array[middle]

    # Ponteiro para o maior elemento
    i = low - 1

    # Percorre todos os elementos e compara com o pivô
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            # Troca o elemento em i com o elemento em j
            array[i], array[j] = array[j], array[i]

    # Troca o pivô com o elemento maior especificado por i
    array[i + 1], array[high] = array[high], array[i + 1]

    # Retorna a posição de partição
    return i + 1

# Função para executar o Quicksort
def quickSort(array, low, high):
    if low < high:
        # Encontra o elemento pivô tal que elementos menores que o pivô
        # estejam à esquerda e os maiores à direita
        pi = partition(array, low, high)

        # Chamada recursiva à esquerda do pivô
        quickSort(array, low, pi - 1)

        # Chamada recursiva à direita do pivô
        quickSort(array, pi + 1, high)

# Função principal
def main():
    # Entrada do usuário para limites e tamanho do array
    min_val = int(input("Digite o valor mínimo para o intervalo de números: "))
    max_val = int(input("Digite o valor máximo para o intervalo de números: "))
    size = int(input("Digite o tamanho do array: "))
    test_count = int(input("Digite a quantidade de testes: "))

    for test in range(1, test_count + 1):
        # Gera o array aleatório com valores entre min_val e max_val
        data = [random.randint(min_val, max_val) for _ in range(size)]
        print(f"\nArray gerado no teste {test}:")
        print(data)

        # Ordena o array
        quickSort(data, 0, len(data) - 1)

        print(f"\nArray ordenado em ordem crescente no teste {test}:")
        print(data)

# Chamada da função principal
if __name__ == "__main__":
    main()