import random
import math
from typing import List

def are_relatively_prime(a, b):
    """ Проверяет являются ли два числа взаимнопростыми."""
    if evklid(a, b) == 1:
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
    while (not(is_prime(p)) or not(is_prime(q)) or
        not(math.log2(k) == math.floor(math.log2(p + 1))) or 
        not(math.log2(k) == math.floor(math.log2(q + 1)))):
        p = random.randint(2, k) ####
        q = random.randint(2, k) ####    
    n = p*q
    f = (p - 1) * (q - 1)
    e = 65537
    while adv_evk(e,f)[2] != 1:
        r = adv_evk(e,f)
    d = r[1]
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
