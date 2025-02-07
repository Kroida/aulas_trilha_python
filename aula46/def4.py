# Initial populations
pop_a = 80000
pop_b = 200000

# Growth rates
taxa_a = 0.03  # 3%
taxa_b = 0.015  # 1.5%

# Counter for years
anos = 0

# Calculate until population A reaches or surpasses population B
while pop_a < pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1
    
    # Optional: print yearly progress
    print(f"Ano {anos}:")
    print(f"População A: {int(pop_a)}")
    print(f"População B: {int(pop_b)}\n")

print(f"Serão necessários {anos} anos para a população do país A igualar ou ultrapassar a população do país B.")
print(f"População final do país A: {int(pop_a)} habitantes")
print(f"População final do país B: {int(pop_b)} habitantes")