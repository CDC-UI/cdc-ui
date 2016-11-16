#!/usr/bin/env python
# Works in Python 2 and 3

# Author: Antonymous
"""
This module provides a suite of functions
which illustrate basic homomorphic multiplication under RSA.
This module only provides an educational
example of homomorphic multiplicaiton and should
not be used outside this project. For many, hopfully obvious, reasons.
"""

class Client:
    """A Client for RSA homomorphic multiplication"""

    # Default pub/pri keys use primes p, q: p = 2017, q = 997
    # though the user should provide their own keys
    def __init__(self, pub=(2010949,6007), pri=1627207):
        self.N = pub[0] # Store public modulus N
        self.e = pub[1] # Store public exponent e
        self.d = pri    # Store private key d
        print("Client N: %d\nClient e: %d\nClient d: %d"
              % (self.N, self.e, self.d))

    def encrypt(self, number):
        print("Client Encrypted: %d to %d"
              % (number, pow(number, self.e, self.N)))
        return pow(number, self.e, self.N)  # return x^e mod N

    def decrypt(self, number):
        print("Client Decrypted: %d to %d"
              % (number, pow(number, self.d, self.N)))
        return pow(number, self.d, self.N)  # return y^d mod N

    def multiply(self, server, a, b):
        print("Computing: %d * %d"
              % (a, b))
        ca = self.encrypt(a)    # Encrypt the first operand
        cb = self.encrypt(b)    # Encrypt the second operand
        print("Client Sends: %d, %d, mod %d to Server"
              % (ca, cb, self.N))
        sval = server.multiply(ca, cb, self.N)  # Send encrypted data to server
        print("Client Received: %d from Server"
               % (sval))
        result = self.decrypt(sval) # Decrypt result from server
        print("Computed: %d"
              % (result))
        return result

class Server:
    """ A Server for RSA homomorphic multiplication"""

    def multiply(self, a, b, N):
        print("Server Received: %d, %d, mod %d from Client"
              % (a, b, N))
        print("Server Sends: %d to Client"
              % (a * b % N))
        return a * b % N    # return a * b mod N

if __name__ == '__main__':
    c = Client()
    s = Server()
    result = c.multiply(s, 3, 7)
    print(result)
