# Inicializando as variáveis
menor_peso = float('inf')  # Inicializa com infinito para garantir que qualquer peso inserido seja menor
maior_peso = float('-inf')  # Inicializa com menos infinito para garantir que qualquer peso inserido seja maior

# Loop para obter os pesos
for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))
    
    # Atualizando o menor e o maior peso
    menor_peso = min(menor_peso, peso)
    maior_peso = max(maior_peso, peso)

# Exibindo os resultados
print(f"\nO menor peso foi: {menor_peso} kg")
print(f"O maior peso foi: {maior_peso} kg")
