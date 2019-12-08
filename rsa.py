def evklid(m, n):
    while n * m > 0:
        if n > m:
            n = n % m 
        else:
            m = m % n
    return (m + n) 

def phi(n):
    result = 1
    for i in range(2, n): 
        if(evklid(i, n) == 1):
            result+=1
    return result 

def rsa(p,q):
    flag1 = True
    flag2 = True
    for i in range(2, int(p**0.5) + 1): 
        if p % i == 0:
            flag1 = False
    for i in range(2, int(q**0.5) + 1): 
        if q % i == 0:
            flag2 = False
    if (flag1 == False) or (flag2 == False):
        raise ValueError('One of the numbers is not prime')
    else:
        n = p*q
        f = phi(n)
        openk = 0
        i = 2
        while i < f:
            e = evklid(f, i)
            if e == 1:
                openk = i
                break
            i += 1
        i = 2
        while i < n:
            if (i * openk) % f == 1:
                closek = i
                break
            i += 1
        r = ((n, openk),(n, closek))
        return r

def encode_rsa(p, q, m):
    r = rsa(p,q)
    c = m**r[0][1] % r[0][0]
    return c

def decode_rsa(p, q, c):
    r = rsa(p,q)
    m = c**r[1][1] % r[1][0]
    return m


