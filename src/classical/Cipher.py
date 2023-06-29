from abc import ABC, abstractmethod

class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text, key):
        pass

    @abstractmethod
    def decrypt(self, cipher, key):
        pass