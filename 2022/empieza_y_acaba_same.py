
# Resultados de traducións
# ¡Todos los animales están teniendo un festín! Cada animal trae un plato. Solo hay una regla: el plato debe comenzar y terminar con las mismas letras que el nombre del animal. Por ejemplo, la gran garza azul trae pan de ajo y el carbonero trae pastel de chocolate.

# Escriba una función festín que tome el nombre del animal y el plato como argumentos y devuelva verdadero o falso para indicar si la bestia puede llevar el plato al festín.

# Suponga que bestia y plato siempre son cadenas en minúsculas y que cada una tiene al menos dos letras. bestia y plato pueden contener guiones y espacios, pero estos no aparecerán al principio o al final de la cadena. No contendrán numerales




def feast(beast, dish):
    print(beast.endswith(dish[-1]) and beast.startswith(dish[0]))






beast="great blue heron"
dish="garlic naan"


feast(beast,dish)


