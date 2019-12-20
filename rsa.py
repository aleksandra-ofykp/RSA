import random
import math
from typing import List

def are_relatively_prime(a, b):
    """ Проверяет являются ли два числа взаимнопростыми."""
    if evklid(a, b) == 1:
        return True



def prime(n, k = 50):
    """ Тест Миллера-Рабина."""

    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if n < 2:
        return False
    for p in prime:
        if n < p * p:
            return True
        if n % p == 0:
            return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def adv_evk(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = adv_evk(b, a % b)
    return (x, y - (a // b) * x, g)

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
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: 
            return False
    return n > 1

def pow_mod(x, n, mod):
    """ Выполняет возведение в степень по модулю. 
    
    На вход принимает три числа. 
    На выход выдает:
    Результат возведения в ст. по модулю. 

    """
    res = 1
    while n != 0:
        if n % 2 != 0:
            res *= x
            res %= mod
            n -= 1
        else:
            x *= x
            x %= mod
            n /= 2
    return res

def rsa(k):
    """ Составляет открытый и закрытый ключ по алгоритму RSA.

    Генерируется два простых числа.
    Вычисляет их произведение n, которое называется модулем.
    Вычисляет значение функции Эйлера f(n).
    Выбирается произвольное число e,
    взаимно простое со значением функции f(n).
    С помощью алгоритма Евклида вычисляется число,
    которое удовлетворяет условию de == 1 mod f(n). Возвращает:
    Пару {n,e} - публикуется в качестве открытого ключа RSA.
    Пару {n,d} - играет роль закрытого ключа RSA.

    """
    p = 4
    q = 4  
    e = 65537
    while (not(prime(p)) or not(prime(q))):
        p = random.randint(k, 2**k) ####
        q = random.randint(k, 2**k) ####    
    n = p*q
    f = (p - 1) * (q - 1)
   
    assert adv_evk(e,f)[2] == 1
       
    d = adv_evk(e,f)[0]
    while d < 0:
        d += f
    pubk = (n, e)
    prk = (n, d)
    return list(pubk),list(prk)

def encode_rsa(pubk : List, m): 
    """ Кодирует сообщение с помощью открытого ключа RSA.

    На вход получает открытый ключ и сообщение.
    Возвращает закодированное сообщение.

    """
    c = pow_mod(m, pubk[1],pubk[0])
    return c

def decode_rsa(prk : List, c):
    """ Декодирует сообщение с помощью закрытого ключа RSA.

    На вход получает закрытый ключ и закодированное сообщение.
    Возвращает декодированное сообщение.
    
    """
    m = pow_mod(c, prk[1], prk[0])
    return m
