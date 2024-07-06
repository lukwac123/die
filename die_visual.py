from die import Die

# Utworzenie kości typu D6.
die = Die()

# Wykonanie pewnej liczby rzutów i umiezczenie wyników na liście.
results = []
for roll_num in range(1_000):
    result = die.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)