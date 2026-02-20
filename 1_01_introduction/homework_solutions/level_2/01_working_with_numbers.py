# *** LEVEL 2 - ARBEITEN MIT ZAHLEN *** #
# Der Umgang mit Zahlen ist eines der wichtigsten Mittel der Softwareentwicklung.
# Es ist wichtig, den richtigen Umgang mit ihnen zu üben und zu verstehen.
# So können wir später zum Beispiel Stringlängen miteinander vergleichen oder Durchschnitte ermitteln!
# Im Folgenden werden einige Zahlen definiert, mit denen wir verschiedene Operationen ausführen wollen.

sample_number_1 = 1
# korrekt

sample_number_2 = 5
# korrekt

sample_number_3 = 2.5
# korrekt

sample_number_4 = -5
# korrekt


# AUFGABE 1
# Verändern sie die Variablen in den folgenden Vergleichen so, dass die Vergleiche True ausgeben!
# Nutzen Sie dafür die oben definierten Variablen!
# Ändern Sie weder Werte der Variablen, noch die Operatoren!

# print(sample_number_1 != sample_number_1)
# != bedeutet "ungleich". sample_number_1 ist gleich sample_number_1, daher wird das False.
# daher ⮟
print(sample_number_1 != sample_number_2)

# print(sample_number_3 == sample_number_2)
# == bedeutet "gleich". sample_number_3 ist nicht gleich sample_number_2.
# daher ⮟
print(sample_number_3 == sample_number_3)

# print(sample_number_1 < sample_number_4)
# < bedeutet "kleiner als". 1 ist nicht kleiner als -5.
# daher ⮟
print(sample_number_1 < sample_number_2)

# print(sample_number_4 > sample_number_2)
# > bedeutet "größer als". -5 ist nicht größer als 5.
# daher ⮟
print(sample_number_2 > sample_number_4)


# AUFGABE 2
# Nutzen Sie die zuvor definierten Variablen für die folgenden arithmetischen Operationen um zu...

# Addieren
# sample_sum = 0
# sample_sum muss = -2.5 sein.
# daher ⮟
sample_sum = sample_number_3 + sample_number_4

# Subtrahieren
# sample_difference = 0
# sample_difference muss = 4 sein.
# daher ⮟
sample_difference = sample_number_2 - sample_number_1

# Multiplizieren
# sample_product = 0
# sample_product muss = -25 sein.
# daher ⮟
sample_product = sample_number_4 * sample_number_2

# Dividieren
# sample_quotient = 0
# sample_quotient muss = 5.0 sein.
# daher ⮟
sample_quotient = sample_number_2 / sample_number_1

print(sample_sum == -2.5)
print(sample_difference == 4)
print(sample_product == -25)
print(sample_quotient == 5.0)


# AUFGABE 3
# Ersetzen Sie die Variablen in den folgenden Berechnungen mit anderen zuvor definierten Variablen!
# Ziel ist es wieder, über die Print-Funktion True auszugeben!

# print(sample_number_4 - 5 == 0)
# sample_number_4 ist -5, daher ergibt -5 - 5 = -10 und damit False.
# Wir brauchen eine Zahl, die minus 5 genau 0 ergibt. Das ist sample_number_2 (5), da 5 - 5 = 0.
# daher ⮟
print(sample_number_2 - 5 == 0)

# print((2 + sample_number_4) - 1 == 2)
# Damit es True wird, muss (2 + X) - 1 genau 2 ergeben. Das klappt nur, wenn X = 1 ist.
# daher ⮟
print((2 + sample_number_1) - 1 == 2)

# print(sample_number_1**2 - 5 == 20)
# Damit es True wird, muss X**2 - 5 = 20 sein, also X**2 = 25 und damit X = 5.
# daher ⮟
print(sample_number_2**2 - 5 == 20)

# print(5 - sample_number_1 * 4 == -5)
# Damiit es True wird, muss 5 - X*4 = -5 sein, also X*4 = 10 und damit X = 2.5.
# daher ⮟
print(5 - sample_number_3 * 4 == -5)
