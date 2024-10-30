import time
from quickSortT import quickSort, generate_random_array  # Importa as funções do arquivo quickSortT.py

def measure_time(sort_func, data):
    start_time = time.time()  # Inicia a contagem do tempo
    sort_func(data, 0, len(data) - 1)  # Chama a função quickSort
    end_time = time.time()  # Para a contagem do tempo
    return end_time - start_time  # Retorna o tempo decorrido

def main():
    # Valores manuais
    min_val = -1000
    max_val = 1000
    size = 1000

    # Gera o array aleatório
    data = generate_random_array(min_val, max_val, size)

    print("Array gerado:")
    print(data)

    # Medindo o tempo do Quicksort
    quick_time = measure_time(quickSort, data.copy())  # Cria uma cópia para manter os dados originais

    print(f"\nArray ordenado em ordem crescente:")
    print(data)
    print(f"\nQuicksort levou {quick_time:.5f} segundos para ordenar.")

if __name__ == "__main__":
    main()