# Juego de Adivinanza

**Nombre:** Kevin Jimenez  
**Curso:** Lógica de Programación  
**Fecha:** 15 de Febrero 2026

---

## ¿Qué es este proyecto?

Es un juego simple donde tienes que adivinar un número. Lo hice para practicar lo que estoy aprendiendo en el curso de programación.

---

## ¿Cómo funciona?

1. El juego te pide tu nombre
2. Escoges la dificultad (fácil, normal o difícil)
3. Tienes que adivinar un número
4. El juego te da pistas: si es más grande o más pequeño
5. Ganas puntos si adivinas

---

## ¿Cómo usar el programa?

1. Abre la terminal o consola
2. Ve a la carpeta donde está el archivo
3. Escribe: `python juego_adivinanza.py`
4. ¡A jugar!

---

## Lo que incluye el proyecto

### Ya funciona:
- Un modo de juego: adivinar números
- Tres niveles de dificultad
- Sistema de puntos
- Pistas que te ayudan
- Estadísticas básicas

###  Todavía en desarrollo:
- Más modos de juego (palabras, operaciones)
- Mejorar las estadísticas
- Guardar los puntajes en un archivo

---

## Estructuras de programación que usé

### Estructuras repetitivas (bucles):
- **While** para validar las opciones del menú
- **While** para el juego principal (los intentos)
- **While** para pedir el nivel de dificultad

### Estructuras condicionales:
- **If/elif/else** para el menú
- **If/elif/else** para las dificultades
- **If/elif/else** para dar pistas (mayor o menor)
- **If/elif** para calcular el nivel del jugador

### Validación de datos:
- Try-except para cuando el usuario escribe algo que no es número
- Validación de rangos (que el número esté entre 1 y el máximo)

---

## Ejemplo de uso

```
=== ADIVINA EL NÚMERO ===

Elige la dificultad:
1. Fácil (número entre 1-50, 10 intentos)
2. Normal (número entre 1-100, 7 intentos)
3. Difícil (número entre 1-200, 5 intentos)

Tu elección (1, 2 o 3): 2

¡Perfecto! Adivina el número entre 1 y 100
Tienes 7 intentos.

Intento 1/7: 50
El número es MAYOR

Intento 2/7: 75
¡Casi! El número es un poquito más PEQUEÑO

Intento 3/7: 73
¡FELICIDADES! Adivinaste el número: 73
Lo lograste en 3 intentos
Ganaste 50 puntos
```

---

## Lo que aprendí

- Cómo usar bucles while para repetir acciones
- Cómo usar if/elif/else para tomar decisiones en el código
- Cómo validar lo que escribe el usuario
- Cómo hacer que un programa sea interactivo
- Cómo organizar el código en funciones
- Cómo usar variables globales para guardar datos

---

## Próximos pasos

Quiero mejorar el juego agregando:
1. Un modo de adivinar palabras
2. Un modo de resolver operaciones matemáticas
3. Poder guardar los puntajes
4. Hacer que sea más visual

---

## Notas

Este es mi primer proyecto grande de programación. Sé que le falta bastante pero estoy orgulloso de lo que he logrado hasta ahora. Voy a seguir mejorándolo.
