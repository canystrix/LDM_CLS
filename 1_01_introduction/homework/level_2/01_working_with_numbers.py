# *** LEVEL 2 - ARBEITEN MIT ZAHLEN *** #
# Der Umgang mit Zahlen ist eines der wichtigsten Mittel der Sofwareentwicklung.
# Es ist wichtig, den richtigen Umgang mit ihnen zu üben und zu verstehen.
# So können wir später zum Beispiel Stringlängen miteinander vergleichen oder Durchschnitte ermitteln!
# Im Folgenden werden einige Zahlen definiert, mit denen wir verschiedene Operationen ausführen wollen.

sample_number_1 = 1
sample_number_2 = 5
sample_number_3 = 2.5
sample_number_4 = -5


# AUFGABE 1
# Verändern sie die Variablen in den folgenden Vergleichen so, dass die Vergleiche True ausgeben!
# Nutzen Sie dafür die oben definierten Variablen!
# Ändern Sie weder Werte der Variablen, noch die Operatoren!

#print(sample_number_1 != sample_number_1)
#print(sample_number_3 == sample_number_2)
#print(sample_number_1 < sample_number_4)
#print(sample_number_4 > sample_number_2)

print(sample_number_1 != sample_number_2)
print(sample_number_3 == sample_number_2-sample_number_3)
print(sample_number_1 < sample_number_2)
print(sample_number_4 > sample_number_2-11)
# Replace variables in the comparisons to make all expressions return True

# AUFGABE 2
# Nutzen Sie die zuvor definierten Variablen für die folgenden arithmetischen Operationen um zu...

# Addieren
# sample_sum = 0
sample_sum = sample_number_4+sample_number_3
# Subtrahieren
# sample_difference = 0
sample_difference = sample_number_2-sample_number_1
# Multiplizieren
# sample_product = 0
sample_product = sample_number_4 * sample_number_2
# Dividieren
# sample_quotient = 0
sample_quotient = sample_number_2 / sample_number_1
# Use arithmetic operations on the variables


# ...sodass bei den folgenden Vergleichen True ausgeben wird!
print(sample_sum == -2.5)
print(sample_difference == 4)
print(sample_product == -25)
print(sample_quotient == 5.0)


# AUFGABE 3
# Ersetzen Sie die Variablen in den folgenden Berechnungen mit anderen zuvor definierten Variablen!
# Ziel ist es wieder, über die Print-Funktion True auszugeben!

# print(sample_number_4 - 5 == 0)
# print((2 + sample_number_4) - 1 == 2)
# print(sample_number_1**2 - 5 == 20)
# print(5 - sample_number_1 * 4 == -5)

print(sample_number_4 - -sample_quotient == 0)
print((2 + sample_number_1) - 1 == 2)
print(sample_quotient**2 - 5 == 20)
print(5 - sample_number_3 * 4 == -5)

# Substitute the hardcoded numbers with variables to make the equations return True