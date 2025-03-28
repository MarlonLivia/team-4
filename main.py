1#
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)#Ejecucion del factorial
print (factorial(4))#el print#
2#
def Potencia(x,n):
    if n==0:
        return 1
    else:
        return x*Potencia(x,n-1)
print(Potencia(2,3))
3#
def Suma_digito(n):
    if n<10:
        return n
    return (n%10) + Suma_digito(n//10)
print(Suma_digito(14))
4#
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    if len(cadena) <= 1:
        return True
    if cadena[0] == cadena[-1]:
        return es_palindromo(cadena[1:-1])
    
    return False    
print(es_palindromo("aaplllaa")) 
5#
def invertir_cadena(cadena):
    if len(cadena)==0:
        return ""
    return cadena[-1] + invertir_cadena(cadena[:-1])

print(invertir_cadena("Marlon"))
6#
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0]+suma_lista(lista[1:])

print(suma_lista([1,2,3,4]))
7#
def Fibonacci(n):
    if n<=1:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(5))

#Estructura 1
def generar_binarios(cadena, N):
    # Caso base: cuando la longitud de la cadena es N
    if len(cadena) == N:
        print(cadena)
        return
    
    # Tomamos dos decisiones en cada paso
    generar_binarios(cadena + '0', N)  # Añadir '0' y hacer recursión
    generar_binarios(cadena + '1', N)  # Añadir '1' y hacer recursión

# Función para iniciar la recursión
def generar_binarios_inicial(N):
    generar_binarios("", N)

# Llamada para generar cadenas binarias de longitud 3
generar_binarios_inicial(3)

#Estructura 2
def generar_tf(cadena, N):
    # Caso base: cuando la longitud de la cadena es N
    if len(cadena) == N:
        print(cadena)
        return
    
    # Tomamos dos decisiones en cada paso
    generar_tf(cadena + 'T', N)  # Añadir 'T' y hacer recursión
    generar_tf(cadena + 'F', N)  # Añadir 'F' y hacer recursión

# Función para iniciar la recursión
def generar_tf_inicial(N):
    generar_tf("", N)

# Llamada para generar cadenas de T/F de longitud 3
generar_tf_inicial(3)

#Estructura3
def generar_numeros(n, cadena=""):
    if len(cadena) == n:
        print(cadena)
        return
    for digito in "123":
        generar_numeros(n, cadena + digito)
# Ejemplo con N = 3
print(generar_numeros(3))
