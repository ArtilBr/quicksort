# teste_quicksort.py

import time
from quickSort import quickSortT, generate_random_array  # Importa as funções do arquivo quickSort.py

def measure_time(sort_func, data):
    start_time = time.time()
    sort_func(data, 0, len(data) - 1)  # Chama a função quickSort
    end_time = time.time()
    return end_time - start_time

def main():
    # Valores manuais
    min_val = -1000
    max_val = 1000
    size = 1000

    # Gera o array aleatório
    data = generate_random_array(min_val, max_val, size)

    # Medindo o tempo do Quicksort
    print("Array gerado:")
    print(data)

    quick_time = measure_time(quickSortT, data.copy())  # Cria uma cópia para manter os dados originais

    print(f"\nArray ordenado em ordem crescente:")
    print(data)
    print(f"\nQuicksort levou {quick_time:.5f} segundos para ordenar.")

if __name__ == "__main__":
    main()
