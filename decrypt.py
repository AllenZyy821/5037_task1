import os
import time

import Crypto
from Crypto.Util import Padding
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import libnum
import gmpy2

n = 0
e = 0
d = 0
PIN = 0
En = 0


def read_txt():
    f = open("32747918.txt", "r")
    uid = f.readline().strip('\n')
    print("current student id: " + uid)
    global n, e, En
    n = int(f.readline().strip('\n'))
    print("n: ", n)
    e = int(f.readline().strip('\n'))
    print("e:", e)
    f.readline()
    En = int(f.readline().strip('\n'))
    print("En: ", En)


# pow mod 65537
def powMod(a, b, c):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % c
        b = b // 2
        a = a * a % c
    return r


def decrypt():
    global d, PIN
    # brute solve p,q and then get d
    # gmpy2.invert function needs mpz
    # d = gmpy2.invert(e, n)
    # PIN = pow(En, d, n)
    # print(PIN)
    t = time.time()
    #   brute recur 000000
    for i in range(1000000):
        if powMod(i, e, n) == En:
            print(i, f"time: {time.time() - t}")
            PIN = i
            print("PIN: ", i)
            break


if __name__ == '__main__':
    read_txt()
    decrypt()
