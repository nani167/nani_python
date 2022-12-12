texto = input("Bienvenido a mi analizador de textos, por favor ingresa un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Por favor ingresa la primera letra: ").lower())
letras.append(input("Por favor ingresa la segunda letra: ").lower())
letras.append(input("Por favor ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cant_letras1 = texto.count(letras[0])
cant_letras2 = texto.count(letras[1])
cant_letras3 = texto.count(letras[2])

print(f"Encontramos la letra '{letras[0]}' repetida {cant_letras1} veces")
print(f"Encontramos la letra '{letras[1]}' repetida {cant_letras2} veces")
print(f"Encontramos la letra '{letras[2]}' repetida {cant_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Encontramos {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_fin}'")

print("\n")
print("El texto invertido se ve de la siguiente manera")
palabras.reverse()
text_invertido = ' '.join(palabras)
print(f"Si ordeno tu texto al reves va decir: '{text_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
find_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python'{dic[find_python]} esta en el texto")

