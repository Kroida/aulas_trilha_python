# Initial populations
pop_a = int(input('Digite a população do país A: '))
pop_b = int(input('Digite a população do país B: '))

# Growth rates
taxa_a = float(input('Digite a taxa de crescimento anual da população do país A (em %): ')) / 100
taxa_b = float(input('Digite a taxa de crescimento anual da população do país B (em %): ')) / 100

# Counter for years
anos = 0

# Calculate until population A reaches or surpasses population B
if pop_a < pop_b:
    while pop_a < pop_b:
        pop_a = pop_a + (pop_a * taxa_a)
        pop_b = pop_b + (pop_b * taxa_b)
        anos += 1
    print(f"Serão necessários {anos} ano(s) para a população do país A igualar ou ultrapassar a população do país B.")
else:
    print("A população do país A já é maior que a população do país B!")

print(f"População final do país A: {int(pop_a)} habitantes")
print(f"População final do país B: {int(pop_b)} habitantes")