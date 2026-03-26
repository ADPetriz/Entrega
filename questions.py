import random

categorias = {
    "Programacion":["python","programa","variable","funcion","bucle","cadena","entero","lista"],
    "Vehiculos":["auto","avion","barco","helicoptero","moto","camioneta","camion","bicicleta"],
    "Comidas":["pizza","pancho","hamburguesa","ensalada","fideos","milanesa","albondigas","empanadas"],
    "Vestimentas":["remera","pantalon","corbata","pollera","vestido","zapatos","sombrero","medias"]}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías para jugar:")
print()

nombres_cat = list(categorias.keys())
num = 0
for nom in nombres_cat:
    num += 1
    print(f'{num}. {nom}')
print()

while True:
    while True:
        seleccion_str = input("Elegí el número de la categoría: ")

        if seleccion_str.isdigit():
            seleccion = int(seleccion_str)
        else:
            print("Entrada no válida. Elegí un número entero.")
            continue

        if 1 <= seleccion <= len(nombres_cat):
            categoria_elegida = nombres_cat[seleccion - 1]
            break
        else:
            print("Por favor, elegí un número de la lista.")
            
    print()

    palabras_disponibles = categorias[categoria_elegida]
    fila_de_palabras = random.sample(palabras_disponibles, len(palabras_disponibles))

    while len(fila_de_palabras) > 0:
        word = fila_de_palabras.pop()
        guessed = []
        attempts = 6
        puntaje = 0

        print(f"La categoría elegida es {categoria_elegida}")
        print()

        print('Nueva ronda')
        print(f'Palabras restantes en la categoría: {len(fila_de_palabras)+1}')
        print()

        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in word:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                puntaje += 6
                break
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            letter = input("Ingresá una letra: ")

            if len(letter) != 1 or not letter.isalpha():
                print("Entrada no válida")
                continue
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")

            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
                puntaje -= 1
            
            print()
        else:
            puntaje = 0
            print(f"¡Perdiste! La palabra era: {word}")
        print(f'Tu puntaje es {puntaje}')

        if len(fila_de_palabras) == 0:
                print('Jugaste todas las palabras de esta categoría.')
                print()
                break

        if len(fila_de_palabras) > 0:
                jugar_otra = input('Presiona "y" si querés jugar otra ronda de la misma categoría, si no presiona otra tecla: ')
                if jugar_otra != 'y':
                    break

    nueva_cat = input('Presiona "y" si querés jugar con las mismas palabras o cambiar de categoría, si no presiona otra tecla: ')    
    if nueva_cat != 'y':
        break