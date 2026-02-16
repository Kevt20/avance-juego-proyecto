# Análisis del Proyecto - Juego de Adivinanza

**Estudiante:** Kevin Torres  
**Curso:** Lógica de Programación  
**Fecha:** 15 de Febrero 2026

---

## Introducción

Este documento explica lo que hice en mi proyecto y por qué lo hice así. Es un juego simple de adivinar números que programé para practicar lo que estoy aprendiendo en clase.

---

## ¿Qué quería lograr?

Mi objetivo principal era hacer un programa que funcionara y que usara las cosas que estamos viendo en clase:
- Bucles (while y for)
- Condicionales (if, elif, else)
- Funciones
- Validación de datos

También quería que fuera algo que realmente se pudiera jugar y que no fuera aburrido.

---

## ¿Cómo lo desarrollé?

### Paso 1: La idea
Primero pensé qué tipo de juego hacer. Me decidí por adivinar números porque es simple pero permite usar todas las estructuras que necesito demostrar.

### Paso 2: El código básico
Empecé haciendo que el juego funcionara de forma básica:
1. Generar un número aleatorio
2. Pedirle al usuario que adivine
3. Decirle si acertó o no

### Paso 3: Mejoras
Después fui agregando cosas:
- Niveles de dificultad
- Pistas más útiles (muy cerca, cerca, lejos)
- Sistema de puntos
- Un menú para poder jugar varias veces

### Paso 4: Validaciones
Al final agregué validaciones para que el programa no se rompa si el usuario escribe algo mal.

---

## Estructuras de programación que usé

### 1. Estructuras repetitivas (While)

**¿Dónde las usé?**
- En el menú principal (para que siga funcionando hasta que el usuario quiera salir)
- En el juego (para los intentos de adivinar)
- Para validar las opciones del usuario

**Ejemplo del código:**
```python
while intentos < intentos_maximos:
    intento = int(input("Tu intento: "))
    
    if intento == numero_secreto:
        print("¡Ganaste!")
        break
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    intentos += 1
```

**¿Por qué es importante?**
El while me permite repetir el proceso de pedir un número hasta que se acaben los intentos o el usuario acierte.

---

### 2. Estructuras condicionales (If/Elif/Else)

**¿Dónde las usé?**
- Para el menú (opción 1, 2 o 3)
- Para las dificultades
- Para dar las pistas
- Para calcular el nivel del jugador

**Ejemplo del código:**
```python
if dificultad == 1:
    numero_maximo = 50
    intentos_maximos = 10
elif dificultad == 2:
    numero_maximo = 100
    intentos_maximos = 7
else:
    numero_maximo = 200
    intentos_maximos = 5
```

**¿Por qué es importante?**
Los condicionales me dejan tomar decisiones en el programa. Según lo que elija el usuario, el programa hace cosas diferentes.

---

### 3. Validación de datos

**¿Qué validé?**
- Que el usuario ingrese números y no letras
- Que los números estén en el rango correcto
- Que las opciones del menú sean válidas

**Ejemplo del código:**
```python
try:
    intento = int(input("Tu intento: "))
    
    if intento < 1 or intento > numero_maximo:
        print("El número debe estar en el rango!")
        continue
        
except:
    print("Por favor ingresa un número válido")
```

**¿Por qué es importante?**
Si no valido los datos, el programa puede dar error y cerrarse. Con las validaciones me aseguro de que funcione bien aunque el usuario escriba algo mal.

---

## Desafíos que tuve

### Problema 1: Las pistas no eran muy útiles
**Qué pasaba:** Al principio solo decía "mayor" o "menor" pero eso no ayudaba mucho.

**Cómo lo resolví:** Agregué tres niveles de pistas:
- "Un poquito más grande/pequeño" (si está a 5 o menos)
- "Mayor/Menor" (si está entre 5 y 15)
- "MUCHO mayor/menor" (si está a más de 15)

### Problema 2: No sabía cómo calcular los puntos
**Qué pasaba:** No tenía claro cómo dar puntos de forma justa.

**Cómo lo resolví:** Decidí dar más puntos si aciertas en menos intentos. La fórmula es simple:
```
puntos = (intentos que sobraron + 1) x 10
```

### Problema 3: El código se veía desordenado
**Qué pasaba:** Al principio todo estaba en un solo bloque y era difícil de entender.

**Cómo lo resolví:** Separé el código en funciones:
- Una función para el juego
- Una función para el menú
- Una función para las estadísticas

---

## Lo que funciona bien

✅ El juego funciona sin errores  
✅ Las validaciones evitan que se rompa  
✅ Las pistas ayudan a adivinar más rápido  
✅ Se puede jugar varias veces seguidas  
✅ El sistema de puntos funciona  

---

## Lo que me falta hacer

🚧 Agregar más modos de juego  
🚧 Guardar los puntajes en un archivo  
🚧 Hacer una interfaz más bonita  
🚧 Agregar sonidos o colores  

---

## Reflexión personal

### ¿Qué aprendí?

Lo más importante que aprendí es que programar es como resolver un rompecabezas. Tienes que ir pieza por pieza. Al principio me parecía complicado pero cuando empecé a dividirlo en partes pequeñas se volvió más fácil.

También aprendí que es súper importante probar el código muchas veces. Encontré varios errores solo probando cosas raras (como poner letras donde van números).

### ¿Qué fue lo más difícil?

Lo más difícil fue organizar el código. Al principio tenía todo mezclado y cuando quería cambiar algo tenía que buscar en un montón de líneas. Cuando lo separé en funciones fue mucho más fácil.

### ¿Qué mejoraría?

Si tuviera más tiempo, me gustaría:
1. Hacer que se vea mejor visualmente
2. Agregar un modo multijugador
3. Hacer que guarde un historial de partidas
4. Agregar logros o medallas

---

## Conclusión

Este proyecto me ayudó a entender mejor cómo funcionan los bucles, los condicionales y las validaciones. Sé que todavía me falta mucho por aprender pero estoy contento con lo que logré.

Lo más importante es que el juego funciona y que apliqué lo que estamos viendo en clase. Ahora entiendo por qué son importantes estas estructuras y cómo se usan en un programa real.

---

## Recursos que usé

- Apuntes de clase sobre while y if/else
- La documentación de Python para la función random
- Ayuda de compañeros para entender algunos conceptos
- Mucha prueba y error

---

**Nota:** Este es un proyecto en desarrollo. Voy a seguir mejorándolo conforme aprenda más cosas en el curso.
