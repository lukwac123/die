import plotly.express as px

from die import Die

# Utworzenie dwóch kości do gry typu D6..
die_1 = Die()
die_2 = Die()

# Wykonanie pewnej liczby rzutów i umiezczenie wyników na liście.
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
title = "Wynik rzucania dwiema kośćmi D6 tysiąc razy."
labels = {'x': 'Wynik', 'y': 'Częstotliwość występowania wartości'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Dalsze dostosowywanie wykresu do własnych potrzeb.
fig.update_layout(xaxis_dtick=1)

fig.show()

print(frequencies)