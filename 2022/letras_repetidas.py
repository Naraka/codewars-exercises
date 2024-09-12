# Escriba una función que devuelva el recuento de caracteres alfabéticos distintos que no distinguen entre mayúsculas y minúsculas y dígitos numéricos que aparecen más de una vez en la cadena de entrada. Se puede suponer que la cadena de entrada contiene solo letras (tanto mayúsculas como minúsculas) y dígitos numéricos.

# Ejemplo
# "abcde" -> 0 # ningún carácter se repite más de una vez
# "aabbcde" -> 2 # 'a' y 'b'
# "aabBcde" -> 2 # 'a' ocurre dos veces y 'b' dos veces (`b` y `B`)
# "indivisibilidad" -> 1 # 'i' aparece seis veces
# "Indivisibilidades" -> 2 # 'i' ocurre siete veces y 's' ocurre dos veces
# "aA11" -> 2 # 'a' y '1'
# "ABBA" -> 2 # 'A' y 'B' cada uno ocurre dos veces







def duplicate_count(text):
    text=text.lower()

    result=""
    for i in text:
        if text.count(i) > 1 :
            result+=i

    print(len(set(result)))





duplicate_count("abcdeaB")