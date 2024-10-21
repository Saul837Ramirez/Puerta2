"""
Diseñe un programa de control lógico, para habilitar-deshabilitar el seguro del 
picaporte y,o pasador de dos cerraduras electromecánicas.

Se tiene que cada cerradura tiene:

La primer cerradura electomecánica tiene CUATRO entradas {A,B,C,D} y una salida {Seguro}.

Proposiciones de entrada:
		La entrada (A) activa en ALTO, cuando la cerradura detecta la presencia de la llave
		en el interior del cilindro de la cerradura.
		La entrada (B) activa en ALTO, indica la COINCIDENCIA de combinaciones mecánicas de
		la llave y la cerradura electromecánica.  
		La entrada (C) activa en BAJO, indica perilla/manija en posición de apertura.
		La entrada (D) activa en ALTO, indica la validación de liberación del pasador de la 
		segunda cerradura electrónica.
	
Predicado de salida:
		Libera/bloquea el pasador/picaporte de la cerradura electromecánica.

Parámetros proposicionales en CIERTO.		
					SI, la entrada (A) en ALTO y la entrada (B) en ALTO
					SI, la entrada (C) en BAJO y las DOS entradas (A) y (B) 
					en ALTO.	  								  
					SI, la entrada (D) en CIERTO y la entrada (A)y(B)y(C) 
					en alto.    
Por lo que:
Se libera el pasador/picaporte de la cerradura electromecánica y
mostrar en el estandárt de salida el valor de msg.
					
Caso contrario 
	Se bloquea el pasador/picaporte de la primer cerradura electromecánica.
	
La segunda cerradura electromecánica tiene:
		TRES entradas {A,B,C} y una salida {D}.
		
Parámetros proposicionales en CIERTO.
		La entrada (A) activa en ALTO, cuando la cerradura detecta la presencia de la llave
		en el interior del cilindro.
		La entrada (B) activa en BAJO, indica la COINCIDENCIA de combinaciones mecánicas de
		la llave y la cerradura electromecánica.  
		La entrada (C) activa en BAJO, indica perilla/manija en posición de apertura.	
		
Por lo que:
Se libera el pasador/picaporte de la cerradura electromecánica y se asegura el valor de 
verdad en CIERTO para la entrada (D) de la primer cerradura.

Crea y reconoce Expresiones Regulares para solucionar problemas del entorno.-
"""
"""plantillaMain.py Contiene una función main() para ejecutar func1iones
Descripción.
"""
import time
import sys

msg = str("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")

def echo() -> str:
    """Retorna la hora actual como cadena."""
    return time.ctime()

def verificar_cerradura_1(A1: int, B1: int, C1: int, T2: int) -> str:
    """Verifica el estado de la primera cerradura y retorna un mensaje."""
    if (A1 == 1 and B1 == 1) or (C1 == 0 and A1 == 1 and B1 == 1) or (T2 == 1 and A1 == 1 and B1 == 1 and C1 == 0):
        return f"Cerradura 1 desbloqueada, mensaje: {msg}"
    else:
        return "Cerradura 1 bloqueada"

def verificar_cerradura_2(A2: int, B2: int, C2: int) -> (str, int):
    """Verifica el estado de la segunda cerradura y retorna un mensaje y su salida."""
    if A2 == 1 and B2 == 0 and C2 == 0:
        return "Cerradura 2 abierta", 1  # Mensaje y salida 1 (abierta)
    else:
        return "Cerradura 2 cerrada", 0  # Mensaje y salida 0 (cerrada)

def ejecutar_cerraduras() -> None:
    """Ejecuta la verificación de ambas cerraduras."""
    # Entradas de la primera cerradura
    A1 = 1  # ALTO
    B1 = 1  # ALTO
    C1 = 0  # BAJO

    # Entradas de la segunda cerradura
    A2 = 1  # ALTO
    B2 = 0  # BAJO
    C2 = 0  # BAJO

    # Mensajes para la segunda cerradura y su salida
    print("Ejecutando Cerradura 2...")
    mensaje_cerradura_2, T2 = verificar_cerradura_2(A2, B2, C2)
    print(mensaje_cerradura_2)  # Mostrar mensaje de la segunda cerradura

    # Mensajes para la primera cerradura
    print("Ejecutando Cerradura 1...")
    print(verificar_cerradura_1(A1, B1, C1, T2))  # Pasar T2 en lugar de D1

def main() -> int:
    """Función principal que controla la ejecución del programa."""
    ejecutar_cerraduras()
    return 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nPrograma finalizado por usuario.")
        sys.exit(0)
