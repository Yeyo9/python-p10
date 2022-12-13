# exo 3.9
# Charly fait ses courses.
# Il compare le prix de deux marques différentes de chocolat.
# La marque Alpha propose une tablette à 2,00 euros (pour 120 g).
# La marque Beta propose une tablette à 1,70 euros (pour 100 g).
# Charly a l'intuition que la marque Alpha est plus avantageuse.
# A-t-il raison ?
# Calculez d'abord le poid au kilo (convertir les grammes en kilo donc) et stockez les résultats dans les variables `weight_alpha` et `weight_beta`.
# Puis calculez le prix au kilo avec les variables `price_alpha` et `weight_alpha`, et `price_beta` et `weight_beta` respectivement puis stockez les résultat dans les variables `price_per_kilo_alpha` et `price_per_kilo_beta`.
# Utilisez un opérateur de comparaison (qui doit donc renvoyer une valeur booléenne) pour vérifier si Charly a raison.
# Affichez le résultat booléen.

price_alpha = 2.00
price_beta = 1.70


weight_alpha = 0.12
weight_beta =  0.10

price_per_kilo_alpha = price_alpha * 100 / weight_alpha
print(price_per_kilo_alpha)
réponse = 1666.6666666666667 

price_per_kilo_beta = price_beta * 100 / weight_beta
print(price_per_kilo_beta)
réponse = 1700.0 

alpha = True
beta = False
print(alpha)
