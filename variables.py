#"l'opérateur d'affectation = permet d'injecter une valeur dans une variable"

# integer, nombre entier

my_number1 = 123
my_number2 = -42
my_number6 = 11
print(my_number1)
print(my_number2)
print(my_number6)
print(type(my_number6))

# float, nombre à virgule

my_number3 = 3.14
my_number4 = -2.71
# 0.0 0. ou .0
my_number5 = .0
print(my_number3)
print(my_number4)
print(my_number5)
print(type(my_number3))


# bool, booléen

my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)
print(type(my_boolean1))

# None, valeur nulle , quand on ne connait pas la valeur
# autres languages identique = null, nil

my_none = None
print(my_none)
print(type(my_none))

# strings, chaînes de caractères
# double quote ou simple quote, c'est pareil

my_text1 = "Ceci est une chaines de caratères"
my_text2 = 'Ceci est aussi une chaines de caratères'

print(my_text1)
print(my_text2)

# \ caractère d'échappement
# \n saut de ligne

my_text3 = "abc\ndef\nghi"
my_text4 = "\\"
my_text5 = "John \"Foo\" Doe" #on ajoute les backslash pour afficher les cotes de Foo
print(my_text3)
print(my_text4)
print(my_text5)

a = 123
b = 42
# permutation de la valeur des variables
a, b = b, a
print(a, b)


a = 123
b = 42

# à vous de jouer
a = 42
b = 123

# variante
c = a + b
a = c - a
b = c - b
print(a,b)