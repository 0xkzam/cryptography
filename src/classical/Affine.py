from Cipher import Cipher

class Affine(Cipher):

    def encrypt(self, text, key):
        
        a, b = key
        m = 26 # English alphabet
        
        cipher = ""

        for char in text:

            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                x = ord(char) - offset
                c = (a * x + b) % m       
                cipher += chr( offset + c ) 
            else:
                cipher += char
        
        return cipher

    def decrypt(self, cipher, key):
        a, b = key
        m = 26 # English alphabet
        
        text = ""

        for char in cipher:

            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                x = ord(char) - offset

                a_inv = self.mod_inverse(a, m)                
                c = (a_inv *(x-b)) % m    
                
                text += chr( offset + c ) 
            else:
                text += char        
        return text
    
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(self, a, m):
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m
