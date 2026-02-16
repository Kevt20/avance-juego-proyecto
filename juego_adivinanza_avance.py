"""
Juego de Adivinanza
Autor: Kevin Torres
Fecha: 15 de Febrero 2026
Proyecto para el curso de Lógica de Programación
"""

import random
import os

# Variable para guardar puntos
puntos = 0
partidas = 0

def limpiar():
    """Limpia la pantalla"""
    os.system('cls' if os.name == 'nt' else 'clear')

def adivinar_numero():
    """
    Juego principal: adivinar un número
    Aquí uso estructuras repetitivas (while) y condicionales (if/else)
    """
    global puntos, partidas
    
    print("\n=== ADIVINA EL NÚMERO ===\n")
    
    # Le pregunto al usuario la dificultad
    print("Elige la dificultad:")
    print("1. Fácil (número entre 1-50, 10 intentos)")
    print("2. Normal (número entre 1-100, 7 intentos)")
    print("3. Difícil (número entre 1-200, 5 intentos)")
    
    # Estructura repetitiva para validar la opción
    while True:
        try:
            dificultad = int(input("\nTu elección (1, 2 o 3): "))
            
            # Estructura condicional para asignar valores según dificultad
            if dificultad == 1:
                numero_maximo = 50
                intentos_maximos = 10
                break
            elif dificultad == 2:
                numero_maximo = 100
                intentos_maximos = 7
                break
            elif dificultad == 3:
                numero_maximo = 200
                intentos_maximos = 5
                break
            else:
                print("Opción no válida. Elige 1, 2 o 3.")
        except:
            print("Por favor ingresa un número válido.")
    
    # Genero el número aleatorio
    numero_secreto = random.randint(1, numero_maximo)
    intentos = 0
    
    print(f"\n¡Perfecto! Adivina el número entre 1 y {numero_maximo}")
    print(f"Tienes {intentos_maximos} intentos.\n")
    
    # Bucle principal del juego - Estructura repetitiva while
    while intentos < intentos_maximos:
        try:
            # Pido el intento al usuario
            intento = int(input(f"Intento {intentos + 1}/{intentos_maximos}: "))
            
            # Valido que esté en el rango
            if intento < 1 or intento > numero_maximo:
                print(f"El número debe estar entre 1 y {numero_maximo}!")
                continue
            
            intentos += 1
            
            # Estructuras condicionales para dar pistas
            if intento == numero_secreto:
                # ¡Ganó!
                print("\n" + "🎉" * 20)
                print(f"¡FELICIDADES! Adivinaste el número: {numero_secreto}")
                print(f"Lo lograste en {intentos} intentos")
                
                # Calculo puntos según los intentos que usó
                puntos_ganados = (intentos_maximos - intentos + 1) * 10
                puntos += puntos_ganados
                
                print(f"Ganaste {puntos_ganados} puntos")
                print("🎉" * 20)
                partidas += 1
                return True
                
            elif intento < numero_secreto:
                # El número es mayor
                diferencia = numero_secreto - intento
                
                if diferencia <= 5:
                    print("¡Casi! El número es un poquito más GRANDE")
                elif diferencia <= 15:
                    print("El número es MAYOR")
                else:
                    print("El número es MUCHO MAYOR")
                    
            else:
                # El número es menor
                diferencia = intento - numero_secreto
                
                if diferencia <= 5:
                    print("¡Casi! El número es un poquito más PEQUEÑO")
                elif diferencia <= 15:
                    print("El número es MENOR")
                else:
                    print("El número es MUCHO MENOR")
            
            # Muestro cuántos intentos quedan
            quedan = intentos_maximos - intentos
            if quedan > 0:
                print(f"Te quedan {quedan} intentos\n")
                
        except:
            print("Por favor ingresa un número válido.\n")
    
    # Si llegó aquí es porque se acabaron los intentos
    print("\n" + "😢" * 20)
    print(f"Se acabaron los intentos...")
    print(f"El número era: {numero_secreto}")
    print("😢" * 20)
    partidas += 1
    return False


def mostrar_estadisticas():
    """Muestra los puntos y partidas jugadas"""
    print("\n=== MIS ESTADÍSTICAS ===")
    print(f"Partidas jugadas: {partidas}")
    print(f"Puntos totales: {puntos}")
    
    # Estructura condicional para dar un "rango" según puntos
    if puntos < 50:
        print("Nivel: Principiante 🌱")
    elif puntos < 150:
        print("Nivel: Intermedio 📚")
    elif puntos < 300:
        print("Nivel: Avanzado 🎯")
    else:
        print("Nivel: Experto 👑")
    print()


def menu_principal():
    """
    Menú principal del juego
    Usa estructura repetitiva (while True) y condicionales (if/elif/else)
    """
    limpiar()
    
    print("=" * 40)
    print("  JUEGO DE ADIVINANZA - Kevin Torres")
    print("=" * 40)
    
    # Pido el nombre
    nombre = input("\n¿Cómo te llamas? ")
    print(f"\n¡Hola {nombre}! Bienvenido al juego\n")
    input("Presiona ENTER para continuar...")
    
    # Bucle principal del menú - Estructura repetitiva
    while True:
        limpiar()
        print("=" * 40)
        print(f"  JUGADOR: {nombre}")
        print(f"  PUNTOS: {puntos}")
        print("=" * 40)
        
        print("\nMENÚ PRINCIPAL:")
        print("1. Jugar (Adivina el número)")
        print("2. Ver mis estadísticas")
        print("3. Salir")
        
        # Estructura condicional para el menú
        opcion = input("\n¿Qué quieres hacer? (1, 2 o 3): ")
        
        if opcion == "1":
            adivinar_numero()
            input("\nPresiona ENTER para continuar...")
            
        elif opcion == "2":
            mostrar_estadisticas()
            input("Presiona ENTER para continuar...")
            
        elif opcion == "3":
            print("\n¡Gracias por jugar!")
            print(f"Puntos finales: {puntos}")
            print(f"Partidas jugadas: {partidas}")
            print("\n¡Hasta pronto! 👋\n")
            break
            
        else:
            print("\nOpción no válida. Por favor elige 1, 2 o 3.")
            input("Presiona ENTER para continuar...")


# INICIO DEL PROGRAMA
if __name__ == "__main__":
    menu_principal()


# NOTAS DE DESARROLLO:
# - Ya funciona el modo de adivinar números con diferentes dificultades
# - Falta agregar más modos de juego (palabras, matemáticas)
# - Falta mejorar el sistema de puntos
# - Pendiente: guardar las estadísticas en un archivo
