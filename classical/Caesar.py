from .Cipher import Cipher


class Caesar(Cipher):
    def encrypt(self, text: str, key="") -> str:
        return self._perform(True, text)

    def decrypt(self, cipher: str, key="") -> str:
        return self._perform(False, cipher)

    def _perform(self, encrypt: bool, message: str, shift=3) -> str:
        """
        Caesar Cipher

        :param encrypt - True for encryption, False for decryption
        :param shift - default value = 3
        """
        text = ""

        for char in message:
            if char.isalpha():
                if char.islower():
                    ord_offset = ord('a')
                else:
                    ord_offset = ord('A')

                if encrypt:
                    text += chr(((ord(char) - ord_offset + shift) % 26) + ord_offset)
                else:
                    text += chr(((ord(char) - ord_offset - shift) % 26) + ord_offset)
            else:
                text += char

        return text
