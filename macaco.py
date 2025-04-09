import string
import random
import timeit
from datetime import datetime

def write_initial_data(file, true_string):
    file.write("A String foi: " + true_string + '\n')

def get_user_input():
    return input('Enter a string in lowercase only: ')

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for _ in range(length))

def calculate_score(true_string, random_string):
    # Divide as strings em listas de palavras
    true_words = set(true_string.split())
    random_words = set(random_string.split())

    # Calcula o percentual de coincidência entre as palavras
    match_count = len(true_words & random_words)
    total_words = len(true_words)
    
    # Retorna a pontuação em percentual
    return (match_count / total_words) * 100 if total_words > 0 else 0

def main():
    true_string = get_user_input()
    length = len(true_string)
    score_update = 0
    run = 0

    # Cria um arquivo para armazenar as palavras geradas com o nome da string de entrada
    random_words_file = open(f"{true_string}.txt", 'w')

    with open('Macacada.txt', 'w') as file:
        write_initial_data(file, true_string)
        
        while score_update != 100:
            random_string = generate_random_string(length)
            print(random_string)  # Exibe cada combinação gerada
            random_words_file.write(random_string + '\n')  # Salva cada palavra gerada no arquivo
            score_update = calculate_score(true_string, random_string)
            run += 1

        
        file.write(f'\nProbabilidade é /{run}\n')

    random_words_file.close()
    return run

# Registro do tempo de início
start_datetime = datetime.now()

# Execução do programa
start_time = timeit.default_timer()
runs = main()
end_time = timeit.default_timer()

# Registro do tempo de término
end_datetime = datetime.now()

# Cálculo da probabilidade
probability = 1 / runs if runs > 0 else 0

# Exibe a probabilidade e o tempo total quando a palavra é encontrada
print(f"Probabilidade é: 1/{runs} ({probability:.10f})")
print(f"Total Time: {end_time - start_time:.2f} seconds")
print(f"Start Date and Time: {start_datetime}")
print(f"End Date and Time: {end_datetime}")

# Registro do tempo, probabilidade e data e hora no arquivo resultado.txt
with open('resultado.txt', 'a') as result_file:
#    result_file.write(f'Palavra: {true_string} \n')
    result_file.write(f'Start Date and Time: {start_datetime}\n')
    result_file.write(f'Stop Date and Time: {end_datetime}\n')
    result_file.write(f'Total Runs: {runs}\n')
    result_file.write(f'Probabilidade da palavra ser digitada: 1/{runs} ({probability:.10f})\n')
    result_file.write(f'Total Time: {end_time - start_time:.2f} seconds\n')
    result_file.write(f'----------------------------------------\n')
