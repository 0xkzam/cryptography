from .Cipher import Cipher
from .Caesar import Caesar


class Vigenere(Cipher):

    def encrypt(self, text: str, key) -> str:
        return self._perform(True, text, key)

    def decrypt(self, cipher: str, key) -> str:
        return self._perform(False, cipher, key)

    def _perform(self, encrypt: bool, message: str, key) -> str:

        if len(key) <= 1:
            raise ValueError("Key must have minimum 2 alpha characters")

        caesar = Caesar()

        key = key.upper()
        ord_offset = ord('A')
        key_indexes = [(ord(c) - ord_offset) for c in key]

        text = ""
        alpha_index = 0

        for i in range(len(message)):
            char = message[i]

            if char.isalpha():
                key_index = alpha_index % len(key_indexes)
                if char.islower():
                    ord_offset = ord('a')
                else:
                    ord_offset = ord('A')

                if encrypt:
                    text += caesar._perform(True, char, key_indexes[key_index])
                else:
                    text += caesar._perform(False, char, key_indexes[key_index])

                alpha_index += 1
            else:
                text += char

        return text
