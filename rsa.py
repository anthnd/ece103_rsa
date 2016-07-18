import math, pyperclip, textwrap, random, sys
sys.setrecursionlimit(1000000)

def stringToAscii(string):
    codeList = ""
    for letter in string:
        codeList += (getThreeDigitAscii(letter))
    return codeList

def asciiToString(asciiStr):
    length = len(str(asciiStr))
    s = ""
    if (length % 3 == 2):
        s = "0" + str(asciiStr)
    elif (length % 3 == 1):
        s = "00" + str(asciiStr)
    else:
        s = str(asciiStr)

    codeList = textwrap.wrap(s, 3)
    msg = ""
    for code in codeList:
        msg += toCharCode(code)
    return msg

def getThreeDigitAscii(char):
    strcode = str(ord(char))
    length = len(strcode)
    if length == 1:
        return "00" + strcode
    elif length == 2:
        return "0" + strcode
    else:
        return strcode

def toCharCode(string):
    cleanInt = int(string.lstrip("0"))
    return chr(cleanInt)

def encrypt(message, e, n):
    m = int(message)
    cipher = pow(m, e, n)
    return cipher

def decrypt(cipher, d, n):
    return pow(int(cipher), int(d), int(n))

def rabinMiller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v!= 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num

    return True

def isPrime(num):
    if num < 2:
        return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    return rabinMiller(num)

def generateLargePrimes(keysize=1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b//a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

    

# Get user input
## Decryption main loop
##print("Enter cipher: \n")
userInput = input()
##print("d:\n")
##d = input()
##print("n:\n")
##n = input()
##print(asciiToString(decrypt(userInput, d, n)))

## Convert to ASCII
asciiString = stringToAscii(userInput)
#print(asciiString)
message = asciiToString(asciiString)
#print(message)
#print()

### Get provided e and n from .txt
f = open('martin_rsa_keys.txt', 'r')
message = f.read()
#print(message)
eloc = message.find("e = ")
e = int(message[eloc+4:])
nloc = message.find("n = ")
n = int(message[nloc+4:eloc])
#print()


# Encrypt the user input using the e and n
print("Encrypted message: \n" + str(encrypt(asciiString.lstrip("0"), e, n)))

# Key generation output
##p = generateLargePrimes()
##q = generateLargePrimes()
##e = 70001
##phi = (p-1)*(q-1)
##
##print("p: " + str(p))
##print("q: " + str(q))
##print("e: " + str(e))
##print("n: " + str(p*q))
##print("phi: " + str(phi))
##print("d: " + str(modinv(e, phi)))
