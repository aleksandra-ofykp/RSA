import sympy
from typing import List

def are_relatively_prime(a, b):
    """ Проверяет являются ли два числа взаимнопростыми."""
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True

def evklid(m, n):
    """ Находит НОД двух чисел.
    
    На вход принимает два числа.
    Возвращает НОД.

    """
    while n * m > 0:
        if n > m:
            n = n % m 
        else:
            m = m % n
    return (m + n) 

def is_prime(n):
    """ Проверяет число на простоту. 
    
    На вход принимает число. (n > 0) 
    На выход выдает:
    True, если число простое,
    False, если число сложное. 

    """
    return sympy.isprime(n)

def rsa(p,q):
    """ Составляет открытый и закрытый ключ по алгоритму RSA.

    На вход принимает два простых числа. (Если хотя бы 
    одно из чисел не является простым, возвращает исключение).
    Вычисляет их произведение n, которое называется модулем.
    Вычисляет значение функции Эйлера f(n).
    Выбирается произвольное число e,
    взаимно простое со значением функции f(n).
    С помощью алгоритма Евклида вычисляется число,
    которое удовлетворяет условию de == 1 mod f(n). Возвращает:
    Пару {n,e} - публикуется в качестве открытого ключа RSA.
    Пару {n,d} - играет роль закрытого ключа RSA.

    """
    if  not(is_prime(p)) or not(is_prime(q)):
        raise ValueError('One of the numbers is not prime')
    else:
        n = p*q
        f = (p - 1)*(q - 1)
        for e in range(3, f, 2):
            if are_relatively_prime(e, f):
                break
        for d in range(3, f, 2):
            if d * e % f == 1:
                break
        pubk = (n, e)
        prk = (n, d)
        return list(pubk),list(prk)

def encode_rsa(pubk : List, m): 
    """ Кодирует сообщение с помощью открытого ключа RSA.

    На вход получает открытый ключ и сообщение.
    Возвращает закодированное сообщение.

    """
    c = m**pubk[1] % pubk[0]
    return c

def decode_rsa(prk : List, c):
    """ Декодирует сообщение с помощью закрытого ключа RSA.

    На вход получает закрытый ключ и закодированное сообщение.
    Возвращает декодированное сообщение.
    
    """
    m = c**prk[1] % prk[0]
    return m


