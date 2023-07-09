from unittest import TestCase

from classical.Caesar import Caesar
from classical.Vigenere import Vigenere
from classical.Affine import Affine


class TestCaesar(TestCase):
    def test(self):
        caesar = Caesar()
        self.assertEqual(caesar.encrypt("hello world"), "khoor zruog")
        self.assertEqual(caesar.decrypt("khoor zruog"), "hello world")

        self.assertEqual(caesar.encrypt("hello 2 world!"), "khoor 2 zruog!")
        self.assertEqual(caesar.decrypt("khoor 2 zruog!"), "hello 2 world!")

        self.assertEqual(caesar.encrypt("Hello WORLD 123"), "Khoor ZRUOG 123")
        self.assertEqual(caesar.decrypt("Khoor ZRUOG 123"), "Hello WORLD 123")


class TestVigenere(TestCase):
    def test(self):
        v = Vigenere()
        key = "myKey"

        # edge case: empty string
        self.assertEqual(v.encrypt("", key), "")
        self.assertEqual(v.decrypt("", key), "")

        # edge case: string only contains spaces
        self.assertEqual(v.encrypt("   ", key), "   ")
        self.assertEqual(v.decrypt("   ", key), "   ")

        # edge case: string only contains non-alphabetic characters
        self.assertEqual(v.encrypt("1234567890!@#$%^&*()", key), "1234567890!@#$%^&*()")
        self.assertEqual(v.decrypt("1234567890!@#$%^&*()", key), "1234567890!@#$%^&*()")

        # edge case: string with all alphabets, uppercase and lowercase
        self.assertEqual(v.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", key),
                         "MZMHCRERMHWJWRMBOBWRGTGBWLylgbqdqlgvivqlanavqfsfavkx")
        self.assertEqual(v.decrypt("MZMHCRERMHWJWRMBOBWRGTGBWLylgbqdqlgvivqlanavqfsfavkx", key),
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        # edge case: very long string
        self.assertEqual(v.decrypt(v.encrypt("A" * 10000, key), key), "A" * 10000)

        # edge case: key is a single character

        try:
            single_char_key = "A"
            self.assertEqual(v.encrypt("Hello, World!", single_char_key), "Jvjah, Ewtcb!")
        except ValueError as e:
            print("")

        # edge case: key is longer than the text
        long_key = "ThisIsALongKeyThatIsLongerThanTheText"
        self.assertFalse(v.encrypt("Hello", long_key), "Hello")
        self.assertEqual(v.decrypt(v.encrypt("Hello", long_key), long_key), "Hello")

        self.assertEqual(v.encrypt("hello world", key), "tcvpm imbpb")
        self.assertEqual(v.decrypt("tcvpm imbpb", key), "hello world")

        self.assertEqual(v.encrypt("hello 2 world!", key), "tcvpm 2 imbpb!")
        self.assertEqual(v.decrypt("tcvpm 2 imbpb!", key), "hello 2 world!")

        self.assertEqual(v.encrypt("Hello WORLD 123", key), "Tcvpm IMBPB 123")
        self.assertEqual(v.decrypt("Tcvpm IMBPB 123", key), "Hello WORLD 123")


class TestAffine(TestCase):
    def test(self):
        a = Affine()
        key = (5, 8)

        # edge case: empty string
        self.assertEqual(a.encrypt("", key), "")
        self.assertEqual(a.decrypt("", key), "")

        # edge case: string only contains spaces
        self.assertEqual(a.encrypt("   ", key), "   ")
        self.assertEqual(a.decrypt("   ", key), "   ")

        # edge case: string only contains non-alphabetic characters
        self.assertEqual(a.encrypt("1234567890!@#$%^&*()", key), "1234567890!@#$%^&*()")
        self.assertEqual(a.decrypt("1234567890!@#$%^&*()", key), "1234567890!@#$%^&*()")

        self.assertEqual(a.encrypt("Hello World!", key), "Rclla Oaplx!")
        self.assertEqual(a.decrypt("Rclla Oaplx!", key), "Hello World!")

        # edge case: string with all alphabets, uppercase and lowercase
        self.assertEqual(a.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", key),
                         "INSXCHMRWBGLQVAFKPUZEJOTYDinsxchmrwbglqvafkpuzejotyd")
        self.assertEqual(a.decrypt("INSXCHMRWBGLQVAFKPUZEJOTYDinsxchmrwbglqvafkpuzejotyd", key),
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        # edge case: very long string
        self.assertEqual(a.decrypt(a.encrypt("A" * 10000, key), key), "A" * 10000)
