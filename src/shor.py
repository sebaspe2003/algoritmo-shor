"""
Shor's Algorithm (Simulated Classical Version)
----------------------------------------------
Este script implementa una versión clásica del algoritmo de Shor para factorizar un número entero N.
Para propósitos educativos, no usa una computadora cuántica, sino que simula los pasos.

Autor: Tu Nombre
Repositorio: https://github.com/tu_usuario/ShorAlgorithm
"""

import random
import math
from sympy import gcd, isprime


def is_power(n):
    """Verifica si n es una potencia exacta de algún número entero"""
    for b in range(2, int(math.log2(n)) + 1):
        a = int(round(n ** (1 / b)))
        if a ** b == n:
            return True
    return False


def modular_pow(base, exponent, modulus):
    """Exponenciación modular rápida: (base^exponent) mod modulus"""
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result


def find_order(a, N):
    """Busca el orden r tal que a^r mod N = 1"""
    r = 1
    while r < N:
        if modular_pow(a, r, N) == 1:
            return r
        r += 1
    return None


def shor(N):
    """Implementa el algoritmo de Shor de forma simulada"""
    print(f"\n--- Factoring N = {N} ---")

    if N % 2 == 0:
        return 2, N // 2
    if isprime(N):
        print("El número es primo. No se puede factorizar.")
        return None
    if is_power(N):
        print("El número es una potencia exacta. No se necesita Shor.")
        return None

    while True:
        a = random.randrange(2, N)
        g = gcd(a, N)
        if g > 1:
            return g, N // g

        r = find_order(a, N)
        if r is None or r % 2 != 0:
            continue

        x = modular_pow(a, r // 2, N)
        if x == N - 1 or x == 1:
            continue

        p = gcd(x - 1, N)
        q = gcd(x + 1, N)

        if p * q == N:
            return p, q


def main():
    print("Algoritmo de Shor (Simulado)")
    try:
        N = int(input("Ingrese un número entero a factorizar (N > 1): "))
        if N <= 1:
            raise ValueError

        result = shor(N)
        if result:
            p, q = result
            print(f"\n✅ Factores encontrados: {p} × {q} = {N}")
        else:
            print("❌ No se encontraron factores. Intenta con otro número.")
    except ValueError:
        print("Por favor ingrese un número válido mayor que 1.")


if __name__ == "__main__":
    main()
