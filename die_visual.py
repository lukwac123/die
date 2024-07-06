import plotly.express as px

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

# Wizualizacja wyników.
title = "Wynik rzucania pojedynczą kością D6 tysiąc razy."
labels = {'x': 'Wynik', 'y': 'Częstotliwość występowania wartości'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

print(frequencies)